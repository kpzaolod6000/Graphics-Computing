#include "Utils.h"
#include "Solver_Navier_Stokes.h"

using namespace std;

#define numVAOs 1
#define numVBOs 2

float cameraX, cameraY, cameraZ;
float cubeLocX, cubeLocY, cubeLocZ;

GLuint renderingProgram;
GLuint vao[numVAOs];
GLuint vbo[numVBOs];



// asigna las variables utilizadas en la función display (), de modo que no sea necesario asignarlas durante el renderizado 
GLuint mvLoc, projLoc;
int width, height;
float aspect;
glm::mat4 pMat, vMat, mMat, mvMat;


//fluid field information
static int N = SIZE; // grid x

static float dt = 0.4f; // time delta
static float diff = 0.0f; // diffuse
static float visc = 0.0f; // viscosity
static float force = 10.0f;  // added on keypress on an axis
static float source = 200.0f; // density
static float source_alpha = 0.05; //for displaying density

static int addforce[3] = { 0, 0, 0 };
static int addsource = 0;

static float* u, * v, * w, * u_prev, * v_prev, * w_prev;
static float* dens, * dens_prev;

static int dvel = 0;
static int dhelp = 1;
static int daxis = 0;

static int win_id;
static int win_x = WINDOW_WIDTH;
static int  win_y = WINDOW_HEIGHT;

static int mouse_down[3];
static int omx, omy, mx, my;


GLfloat trans[3];
GLfloat rot[2];


static void free_data(void)
{
	if (u) free(u);
	if (v) free(v);
	if (w) free(w);
	if (u_prev) free(u_prev);
	if (v_prev) free(v_prev);
	if (w_prev) free(w_prev);
	if (dens) free(dens);
	if (dens_prev) free(dens_prev);
}

static void clear_data(void)
{
	int i, size = (N + 2) * (N + 2) * (N + 2);

	for (i = 0; i < size; i++) {
		u[i] = v[i] = w[i] = u_prev[i] = v_prev[i] = w_prev[i] = dens[i] = dens_prev[i] = 0.0f;
	}


}

static int allocate_data(void)
{
	int size = (N + 2) * (N + 2) * (N + 2);

	u = (float*)malloc(size * sizeof(float));
	v = (float*)malloc(size * sizeof(float));
	w = (float*)malloc(size * sizeof(float));
	u_prev = (float*)malloc(size * sizeof(float));
	v_prev = (float*)malloc(size * sizeof(float));
	w_prev = (float*)malloc(size * sizeof(float));
	dens = (float*)malloc(size * sizeof(float));
	dens_prev = (float*)malloc(size * sizeof(float));

	if (!u || !v || !w || !u_prev || !v_prev || !w_prev || !dens || !dens_prev) {
		fprintf(stderr, "cannot allocate data\n");
		return (0);
	}

	return (1);
}


static void get_force_source(float* d, float* u, float* v, float* w)
{
	int i, j, k, size = (N + 2) * (N + 2) * (N + 2);;

	for (i = 0; i < size; i++) {
		u[i] = v[i] = w[i] = d[i] = 0.0f;
	}

	//ADD SOURCE
	int mitad = N / 2;
	i = mitad,
		j = mitad;
	k = mitad;
	d[IX(i, j, k)] = source;
	//addsource = 0;

	//ADD FORCE
	i = mitad;
	j = 2;
	k = mitad;

	if (i<1 || i>N || j<1 || j>N || k <1 || k>N) return;
	v[IX(i, j, k)] = force * 10;

	return;
}

void key_callback(GLFWwindow*  , int key, int scancode, int action, int mods)
{
	switch (key) {
		case 'w':       // 'W' key - apply force x-axis
			addforce[1] = 1;
			break;
		case 'x':       // 'X' key - add source at centre
			addsource = 1;
			break;
	}
}

void window_size_callback(GLFWwindow* window, int width, int height)

{
	glfwSetWindowSize(window, width, height);
	win_x = width;
	win_y = height;
}

void idle_func()
{
	get_force_source(dens_prev, u_prev, v_prev, w_prev);
	vel_step(N, u, v, w, u_prev, v_prev, w_prev, visc, dt);
	dens_step(N, dens, dens_prev, u, v, w, diff, dt);
}

void setupV(void) { // 36 vértices, 12 triángulos, hace un cubo de 2x2x2 colocado en el origen 
	/*float vertexPositions[108] = {
	 -1.0f, 1.0f, -1.0f, -1.0f, -1.0f, -1.0f, 1.0f, -1.0f, -1.0f,//triangulo
	 1.0f, -1.0f, -1.0f, 1.0f, 1.0f, -1.0f, -1.0f, 1.0f, -1.0f,
	 1.0f, -1.0f, -1.0f, 1.0f, -1.0f, 1.0f, 1.0f, 1.0f, -1.0f,
	 1.0f, -1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, -1.0f,
	 1.0f, -1.0f, 1.0f, -1.0f, -1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
	 -1.0f, -1.0f, 1.0f, -1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
	 -1.0f, -1.0f, 1.0f, -1.0f, -1.0f, -1.0f, -1.0f, 1.0f, 1.0f,
	 -1.0f, -1.0f, -1.0f, -1.0f, 1.0f, -1.0f, -1.0f, 1.0f, 1.0f,
	 -1.0f, -1.0f, 1.0f, 1.0f, -1.0f, 1.0f, 1.0f, -1.0f, -1.0f,
	 1.0f, -1.0f, -1.0f, -1.0f, -1.0f, -1.0f, -1.0f, -1.0f, 1.0f,
	 -1.0f, 1.0f, -1.0f, 1.0f, 1.0f, -1.0f, 1.0f, 1.0f, 1.0f,
	 1.0f, 1.0f, 1.0f, -1.0f, 1.0f, 1.0f, -1.0f, 1.0f, -1.0f
	};*/
	glGenVertexArrays(1, vao);
	glBindVertexArray(vao[0]);
	glGenBuffers(numVBOs, vbo);

	/*
	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertexPositions), vertexPositions, GL_STATIC_DRAW);*/

}

void init(GLFWwindow* window) {
	const char* vertShader = "Shaders/vertShader.glsl";
	const char* fragShader = "Shaders/fragShader.glsl";
	//if (!allocate_data()) return;

	allocate_data();
	renderingProgram = Utils::createShaderProgram(vertShader, fragShader);
	cameraX = 0.0f; cameraY = 5.0f; cameraZ = 16.0f;
	cubeLocX = 0.0f; cubeLocY = -2.0f; cubeLocZ = 0.0f;  //desplaza hacia abajo Y para revelar la perspectiva
	setupV();
	rot[0] = 30;
	rot[1] = -45;
}

void display(GLFWwindow* window, double currentTime) {
	

	glClear(GL_DEPTH_BUFFER_BIT);
	glClearColor(0.0, 0.0, 0.0, 1.0);
	glClear(GL_COLOR_BUFFER_BIT);
	glUseProgram(renderingProgram);//instalando el código GLSL en la GPU.

	//draw_density();
	//glfwSetKeyCallback(window, key_callback);
	//glfwSetWindowSizeCallback(window, window_size_callback);
	idle_func();
	//obtener las variables uniformes para las matrices de MV y proyección
	mvLoc = glGetUniformLocation(renderingProgram, "mv_matrix");
	projLoc = glGetUniformLocation(renderingProgram, "proj_matrix");

	// construir la matriz de prespectiva
	glfwGetFramebufferSize(window, &width, &height);
	aspect = (float)width / (float)height;
	pMat = glm::perspective(1.0472f, aspect, 0.1f, 1000.0f); // 1.0472 radians = 60 degrees

	// construir view matrix, model matrix, and model-view matrix
	vMat = glm::translate(glm::mat4(1.0f), glm::vec3(-cameraX, -cameraY, -cameraZ));
	mMat = glm::translate(glm::mat4(1.0f), glm::vec3(cubeLocX, cubeLocY, cubeLocZ));
	mvMat = vMat * mMat;

	// copiar matrices de perspectiva y MV a las correspondientes variables uniformes 
	glUniformMatrix4fv(mvLoc, 1, GL_FALSE, glm::value_ptr(mvMat));
	glUniformMatrix4fv(projLoc, 1, GL_FALSE, glm::value_ptr(pMat));
	glPushMatrix();
	glTranslatef(0, 0,0);
	glRotatef(30, 1.0f, 0.0f, 0.0f);
	glRotatef(-45, 0.0f, 1.0f, 0.0f);

	int i, j, k;
	float x, y, z, h, d000, d010, d100, d110, d001, d011, d101, d111;

	h = 1.0f / N;

	glBegin(GL_QUADS);

	for (i = 0; i <= N; i++) {
		x = (i - 0.5f) * h;
		for (j = 0; j <= N; j++) {
			y = (j - 0.5f) * h;
			for (k = 0; k <= N; k++) {
				z = (k - 0.5f) * h;

				d000 = dens[IX(i, j, k)];
				d010 = dens[IX(i, j + 1, k)];
				d100 = dens[IX(i + 1, j, k)];
				d110 = dens[IX(i + 1, j + 1, k)];

				d001 = dens[IX(i, j, k + 1)];
				d011 = dens[IX(i, j + 1, k + 1)];
				d101 = dens[IX(i + 1, j, k + 1)];
				d111 = dens[IX(i + 1, j + 1, k + 1)];

				// draw density as a cube of quads

				glColor4f(d111, d111, d111, source_alpha); glVertex3f(x + h, y + h, z + h);
				glColor4f(d011, d011, d011, source_alpha); glVertex3f(x, y + h, z + h);
				glColor4f(d001, d001, d001, source_alpha); glVertex3f(x, y, z + h);
				glColor4f(d101, d101, d101, source_alpha); glVertex3f(x + h, y, z + h);

				glColor4f(d110, d110, d110, source_alpha); glVertex3f(x + h, y + h, z);
				glColor4f(d111, d111, d111, source_alpha); glVertex3f(x + h, y + h, z + h);
				glColor4f(d101, d101, d101, source_alpha); glVertex3f(x + h, y, z + h);
				glColor4f(d100, d100, d100, source_alpha); glVertex3f(x + h, y, z);

				glColor4f(d010, d010, d010, source_alpha); glVertex3f(x, y + h, z);
				glColor4f(d110, d110, d110, source_alpha); glVertex3f(x + h, y + h, z);
				glColor4f(d100, d100, d100, source_alpha); glVertex3f(x + h, y, z);
				glColor4f(d000, d000, d000, source_alpha); glVertex3f(x, y, z);

				glColor4f(d011, d011, d011, source_alpha); glVertex3f(x, y + h, z + h);
				glColor4f(d010, d010, d010, source_alpha); glVertex3f(x, y + h, z);
				glColor4f(d000, d000, d000, source_alpha); glVertex3f(x, y, z);
				glColor4f(d001, d001, d001, source_alpha); glVertex3f(x, y, z + h);

				glColor4f(d100, d100, d100, source_alpha); glVertex3f(x + h, y, z);
				glColor4f(d000, d000, d000, source_alpha); glVertex3f(x, y, z);
				glColor4f(d001, d001, d001, source_alpha); glVertex3f(x, y, z + h);
				glColor4f(d101, d101, d101, source_alpha); glVertex3f(x + h, y, z + h);

				glColor4f(d110, d110, d110, source_alpha); glVertex3f(x + h, y + h, z);
				glColor4f(d010, d010, d010, source_alpha); glVertex3f(x, y + h, z);
				glColor4f(d011, d011, d011, source_alpha); glVertex3f(x, y + h, z + h);
				glColor4f(d111, d111, d111, source_alpha); glVertex3f(x + h, y + h, z + h);
			}
		}
	}

	glEnd();
	
	glPopMatrix();
	clear_data();
	// asociar VBO con el atributo de vértice correspondiente en el sombreador de vértices 
	/*glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(0);

	// ajustar la configuración de OpenGL y dibujar el modelo 
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glDrawArrays(GL_TRIANGLES, 0, 36);*/
}


int main(void) { // main() is unchanged from before
	if (!glfwInit()) { exit(EXIT_FAILURE); }
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	GLFWwindow* window = glfwCreateWindow(768, 768, "Chapter 4 - Fluid Simulation", NULL, NULL);
	glfwMakeContextCurrent(window);
	if (glewInit() != GLEW_OK) { exit(EXIT_FAILURE); }
	glfwSwapInterval(1);
	init(window);
	while (!glfwWindowShouldClose(window)) {
		display(window, glfwGetTime());
		glfwSwapBuffers(window);
		glfwPollEvents();
	}
	glfwDestroyWindow(window);
	glfwTerminate();
	exit(EXIT_SUCCESS);
}
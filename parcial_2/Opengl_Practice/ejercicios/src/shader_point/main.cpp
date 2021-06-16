//#include <GL/glew.h>
#include <glad/glad.h>
#include <glfw/glfw3.h>

#include <iostream>

using namespace std;


#define numVAOs 1
GLuint renderingProgram; // "Unsigned int" proporcionado por OpenGL (
GLuint vao[numVAOs];

GLuint createShaderProgram() {
	const char *vshaderSource =
			"#version 430 \n" // version 4.3 glsl es parecido a c++
			"void main(void) \n"
			"{ gl_Position = vec4(0.0, 0.0, 0.0, 1.0); }"; // posicion de las coordenadas del vertice en el espacio 3D , origen (0,0,0)
	// creamos un vertice, no especificamos salida, porque gl_position es por defecto de salida
	const char *fshaderSource =
			"#version 430 \n"
			"out vec4 color; \n"// out indica que el variable color es una salida
			"void main(void) \n"
			"{ color = vec4(0.0, 0.0, 1.0, 1.0); }";
			//El propósito de cualquier shader de fragmentos es establecer el color RGB de un píxel que se mostrará. 
	//No fue necesario especificar una etiqueta "out" para gl_Position en el shader 
	//de vértices, porque gl_Position es una variable de salida predefinida).
	
	//en el etapss entre vertex y fragment, el vertice se convierte en un pixel
	//especificamos el color de los pixeles

	GLuint vShader = glCreateShader(GL_VERTEX_SHADER); //generando shader for vertex  vacios
	GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);//generando shader for fragment vacios
	 // y devuelve un ID de número entero para cada uno de los que es un índice para referenciarlo más tarde, 
	 // nuestro código almacena este ID en las variables vShader y fShader

	glShaderSource(vShader, 1, &vshaderSource, NULL);
	glShaderSource(fShader, 1, &fshaderSource, NULL);
	//Luego llama a glShaderSource (), que carga el código GLSL de las cadenas en los objetos de sombreado vacíos.
	//Las dos llamadas especifican el número de líneas de código en cada sombreador como "1";
	glCompileShader(vShader);
	glCompileShader(fShader);
	//compiladores 
	GLuint vfProgram = glCreateProgram();
	//Crea un objeto de programa llamado vfProgram y guarda el ID entero que apunta a él.
	//Un objeto de "programa" OpenGL contiene una serie de sombreadores(shaders) compilados, 
	//y aquí vemos los siguientes comandos: glCreateProgram () para crear el objeto de programa, 
	//glAttachShader () para adjuntar cada uno de los sombreadores(shaders) y luego glLinkProgram () 
	//para solicitar el compilador GLSL se asegura de que sean compatibles.
	glAttachShader(vfProgram, vShader);
	glAttachShader(vfProgram, fShader);
	glLinkProgram(vfProgram);
	return vfProgram;
}

void init(GLFWwindow* window) {
	renderingProgram = createShaderProgram();
	glGenVertexArrays(numVAOs, vao);
	glBindVertexArray(vao[0]);
}

void display(GLFWwindow* window, double currentTime) {
	glUseProgram(renderingProgram);
	//carga el programa que contiene los dos sombreadores compilados en las etapas de la canalización de OpenGL (¡en la GPU!).
	//no ejecuta los sombreadores, solo los carga en el hardware.
	glPointSize(30.0f); // un vertice es un pixel, con esto especificamos el tamaño del pixel
	glDrawArrays(GL_POINTS, 0, 1); 
	// La aplicación C ++ / OpenGL también es responsable de decirle a OpenGL que construya primitivas. 
	//El tipo primitivo es GL_POINTS
	//Hacemos esto usando la siguiente función OpenGL: glDrawArrays(GLenum mode, Glint first, GLsizei count);
	//Cuando se llama a glDrawArrays (), el código GLSL en la canalización comienza a ejecutarse.
	//glDrawArrays(GLenum mode, Glint first, GLsizei count);  GLenum mode= El modo es el tipo de primitiva
	//El modo es el tipo de primitiva; para los triángulos usamos GL_TRIANGLES. 
	//El parámetro "primero" (Glint first) indica con qué vértice comenzar (generalmente el vértice número 0, el primero), 
	//y count (GLsizei count) especifica el número total de vértices que se dibujarán.
}

int main(void) {
	if (!glfwInit()) { exit(EXIT_FAILURE); }
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);

	GLFWwindow* window = glfwCreateWindow(600, 600, "Chapter2 - program1", NULL, NULL);
	glfwMakeContextCurrent(window);

	//if (glewInit() != GLEW_OK) { exit(EXIT_FAILURE); }
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)){ exit(EXIT_FAILURE); }

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


//Independientemente de dónde se originen, todos los vértices pasan por el sombreador de vértices. 
//Lo hacen uno por uno; es decir, el sombreador se ejecuta una vez por vértice. 
//Para un modelo grande y complejo con muchos vértices, el sombreador de vértices
// puede ejecutarse cientos, miles o incluso millones de veces, a menudo en paralelo.

//los vértices se mueven a través de la tubería hasta el rasterizador, donde se transforman
// en ubicaciones de píxeles (o más exactamente, fragmentos; esto se describe más adelante).
///Finalmente, estos píxeles (fragmentos) llegan al sombreador de fragmentos:


 // la etapa de rasterización. Es allí donde las primitivas (como puntos o triángulos) 
 //se convierten en conjuntos de píxeles.
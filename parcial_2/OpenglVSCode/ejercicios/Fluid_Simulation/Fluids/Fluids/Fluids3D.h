
/*
A 3D Real Time Fluid Solver based on Jos Stam's fluid solver (stable N-S solver).

Reference: Jos Stam, "Real-Time Fluid Dynamics for Games". Proceedings of the Game Developer Conference, March 2003.
  *http://www.dgp.toronto.edu/people/stam/reality/Research/pdf/GDC03.pdf]
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//#include <GL\gl.h>
//#include <GL\glu.h>
#include <GL\glut.h>

#define IX(i,j,k) ((i)+(M+2)*(j) + (M+2)*(N+2)*(k))
#define SWAP(x0,x) {float * tmp=x0;x0=x;x=tmp;}
#define MAX(a,b)            (((a) > (b)) ? (a) : (b))
#define LINEARSOLVERTIMES 10

void add_source(int M, int N, int O, float* x, float* s, float dt)
{
	int i, size = (M + 2) * (N + 2) * (O + 2);
	for (i = 0; i < size; i++) x[i] += dt * s[i];
}

void  set_bnd(int M, int N, int O, int b, float* x)
{

	// bounds are cells at faces of the cube

	int i, j;

	//setting faces
	for (i = 1; i <= M; i++) {
		for (j = 1; j <= N; j++) {
			x[IX(i, j, 0)] = b == 3 ? -x[IX(i, j, 1)] : x[IX(i, j, 1)];
			x[IX(i, j, O + 1)] = b == 3 ? -x[IX(i, j, O)] : x[IX(i, j, O)];
		}
	}

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= O; j++) {
			x[IX(0, i, j)] = b == 1 ? -x[IX(1, i, j)] : x[IX(1, i, j)];
			x[IX(M + 1, i, j)] = b == 1 ? -x[IX(M, i, j)] : x[IX(M, i, j)];
		}
	}

	for (i = 1; i <= M; i++) {
		for (j = 1; j <= O; j++) {
			x[IX(i, 0, j)] = b == 2 ? -x[IX(i, 1, j)] : x[IX(i, 1, j)];
			x[IX(i, N + 1, j)] = b == 2 ? -x[IX(i, N, j)] : x[IX(i, N, j)];
		}
	}

	//Setting edges
	for (i = 1; i <= M; i++) {
		x[IX(i, 0, 0)] = 1.0 / 2.0 * (x[IX(i, 1, 0)] + x[IX(i, 0, 1)]);
		x[IX(i, N + 1, 0)] = 1.0 / 2.0 * (x[IX(i, N, 0)] + x[IX(i, N + 1, 1)]);
		x[IX(i, 0, O + 1)] = 1.0 / 2.0 * (x[IX(i, 0, O)] + x[IX(i, 1, O + 1)]);
		x[IX(i, N + 1, O + 1)] = 1.0 / 2.0 * (x[IX(i, N, O + 1)] + x[IX(i, N + 1, O)]);
	}

	for (i = 1; i <= N; i++) {
		x[IX(0, i, 0)] = 1.0 / 2.0 * (x[IX(1, i, 0)] + x[IX(0, i, 1)]);
		x[IX(M + 1, i, 0)] = 1.0 / 2.0 * (x[IX(M, i, 0)] + x[IX(M + 1, i, 1)]);
		x[IX(0, i, O + 1)] = 1.0 / 2.0 * (x[IX(0, i, O)] + x[IX(1, i, O + 1)]);
		x[IX(M + 1, i, O + 1)] = 1.0 / 2.0 * (x[IX(M, i, O + 1)] + x[IX(M + 1, i, O)]);
	}

	for (i = 1; i <= O; i++) {
		x[IX(0, 0, i)] = 1.0 / 2.0 * (x[IX(0, 1, i)] + x[IX(1, 0, i)]);
		x[IX(0, N + 1, i)] = 1.0 / 2.0 * (x[IX(0, N, i)] + x[IX(1, N + 1, i)]);
		x[IX(M + 1, 0, i)] = 1.0 / 2.0 * (x[IX(M, 0, i)] + x[IX(M + 1, 1, i)]);
		x[IX(M + 1, N + 1, i)] = 1.0 / 2.0 * (x[IX(M + 1, N, i)] + x[IX(M, N + 1, i)]);
	}

	//setting corners
	x[IX(0, 0, 0)] = 1.0 / 3.0 * (x[IX(1, 0, 0)] + x[IX(0, 1, 0)] + x[IX(0, 0, 1)]);
	x[IX(0, N + 1, 0)] = 1.0 / 3.0 * (x[IX(1, N + 1, 0)] + x[IX(0, N, 0)] + x[IX(0, N + 1, 1)]);

	x[IX(M + 1, 0, 0)] = 1.0 / 3.0 * (x[IX(M, 0, 0)] + x[IX(M + 1, 1, 0)] + x[IX(M + 1, 0, 1)]);
	x[IX(M + 1, N + 1, 0)] = 1.0 / 3.0 * (x[IX(M, N + 1, 0)] + x[IX(M + 1, N, 0)] + x[IX(M + 1, N + 1, 1)]);

	x[IX(0, 0, O + 1)] = 1.0 / 3.0 * (x[IX(1, 0, O + 1)] + x[IX(0, 1, O + 1)] + x[IX(0, 0, O)]);
	x[IX(0, N + 1, O + 1)] = 1.0 / 3.0 * (x[IX(1, N + 1, O + 1)] + x[IX(0, N, O + 1)] + x[IX(0, N + 1, O)]);

	x[IX(M + 1, 0, O + 1)] = 1.0 / 3.0 * (x[IX(M, 0, O + 1)] + x[IX(M + 1, 1, O + 1)] + x[IX(M + 1, 0, O)]);
	x[IX(M + 1, N + 1, O + 1)] = 1.0 / 3.0 * (x[IX(M, N + 1, O + 1)] + x[IX(M + 1, N, O + 1)] + x[IX(M + 1, N + 1, O)]);
}

void lin_solve(int M, int N, int O, int b, float* x, float* x0, float a, float c)
{
	int i, j, k, l;

	// iterate the solver
	for (l = 0; l < LINEARSOLVERTIMES; l++) {
		// update for each cell
		for (i = 1; i <= M; i++) {
			for (j = 1; j <= N; j++) {
				for (k = 1; k <= O; k++) {
					x[IX(i, j, k)] = (x0[IX(i, j, k)] + a * (x[IX(i - 1, j, k)] + x[IX(i + 1, j, k)] + x[IX(i, j - 1, k)] + x[IX(i, j + 1, k)] + x[IX(i, j, k - 1)] + x[IX(i, j, k + 1)])) / c;
				}
			}
		}
		set_bnd(M, N, O, b, x);
	}
}

void diffuse(int M, int N, int O, int b, float* x, float* x0, float diff, float dt)
{
	int max = MAX(MAX(M, N), MAX(N, O));
	float a = dt * diff * max * max * max;
	lin_solve(M, N, O, b, x, x0, a, 1 + 6 * a);
}

void advect(int M, int N, int O, int b, float* d, float* d0, float* u, float* v, float* w, float dt)
{
	int i, j, k, i0, j0, k0, i1, j1, k1;
	float x, y, z, s0, t0, s1, t1, u1, u0, dtx, dty, dtz;

	dtx = dty = dtz = dt * MAX(MAX(M, N), MAX(N, O));

	for (i = 1; i <= M; i++) {
		for (j = 1; j <= N; j++) {
			for (k = 1; k <= O; k++) {
				x = i - dtx * u[IX(i, j, k)]; y = j - dty * v[IX(i, j, k)]; z = k - dtz * w[IX(i, j, k)];
				if (x < 0.5f) x = 0.5f; if (x > M + 0.5f) x = M + 0.5f; i0 = (int)x; i1 = i0 + 1;
				if (y < 0.5f) y = 0.5f; if (y > N + 0.5f) y = N + 0.5f; j0 = (int)y; j1 = j0 + 1;
				if (z < 0.5f) z = 0.5f; if (z > O + 0.5f) z = O + 0.5f; k0 = (int)z; k1 = k0 + 1;

				s1 = x - i0; s0 = 1 - s1; t1 = y - j0; t0 = 1 - t1; u1 = z - k0; u0 = 1 - u1;
				d[IX(i, j, k)] = s0 * (t0 * u0 * d0[IX(i0, j0, k0)] + t1 * u0 * d0[IX(i0, j1, k0)] + t0 * u1 * d0[IX(i0, j0, k1)] + t1 * u1 * d0[IX(i0, j1, k1)]) +
					s1 * (t0 * u0 * d0[IX(i1, j0, k0)] + t1 * u0 * d0[IX(i1, j1, k0)] + t0 * u1 * d0[IX(i1, j0, k1)] + t1 * u1 * d0[IX(i1, j1, k1)]);
			}
		}
	}

	set_bnd(M, N, O, b, d);
}

void project(int M, int N, int O, float* u, float* v, float* w, float* p, float* div)
{
	int i, j, k;

	for (i = 1; i <= M; i++) {
		for (j = 1; j <= N; j++) {
			for (k = 1; k <= O; k++) {
				div[IX(i, j, k)] = -1.0 / 3.0 * ((u[IX(i + 1, j, k)] - u[IX(i - 1, j, k)]) / M + (v[IX(i, j + 1, k)] - v[IX(i, j - 1, k)]) / M + (w[IX(i, j, k + 1)] - w[IX(i, j, k - 1)]) / M);
				p[IX(i, j, k)] = 0;
			}
		}
	}

	set_bnd(M, N, O, 0, div); set_bnd(M, N, O, 0, p);

	lin_solve(M, N, O, 0, p, div, 1, 6);

	for (i = 1; i <= M; i++) {
		for (j = 1; j <= N; j++) {
			for (k = 1; k <= O; k++) {
				u[IX(i, j, k)] -= 0.5f * M * (p[IX(i + 1, j, k)] - p[IX(i - 1, j, k)]);
				v[IX(i, j, k)] -= 0.5f * M * (p[IX(i, j + 1, k)] - p[IX(i, j - 1, k)]);
				w[IX(i, j, k)] -= 0.5f * M * (p[IX(i, j, k + 1)] - p[IX(i, j, k - 1)]);
			}
		}
	}

	set_bnd(M, N, O, 1, u); set_bnd(M, N, O, 2, v); set_bnd(M, N, O, 3, w);
}

void dens_step(int M, int N, int O, float* x, float* x0, float* u, float* v, float* w, float diff, float dt)
{
	add_source(M, N, O, x, x0, dt);
	SWAP(x0, x); diffuse(M, N, O, 0, x, x0, diff, dt);
	SWAP(x0, x); advect(M, N, O, 0, x, x0, u, v, w, dt);
}

void vel_step(int M, int N, int O, float* u, float* v, float* w, float* u0, float* v0, float* w0, float visc, float dt)
{
	add_source(M, N, O, u, u0, dt); add_source(M, N, O, v, v0, dt); add_source(M, N, O, w, w0, dt);
	SWAP(u0, u); diffuse(M, N, O, 1, u, u0, visc, dt);
	SWAP(v0, v); diffuse(M, N, O, 2, v, v0, visc, dt);
	SWAP(w0, w); diffuse(M, N, O, 3, w, w0, visc, dt);
	project(M, N, O, u, v, w, u0, v0);
	SWAP(u0, u); SWAP(v0, v); SWAP(w0, w);
	advect(M, N, O, 1, u, u0, u0, v0, w0, dt); advect(M, N, O, 2, v, v0, u0, v0, w0, dt); advect(M, N, O, 3, w, w0, u0, v0, w0, dt);
	project(M, N, O, u, v, w, u0, v0);
}


#define WINDOW_TITLE "Fluid"
#define WINDOW_WIDTH 768
#define WINDOW_HEIGHT 768
#define SIZE 42 // Best not to raise this very high

//extern void dens_step(int M, int N, int O, float* x, float* x0, float* u, float* v, float* w, float diff, float dt);
//extern void vel_step(int M, int N, int O, float* u, float* v, float* w, float* u0, float* v0, float* w0, float visc, float dt);
void dens_step(int M, int N, int O, float* x, float* x0, float* u, float* v, float* w, float diff, float dt);
void vel_step(int M, int N, int O, float* u, float* v, float* w, float* u0, float* v0, float* w0, float visc, float dt);


//fluid field information
static int M = SIZE; // grid x
static int N = SIZE; // grid y
static int O = SIZE; // grid z
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

enum {
	PAN = 1,
	ROTATE,
	ZOOM
};

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
	int i, size = (M + 2) * (N + 2) * (O + 2);

	for (i = 0; i < size; i++) {
		u[i] = v[i] = w[i] = u_prev[i] = v_prev[i] = w_prev[i] = dens[i] = dens_prev[i] = 0.0f;
	}

	addforce[0] = addforce[1] = addforce[2] = 0;
}

static int allocate_data(void)
{
	int size = (M + 2) * (N + 2) * (O + 2);

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
	int i, j, k, size = (M + 2) * (N + 2) * (O + 2);;

	for (i = 0; i < size; i++) {
		u[i] = v[i] = w[i] = d[i] = 0.0f;
	}

	if (addforce[0] == 1) // x
	{
		i = 2,
			j = N / 2;
		k = O / 2;

		if (i<1 || i>M || j<1 || j>N || k <1 || k>O) return;
		u[IX(i, j, k)] = force * 10;
		addforce[0] = 0;
	}

	if (addforce[1] == 1)
	{
		i = M / 2,
			j = 2;
		k = O / 2;

		if (i<1 || i>M || j<1 || j>N || k <1 || k>O) return;
		v[IX(i, j, k)] = force * 10;
		addforce[1] = 0;
	}

	if (addforce[2] == 1) // y
	{
		i = M / 2,
			j = N / 2;
		k = 2;

		if (i<1 || i>M || j<1 || j>N || k <1 || k>O) return;
		w[IX(i, j, k)] = force * 10;
		addforce[2] = 0;
	}

	if (addsource == 1)
	{
		i = M / 2,
			j = N / 2;
		k = O / 2;
		d[IX(i, j, k)] = source;
		addsource = 0;
	}

	return;
}

static void draw_velocity(void)
{
	int i, j, k;
	float x, y, z, h;

	h = 1.0f / MAX(MAX(M, N), MAX(N, O));

	glColor3f(1.0f, 1.0f, 1.0f);
	glLineWidth(1.0f);

	glBegin(GL_LINES);

	for (i = 1; i <= M; i++) {
		x = (i - 0.5f) * h;
		for (j = 1; j <= N; j++) {
			y = (j - 0.5f) * h;
			for (k = 1; k <= O; k++) {
				z = (k - 0.5f) * h;

				glVertex3f(x, y, z);
				glVertex3f(x + u[IX(i, j, k)], y + v[IX(i, j, k)], z + w[IX(i, j, k)]);
			}
		}
	}

	glEnd();
}

static void draw_axis()
{

	glLineWidth(1.0f);
	glBegin(GL_LINES);

	glColor3f(1.0f, 0.0f, 0.0f);
	glVertex3f(0.25f, 0.f, 0.25f);
	glVertex3f(1.0f, 0.f, 0.25f);

	glColor3f(0.0f, 1.0f, 0.0f);
	glVertex3f(0.25f, 0.f, 0.25f);
	glVertex3f(0.25f, 1.0f, 0.25f);

	glColor3f(0.0f, 0.0f, 1.0f);
	glVertex3f(0.25f, 0.f, 0.25f);
	glVertex3f(0.25f, 0.f, 1.0f);

	glEnd();
}


static void draw_density(void)
{
	int i, j, k;
	float x, y, z, h, d000, d010, d100, d110, d001, d011, d101, d111;

	h = 1.0f / MAX(MAX(M, N), MAX(N, O));

	glBegin(GL_QUADS);

	for (i = 0; i <= M; i++) {
		x = (i - 0.5f) * h;
		for (j = 0; j <= N; j++) {
			y = (j - 0.5f) * h;
			for (k = 0; k <= O; k++) {
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
}

float clamp(float x) {
	return x > 360.0f ? x - 360.0f : x < -360.0f ? x += 360.0f : x;
}

static void update(int state, int ox, int nx, int oy, int ny)
{
	/* ideally, these values should be expressed in terms of window xy
	these magic numbers work for the sake of the demo,
	but consider the case of resizing the window. */

	int dx = ox - nx;
	int dy = ny - oy;

	switch (state) {
	case ROTATE:
		rot[0] += (dy * 180.0f) / 15000.0f;
		rot[1] -= (dx * 180.0f) / 15000.0f;
		rot[0] = clamp(rot[0]);
		rot[1] = clamp(rot[1]);
		break;
	case PAN:
		trans[0] -= dx / 15000.0f;
		trans[1] -= dy / 15000.0f;
		break;
	case ZOOM:
		trans[2] -= (dx + dy) / 100.0f;
		break;
	}
}


int init(void)
{

	rot[0] = 30;
	rot[1] = -45;

	if (!allocate_data())
		return (0);
	clear_data();

	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE);

	glEnable(GL_ALPHA_TEST);
	glAlphaFunc(GL_GREATER, 0);

	return (1);
}

void draw_text(GLint x, GLint y, char* s, GLfloat r, GLfloat g, GLfloat b)
{
	int lines;
	char* p;

	glMatrixMode(GL_PROJECTION);
	glPushMatrix();
	glLoadIdentity();

	gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT);
	glMatrixMode(GL_MODELVIEW);
	glPushMatrix();
	glLoadIdentity();
	glColor3f(r, g, b);
	glRasterPos2i(x, y);
	for (p = s, lines = 0; *p; p++) {
		if (*p == '\n')
		{
			lines++;
			glRasterPos2i(x, y - (lines * 24));
		}
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, *p);
	}
	glPopMatrix();
	glMatrixMode(GL_PROJECTION);
	glPopMatrix();
	glMatrixMode(GL_MODELVIEW);
}

void renderBitmapString(float x, float y, const char* string) {
	const char* c;
	glRasterPos2f(x, y);
	for (c = string; *c != '\0'; c++) {
		if (*c == '\n')
			glRasterPos2f(x, y -= 0.12);
		else
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
	}
}

void draw_help()
{
	glColor4f(0.8f, 0.8f, 0.8f, 1.0f);
	renderBitmapString(-0.5, 0.8,
		"Help:\n" \
		"      'X' key - add source at center\n" \
		"      'W' key - apply force x-axis\n" \
		"      'D' key - apply force y-axis\n" \
		"      'S' key - apply force z-axis\n" \
		"      'C' key - clear simulation\n" \
		"      'V' key - show/hide velocities\n" \
		"      'A' Key - show/hide the XYZ axis\n" \
		"      'H' key - show/hide this help message\n"\
		"      Left click  - pan from location\n" \
		"      Right click - rotate cube\n"\
		"      ESC - quit"\
	);

}



void sim_main(void)
{

	get_force_source(dens_prev, u_prev, v_prev, w_prev);
	vel_step(M, N, O, u, v, w, u_prev, v_prev, w_prev, visc, dt);
	dens_step(M, N, O, dens, dens_prev, u, v, w, diff, dt);

}

int shutdown(void)
{

	free_data();

	return 0;
}

void sim_reset()
{
	clear_data();
}

void reshape(int width, int height)
{
	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60.0, (float)width / height, 0.001, 100.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0.0f, 0.0f, -3.0f);
}

void display()
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glPushMatrix();
	glTranslatef(trans[0], trans[1], trans[2]);
	glRotatef(rot[0], 1.0f, 0.0f, 0.0f);
	glRotatef(rot[1], 0.0f, 1.0f, 0.0f);

	// toggle display modes
	if (dvel) draw_velocity();
	else		draw_density();
	if (dhelp) draw_help();
	if (daxis) draw_axis();

	glEnd();
	glPopMatrix();
	glFlush();
	glutSwapBuffers();
}

static void reshape_func(int width, int height)
{
	glutSetWindow(win_id);
	glutReshapeWindow(width, height);

	win_x = width;
	win_y = height;
}


static void key_func(unsigned char key, int x, int y)
{

	switch (key) {
	case 27:		// ESC key
		free_data();
		exit(0);
		break;
	case 'w':       // 'W' key - apply force x-axis
		addforce[1] = 1;
		break;
	case 'd':       // 'D' key - apply force y-axis
		addforce[0] = 1;
		break;
	case 's':       // 'S' key - apply force z-axis
		addforce[2] = 1;
		break;
	case 'x':       // 'X' key - add source at centre
		addsource = 1;
		break;
	case 'c':       // 'C' key - clear simulation
		sim_reset();
		break;
	case 'v':       // 'V' key show velocity
		dvel = !dvel;  // toggle show velocity
		break;
	case 'a':       // 'A' Key draw axis
		daxis = !daxis;  // toggle draw axis
		break;
	case 'h':       // 'H' key - get help*/
		dhelp = !dhelp;  // toggle show help
		break;
	}
}

static void mouse_func(int button, int state, int x, int y)
{
	omx = mx = x;
	omx = my = y;

	mouse_down[button] = state == GLUT_DOWN;
}

static void motion_func(int x, int y)
{
	omx = mx;
	omy = my;
	mx = x;
	my = y;
}

static void idle_func(void) {

	// ZOOM state = PAN + ROTATE
	int state = 0;

	if (mouse_down[0]) {
		state |= PAN;
	}

	if (mouse_down[2]) {
		state |= ROTATE;
	}

	update(state, omx, omy, mx, my);

	sim_main();

	glutPostRedisplay();

}


static void open_glut_window(void)
{
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);

	glutInitWindowPosition(0, 0);
	glutInitWindowSize(win_x, win_y);
	win_id = glutCreateWindow("3D Fluid Simulation");

	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	glClear(GL_COLOR_BUFFER_BIT);
	glutSwapBuffers();
	glClear(GL_COLOR_BUFFER_BIT);
	glutSwapBuffers();

	glutKeyboardFunc(key_func);
	glutMouseFunc(mouse_func);
	glutMotionFunc(motion_func);
	glutReshapeFunc(reshape_func);
	glutIdleFunc(idle_func);
	glutDisplayFunc(display);
}


int main(int argc, char** argv)
{

	glutInit(&argc, argv);
	open_glut_window();
	init();
	glutMainLoop();
	shutdown();

	return 0;
}
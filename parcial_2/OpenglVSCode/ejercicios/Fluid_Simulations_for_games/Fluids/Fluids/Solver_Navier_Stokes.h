#pragma once

#define IX(i,j,k) ((i)+(N+2)*(j) + (N+2)*(N+2)*(k))
#define SWAP(x0,x) {float * tmp=x0;x0=x;x=tmp;}
//#define MAX(a,b)            (((a) > (b)) ? (a) : (b))
//#define LINEARSOLVERTIMES 10
#define ITER 10
#define WINDOW_TITLE "Fluid"
#define WINDOW_WIDTH 768
#define WINDOW_HEIGHT 768
#define SIZE 42 // Best not to raise this very high

void add_source(int N, float* x, float* s, float dt)
{
	int i, size = (N + 2) * (N + 2) * (N + 2);
	for (i = 0; i < size; i++) x[i] += dt * s[i];
}

void  set_bnd(int N, int b, float* x)
{

	// bounds are cells at faces of the cube

	int i, j;

	//setting faces
	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			x[IX(i, j, 0)] = b == 3 ? -x[IX(i, j, 1)] : x[IX(i, j, 1)];
			x[IX(i, j, N + 1)] = b == 3 ? -x[IX(i, j, N)] : x[IX(i, j, N)];
		}
	}

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			x[IX(0, i, j)] = b == 1 ? -x[IX(1, i, j)] : x[IX(1, i, j)];
			x[IX(N + 1, i, j)] = b == 1 ? -x[IX(N, i, j)] : x[IX(N, i, j)];
		}
	}

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			x[IX(i, 0, j)] = b == 2 ? -x[IX(i, 1, j)] : x[IX(i, 1, j)];
			x[IX(i, N + 1, j)] = b == 2 ? -x[IX(i, N, j)] : x[IX(i, N, j)];
		}
	}

	//Setting edges
	for (i = 1; i <= N; i++) {
		x[IX(i, 0, 0)] = 1.0 / 2.0 * (x[IX(i, 1, 0)] + x[IX(i, 0, 1)]);
		x[IX(i, N + 1, 0)] = 1.0 / 2.0 * (x[IX(i, N, 0)] + x[IX(i, N + 1, 1)]);
		x[IX(i, 0, N + 1)] = 1.0 / 2.0 * (x[IX(i, 0, N)] + x[IX(i, 1, N + 1)]);
		x[IX(i, N + 1, N + 1)] = 1.0 / 2.0 * (x[IX(i, N, N + 1)] + x[IX(i, N + 1, N)]);
	}

	for (i = 1; i <= N; i++) {
		x[IX(0, i, 0)] = 1.0 / 2.0 * (x[IX(1, i, 0)] + x[IX(0, i, 1)]);
		x[IX(N + 1, i, 0)] = 1.0 / 2.0 * (x[IX(N, i, 0)] + x[IX(N + 1, i, 1)]);
		x[IX(0, i, N + 1)] = 1.0 / 2.0 * (x[IX(0, i, N)] + x[IX(1, i, N + 1)]);
		x[IX(N + 1, i, N + 1)] = 1.0 / 2.0 * (x[IX(N, i, N + 1)] + x[IX(N + 1, i, N)]);
	}

	for (i = 1; i <= N; i++) {
		x[IX(0, 0, i)] = 1.0 / 2.0 * (x[IX(0, 1, i)] + x[IX(1, 0, i)]);
		x[IX(0, N + 1, i)] = 1.0 / 2.0 * (x[IX(0, N, i)] + x[IX(1, N + 1, i)]);
		x[IX(N + 1, 0, i)] = 1.0 / 2.0 * (x[IX(N, 0, i)] + x[IX(N + 1, 1, i)]);
		x[IX(N + 1, N + 1, i)] = 1.0 / 2.0 * (x[IX(N + 1, N, i)] + x[IX(N, N + 1, i)]);
	}

	//setting corners
	x[IX(0, 0, 0)] = 1.0 / 3.0 * (x[IX(1, 0, 0)] + x[IX(0, 1, 0)] + x[IX(0, 0, 1)]);
	x[IX(0, N + 1, 0)] = 1.0 / 3.0 * (x[IX(1, N + 1, 0)] + x[IX(0, N, 0)] + x[IX(0, N + 1, 1)]);

	x[IX(N + 1, 0, 0)] = 1.0 / 3.0 * (x[IX(N, 0, 0)] + x[IX(N + 1, 1, 0)] + x[IX(N + 1, 0, 1)]);
	x[IX(N + 1, N + 1, 0)] = 1.0 / 3.0 * (x[IX(N, N + 1, 0)] + x[IX(N + 1, N, 0)] + x[IX(N + 1, N + 1, 1)]);

	x[IX(0, 0, N + 1)] = 1.0 / 3.0 * (x[IX(1, 0, N + 1)] + x[IX(0, 1, N + 1)] + x[IX(0, 0, N)]);
	x[IX(0, N + 1, N + 1)] = 1.0 / 3.0 * (x[IX(1, N + 1, N + 1)] + x[IX(0, N, N + 1)] + x[IX(0, N + 1, N)]);

	x[IX(N + 1, 0, N + 1)] = 1.0 / 3.0 * (x[IX(N, 0, N + 1)] + x[IX(N + 1, 1, N + 1)] + x[IX(N + 1, 0, N)]);
	x[IX(N + 1, N + 1, N + 1)] = 1.0 / 3.0 * (x[IX(N, N + 1, N + 1)] + x[IX(N + 1, N, N + 1)] + x[IX(N + 1, N + 1, N)]);
}

void lin_solve(int N, int b, float* x, float* x0, float a, float c)
{
	int i, j, k, l;

	// iterate the solver
	for (l = 0; l < ITER; l++) {
		// update for each cell
		for (i = 1; i <= N; i++) {
			for (j = 1; j <= N; j++) {
				for (k = 1; k <= N; k++) {
					x[IX(i, j, k)] = (x0[IX(i, j, k)] + a * (x[IX(i - 1, j, k)] + x[IX(i + 1, j, k)] + x[IX(i, j - 1, k)] + x[IX(i, j + 1, k)] + x[IX(i, j, k - 1)] + x[IX(i, j, k + 1)])) / c;
				}
			}
		}
		set_bnd(N, b, x);
	}
}

void diffuse(int N, int b, float* x, float* x0, float diff, float dt)
{
	//int max = N
	float a = dt * diff * N * N * N;
	lin_solve(N, b, x, x0, a, 1 + 6 * a);
}

void advect(int N, int b, float* d, float* d0, float* u, float* v, float* w, float dt)
{
	int i, j, k, i0, j0, k0, i1, j1, k1;
	float x, y, z, s0, t0, s1, t1, u1, u0, dtx, dty, dtz;

	dtx = dty = dtz = dt * N;

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			for (k = 1; k <= N; k++) {
				x = i - dtx * u[IX(i, j, k)]; y = j - dty * v[IX(i, j, k)]; z = k - dtz * w[IX(i, j, k)];
				if (x < 0.5f) x = 0.5f; if (x > N + 0.5f) x = N + 0.5f; i0 = (int)x; i1 = i0 + 1;
				if (y < 0.5f) y = 0.5f; if (y > N + 0.5f) y = N + 0.5f; j0 = (int)y; j1 = j0 + 1;
				if (z < 0.5f) z = 0.5f; if (z > N + 0.5f) z = N + 0.5f; k0 = (int)z; k1 = k0 + 1;

				s1 = x - i0; s0 = 1 - s1; t1 = y - j0; t0 = 1 - t1; u1 = z - k0; u0 = 1 - u1;
				d[IX(i, j, k)] = s0 * (t0 * u0 * d0[IX(i0, j0, k0)] + t1 * u0 * d0[IX(i0, j1, k0)] + t0 * u1 * d0[IX(i0, j0, k1)] + t1 * u1 * d0[IX(i0, j1, k1)]) +
					s1 * (t0 * u0 * d0[IX(i1, j0, k0)] + t1 * u0 * d0[IX(i1, j1, k0)] + t0 * u1 * d0[IX(i1, j0, k1)] + t1 * u1 * d0[IX(i1, j1, k1)]);
			}
		}
	}

	set_bnd(N, b, d);
}

void project(int N, float* u, float* v, float* w, float* p, float* div)
{
	int i, j, k;

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			for (k = 1; k <= N; k++) {
				div[IX(i, j, k)] = -1.0 / 3.0 * ((u[IX(i + 1, j, k)] - u[IX(i - 1, j, k)]) / N + (v[IX(i, j + 1, k)] - v[IX(i, j - 1, k)]) / N + (w[IX(i, j, k + 1)] - w[IX(i, j, k - 1)]) / N);
				p[IX(i, j, k)] = 0;
			}
		}
	}

	set_bnd(N, 0, div); set_bnd(N, 0, p);

	lin_solve(N, 0, p, div, 1, 6);

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			for (k = 1; k <= N; k++) {
				u[IX(i, j, k)] -= 0.5f * N * (p[IX(i + 1, j, k)] - p[IX(i - 1, j, k)]);
				v[IX(i, j, k)] -= 0.5f * N * (p[IX(i, j + 1, k)] - p[IX(i, j - 1, k)]);
				w[IX(i, j, k)] -= 0.5f * N * (p[IX(i, j, k + 1)] - p[IX(i, j, k - 1)]);
			}
		}
	}

	set_bnd(N, 1, u); set_bnd(N, 2, v); set_bnd(N, 3, w);
}

void dens_step(int N, float* x, float* x0, float* u, float* v, float* w, float diff, float dt)
{
	add_source(N, x, x0, dt);
	SWAP(x0, x); diffuse(N, 0, x, x0, diff, dt);
	SWAP(x0, x); advect(N, 0, x, x0, u, v, w, dt);
}

void vel_step(int N, float* u, float* v, float* w, float* u0, float* v0, float* w0, float visc, float dt)
{
	add_source(N, u, u0, dt); add_source(N, v, v0, dt); add_source(N, w, w0, dt);
	SWAP(u0, u); diffuse(N, 1, u, u0, visc, dt);
	SWAP(v0, v); diffuse(N, 2, v, v0, visc, dt);
	SWAP(w0, w); diffuse(N, 3, w, w0, visc, dt);
	project(N, u, v, w, u0, v0);
	SWAP(u0, u); SWAP(v0, v); SWAP(w0, w);
	advect(N, 1, u, u0, u0, v0, w0, dt); advect(N, 2, v, v0, u0, v0, w0, dt); advect(N, 3, w, w0, u0, v0, w0, dt);
	project(N, u, v, w, u0, v0);
}

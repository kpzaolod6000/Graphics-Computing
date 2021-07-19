#pragma once

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>
#include <iostream>

using namespace std;

int main() {
	/*glm::mat4 vertices_1 = glm::mat4(1.0, 1.0, -1.0, -1.0,
		1.0, -1.0, 1.0, -1.0,
		1.0, 1.0, 1.0, 1.0,
		1.0, 1.0, 1.0, 1.0);*/
		/*Vertices*/
	float vertex[16] = { -1.0, 1.0, -1.0, 1.0 ,
							 2.0, 2.0, 0.0, 0.0,
							-5.0, -5.0, -5.0, -5.0,
							 1.0, 1.0, 1.0, 1.0 };

	/*TRANSFORMACION DE VIEWPORT*/

	float nx = 100.00;
	float ny = 50.00;
	float Mvp[16] = { nx / 2, 0.0, 0.0, (nx - 1) / 2 ,
						0.0, ny / 2, 0.0, (ny - 1) / 2 ,
						0.0, 0.0, 1.0, 0.0,
						0.0, 0.0, 0.0, 1.0 };

	for (size_t i = 0; i < 16; i++)
	{
		if (i % 4 == 0) cout << endl;
		cout << Mvp[i] << " ";

	}
	cout << endl;
	/*TRANSFORMACION DE PROJECTION ORTHOGRAFICA*/
	float l = -2.0;
	float b = 0.0;
	float n = -3.0;
	float r = 2.0;
	float t = 2.0;
	float f = -6.0;

	float Morth[16] = { 2 / (r - l), 0.0, 0.0, -((r + l) / (r - l)),
		0.0, 2 / (t - b), 0.0, -((t + b) / (t - b)),
		0.0, 0.0, 2 / (n - f), -((n + f) / (n - f)),
		0.0, 0.0, 0.0, 1.0 };

	for (size_t i = 0; i < 16; i++)
	{
		if (i % 4 == 0) cout << endl;
		cout << Morth[i] << " ";

	}
	cout << endl;
	/*OPERACIONES */
	glm::mat4 mat4_Vertex = glm::transpose(glm::make_mat4(vertex));
	cout << glm::to_string(mat4_Vertex) << endl;
	glm::mat4 mat4_Mvp = glm::transpose(glm::make_mat4(Mvp));
	cout << glm::to_string(mat4_Mvp) << endl;
	glm::mat4 mat4_Morth = glm::transpose(glm::make_mat4(Morth));
	cout << glm::to_string(mat4_Morth) << endl;
	glm::mat4 M = mat4_Mvp * mat4_Morth;
	cout << glm::to_string(mat4_Vertex * M) << endl;

	/*cout << glm::to_string(Mvp) << endl;
	glm::mat4 Morth = buildTrasformationOrtographics(l, b, n, r, t, f);

	cout << glm::to_string(Morth) << endl;

	glm::mat4 M = Morth * Mvp;

	cout << "Matriz M: " << glm::to_string(M) << endl;
	cout << "Posicion de los pixeles en la pantalla : " << glm::to_string(vertices_2 * M) << endl;*/


	return 0;
}
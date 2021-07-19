#pragma once
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>
#include <iostream>

using namespace std;

glm::mat4 buildViewPort(float nx, float ny) {
	glm::mat4 Mvp = glm::mat4(nx / 2, 0.0, 0.0, (nx - 1) / 2,
		0.0, ny / 2, 0.0, (ny - 1) / 2,
		0.0, 0.0, 1.0, 0.0,
		0.0, 0.0, 0.0, 1.0
	);
	return Mvp;
}

glm::mat4 buildTrasformationOrtographics(float l, float b, float n, float r, float t, float f) {
	glm::mat4 Morth = glm::mat4(2 / (r - l), 0.0, 0.0, -((r + l) / (r - l)),
		0.0, 2 / (t - b), 0.0, -((t + b) / (t - b)),
		0.0, 0.0, 2 / (n - f), -((n + f) / (n - f)),
		0.0, 0.0, 0.0, 1.0
	);
	return Morth;
}

glm::mat4 buildTrasformationCamera(glm::vec3 u, glm::vec3 v, glm::vec3 w, glm::vec3 e) {
	glm::mat4 xyz_coordinates = glm::mat4(
		u.x, u.y, u.z, 0,
		v.x, v.y, v.z, 0,
		w.x, w.y, w.z, 0,
		0.0, 0.0, 0.0, 1.0
	);

	glm::mat4 eye_coordinates = glm::mat4(
		1.0, 0.0, 0.0, -e.x,
		0.0, 1.0, 0.0, -e.y,
		0.0, 0.0, 1.0, -e.z,
		0.0, 0.0, 0.0, 1.0
	);
	return eye_coordinates * xyz_coordinates;
}


glm::mat4 buildTrasformationPerspective(float n, float f) {
	glm::mat4 P = glm::mat4(n, 0.0, 0.0, 0.0,
		0.0, n, 0.0, 0.0,
		0.0, 0.0, n + f, -(f * n),
		0.0, 0.0, 1.0, 0.0
	);
	return P;
}

int main() {
	glm::mat4 vertices_1 = glm::mat4(1.0, 1.0, -1.0, -1.0,
		1.0, -1.0, 1.0, -1.0,
		1.0, 1.0, 1.0, 1.0,
		1.0, 1.0, 1.0, 1.0);

	glm::mat4 vertices_2 = glm::mat4(-1.0, 1.0, -1.0, 1.0,
		2.0, 2.0, 0.0, 0.0,
		-5.0, -5.0, -5.0, -5.0,
		1.0, 1.0, 1.0, 1.0);


	float viewX = 100.00;
	float viewY = 50.00;
	float l = -2.0;
	float b = 0.0;
	float n = -3.0;
	float r = 2.0;
	float t = 2.0;
	float f = -6.0;

	/*TRANSFORMACION DE VIEWPORT*/
	glm::mat4 Mvp = buildViewPort(viewX, viewY);
	cout << "Matriz Mvp: " << endl << glm::to_string(Mvp) << endl;

	/*TRANSFORMACION DE PROJECTION ORTHOGRAFICA*/
	glm::mat4 Morth = buildTrasformationOrtographics(l, b, n, r, t, f);
	cout << "Matriz Morth: " << endl << glm::to_string(Morth) << endl;


	/*MATRIZ RESULTANTE M*/
	glm::mat4 M = Morth * Mvp;
	cout << endl << "Matriz M: " << endl << glm::to_string(M) << endl;
	/*RESULTADO*/
	glm::mat4 result = vertices_2 * M;
	cout << "Posicion de los pixeles en la pantalla : " << glm::to_string(result) << endl;
	cout << endl;
	for (size_t i = 0; i < 4; i++)
	{
		for (size_t j = 0; j < 4; j++)
		{
			cout << result[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	/*TRANSFORMACION DE LA CAMARA*/
	/*Posiciones de la camara*/
	/*ojo*/
	glm::vec3 e1 = glm::vec3(0.0, 2.0, 0.0);
	/*vector de mirada*/
	glm::vec3 g1 = glm::vec3(0.0, -2.0, -5.0);
	/*vector de vista superior*/
	glm::vec3 t1 = glm::vec3(0.0, 1.0, 0.0);

	/*vectores unitarios*/
	glm::vec3 w1 = -(glm::normalize(g1));
	glm::vec3 u1 = glm::normalize(glm::cross(t1, w1));
	glm::vec3 v1 = glm::cross(w1, u1);


	//cout << e1.x << e1.y << e1.z << endl;
	cout << glm::to_string(w1) << endl;
	cout << glm::to_string(u1) << endl;
	cout << glm::to_string(v1) << endl;

	/*MATRIZ DE Mcam*/

	glm::mat4 Mcam = buildTrasformationCamera(u1, v1, w1, e1);
	cout << endl << "Matriz Mcam :" << endl << glm::to_string(Mcam) << endl;

	/*TRASFORMACION DEL VERTICE*/
	glm::mat4 M1 = Mcam * Morth * Mvp;

	/*RESULTADO*/
	glm::mat4 result1 = vertices_2 * M1;
	cout << "Posicion de los pixeles en la pantalla con camara : " << endl << glm::to_string(result1) << endl;
	cout << endl;

	/*TRANSFORMACION DE PROJECTION DE PERSPECTIVA*/
	glm::mat4 P = buildTrasformationPerspective(n, f);
	cout << "Matriz P: " << endl << glm::to_string(P) << endl;
	glm::mat4 Mper = P * Morth;
	cout << "Matriz Mper: " << endl << glm::to_string(Mper) << endl;

	/*TRASFORMACION DEL VERTICE*/
	glm::mat4 M2 = Mcam * Mper * Mvp;
	/*RESULTADO*/
	glm::mat4 result2 = vertices_2 * M2;
	cout << "Posicion de los pixeles en la pantalla con camara perspectiva: " << endl << glm::to_string(result2) << endl;
	cout << endl;

	/*CONVITIENDO A COORDENADAS CARTESIANAS*/
	cout << "Resultado Cartesiano: " << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{
			float w_p = result2[3][j];
			cout << result2[i][j] / w_p << " ";
		}
		cout << endl;
	}

	//glm::vec4 vec(1.0f, 0.0f, 0.0f, 1.0f);
	//glm::mat4 trans = glm::mat4(1.0f);
	//trans = glm::translate(trans, glm::vec3(1.0f, 1.0f, 0.0f));
	//vec = trans * vec;
	//cout << vec.x << vec.y << vec.z <<endl;
	return 0;
}


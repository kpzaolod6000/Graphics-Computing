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

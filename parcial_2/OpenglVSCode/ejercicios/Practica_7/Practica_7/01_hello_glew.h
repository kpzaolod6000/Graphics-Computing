#pragma once
#include <GL/glew.h>
//#include <glad/glad.h>
#include <glfw/glfw3.h>

#include <iostream>

using namespace std;
void init(GLFWwindow* window) { }

void display(GLFWwindow* window, double currentTime) {
	glClearColor(0.0, 1.0, 0.0, 1.0); //color el utlimo valor es la opacidad
	glClear(GL_COLOR_BUFFER_BIT);// con esto llenamos el buffer del color con ese color
}
#pragma once

#include "Utils.h"
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

void setupVertices(void) { // 36 vértices, 12 triángulos, hace un cubo de 2x2x2 colocado en el origen 
	float vertexPositions[108] = {
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
	};
	//Los dos comandos OpenGL glGenVertexArrays() y glGenBuffers() crean
	//VAO y VBO respectivamente, y devuelven ID enteros para ellos.Almacenamos esos
	//ID en las matrices de enteros vao y vbo.Los dos parámetros de cada uno de ellos se refieren
	//a cuántos ID se crean y una matriz para contener los ID devueltos.El propósito
	//de glBindVertexArrays() es hacer que el VAO especificado esté "activo" para que los buferes
	//generados se asociarán con ese VAO.
	glGenVertexArrays(1, vao);
	glBindVertexArray(vao[0]);
	glGenBuffers(numVBOs, vbo);

	//Los vertices estan codificados en un arreglo en la aplicación C ++ / OpenGL. En eso
	//caso, necesitamos copiar esos valores en uno de nuestros dos búferes que previamente
	//generamos .Para hacer eso, necesitamos(a) hacer que ese búfer(digamos, el búfer 0) esté "activo"
	//con el comando glBindBuffer() de OpenGL y(b) use el comando glBufferData()
	//para copiar la matriz que contiene los vértices en el búfer activo(el 0º VBO en este
	//caso).Suponiendo que los vértices se almacenan en una matriz flotante denominada vPositions,
	//el siguiente código C++ copiaría esos valores en el 0º VBO :

	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertexPositions), vertexPositions, GL_STATIC_DRAW);

}

void init(GLFWwindow* window) {
	const char* vertShader = "cube_shader/vertShader.glsl";
	const char* fragShader = "cube_shader/fragShader.glsl";

	renderingProgram = Utils::createShaderProgram(vertShader, fragShader);
	cameraX = 0.0f; cameraY = 0.0f; cameraZ = 8.0f;
	cubeLocX = 0.0f; cubeLocY = -2.0f; cubeLocZ = 0.0f;  //desplaza hacia abajo Y para revelar la perspectiva
	setupVertices();
}

void display(GLFWwindow* window, double currentTime) {
	glClear(GL_DEPTH_BUFFER_BIT);//es necesario borrar el búfer de profundidad antes de renderizar un marco para que la eliminación de la superficie oculta se produzca correctamente
	glUseProgram(renderingProgram);//instalando el código GLSL en la GPU. 
	//Recuerde que esto no ejecuta el programa de sombreado, pero habilita las siguientes llamadas OpenGL para determinar el atributo de vértice del sombreador y las ubicaciones uniformes. 

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

	// asociar VBO con el atributo de vértice correspondiente en el sombreador de vértices 
	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(0);
	//Observe también en el sombreador de vértices la presencia del calificador de diseño en la posición 
	//del atributo de vértice entrante. Dado que la ubicación se especifica como "0", la función display () 
	//puede hacer referencia a esta variable simplemente usando 0 en el primer parámetro de la llamada 
	//a la función glVertexAttribPointer () y en la llamada a la función glEnableVertexAttribArray ().

	// ajustar la configuración de OpenGL y dibujar el modelo 
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glDrawArrays(GL_TRIANGLES, 0, 36);
}

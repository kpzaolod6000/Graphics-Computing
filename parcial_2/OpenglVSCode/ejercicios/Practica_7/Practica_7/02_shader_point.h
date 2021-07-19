#pragma once
#include <GL/glew.h>
//#include <glad/glad.h>
#include <glfw/glfw3.h>

#include <iostream>

using namespace std;


#define numVAOs 1
GLuint renderingProgram; // "Unsigned int" proporcionado por OpenGL (
GLuint vao[numVAOs];

GLuint createShaderProgram() {
	const char* vshaderSource =
		"#version 430 \n" // version 4.3 glsl es parecido a c++
		"void main(void) \n"
		"{ gl_Position = vec4(0.0, 0.0, 0.0, 1.0); }"; // posicion de las coordenadas del vertice en el espacio 3D , origen (0,0,0)
// creamos un vertice, no especificamos salida, porque gl_position es por defecto de salida
	const char* fshaderSource =
		"#version 430 \n"
		"out vec4 color; \n"// out indica que el variable color es una salida
		"void main(void) \n"
		"{ color = vec4(0.0, 0.0, 1.0, 1.0); }";
	//El prop�sito de cualquier shader de fragmentos es establecer el color RGB de un p�xel que se mostrar�. 
//No fue necesario especificar una etiqueta "out" para gl_Position en el shader 
//de v�rtices, porque gl_Position es una variable de salida predefinida).

//en el etapss entre vertex y fragment, el vertice se convierte en un pixel
//especificamos el color de los pixeles

	GLuint vShader = glCreateShader(GL_VERTEX_SHADER); //generando shader for vertex  vacios
	GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);//generando shader for fragment vacios
	 // y devuelve un ID de n�mero entero para cada uno de los que es un �ndice para referenciarlo m�s tarde, 
	 // nuestro c�digo almacena este ID en las variables vShader y fShader

	glShaderSource(vShader, 1, &vshaderSource, NULL);
	glShaderSource(fShader, 1, &fshaderSource, NULL);
	//Luego llama a glShaderSource (), que carga el c�digo GLSL de las cadenas en los objetos de sombreado vac�os.
	//Las dos llamadas especifican el n�mero de l�neas de c�digo en cada sombreador como "1";
	glCompileShader(vShader);
	glCompileShader(fShader);
	//compiladores 
	GLuint vfProgram = glCreateProgram();
	//Crea un objeto de programa llamado vfProgram y guarda el ID entero que apunta a �l.
	//Un objeto de "programa" OpenGL contiene una serie de sombreadores(shaders) compilados, 
	//y aqu� vemos los siguientes comandos: glCreateProgram () para crear el objeto de programa, 
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
	//carga el programa que contiene los dos sombreadores compilados en las etapas de la canalizaci�n de OpenGL (�en la GPU!).
	//no ejecuta los sombreadores, solo los carga en el hardware.
	glPointSize(30.0f); // un vertice es un pixel, con esto especificamos el tama�o del pixel
	glDrawArrays(GL_POINTS, 0, 1);
	// La aplicaci�n C ++ / OpenGL tambi�n es responsable de decirle a OpenGL que construya primitivas. 
	//El tipo primitivo es GL_POINTS
	//Hacemos esto usando la siguiente funci�n OpenGL: glDrawArrays(GLenum mode, Glint first, GLsizei count);
	//Cuando se llama a glDrawArrays (), el c�digo GLSL en la canalizaci�n comienza a ejecutarse.
	//glDrawArrays(GLenum mode, Glint first, GLsizei count);  GLenum mode= El modo es el tipo de primitiva
	//El modo es el tipo de primitiva; para los tri�ngulos usamos GL_TRIANGLES. 
	//El par�metro "primero" (Glint first) indica con qu� v�rtice comenzar (generalmente el v�rtice n�mero 0, el primero), 
	//y count (GLsizei count) especifica el n�mero total de v�rtices que se dibujar�n.
}

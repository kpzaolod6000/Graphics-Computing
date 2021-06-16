//#include <GL/glew.h>
#include <glad/glad.h>
#include <glfw/glfw3.h>

#include <iostream>

using namespace std;
void init(GLFWwindow* window) { }

void display(GLFWwindow* window, double currentTime) {
	glClearColor(0.0, 1.0, 0.0, 1.0); //color el utlimo valor es la opacidad
	glClear(GL_COLOR_BUFFER_BIT);// con esto llenamos el buffer del color con ese color
}

int main(void) {
	if (!glfwInit()) { exit(EXIT_FAILURE); }//inicializa library glfw
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);

	GLFWwindow* window = glfwCreateWindow(600, 600, "Chapter2 - program1", NULL, NULL);
	glfwMakeContextCurrent(window); // / ? 

	//if (glewInit() != GLEW_OK) { exit(EXIT_FAILURE); } //inicializa glew
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)){ exit(EXIT_FAILURE); }

	glfwSwapInterval(1);
	init(window);
	while (!glfwWindowShouldClose(window)) {
			display(window, glfwGetTime()); //glfwGetTime() devuelve el tiempo transcurrido desde que se inicializó GLFW.
			glfwSwapBuffers(window); // pinta la pantalla
			glfwPollEvents();//eventos relacionados con la ventana (ejemplo presionar una tecla)
	}

	glfwDestroyWindow(window);
	glfwTerminate();
	exit(EXIT_SUCCESS);

}


//primitivas : punto, linea , triangulo 

//Los vértices pueden provenir de una variedad de fuentes: pueden leerse de archivos 
//y luego cargarse en búferes por la aplicación 
//C ++ / OpenGL, o pueden estar codificados en el código
//C ++ o incluso en el código GLSL.
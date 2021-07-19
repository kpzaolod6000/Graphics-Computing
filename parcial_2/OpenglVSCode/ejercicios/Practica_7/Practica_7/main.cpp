//#include <GL/glew.h>
//#include"01_hello_glew.h"
//#include"02_shader_point.h"
//#include "03_glsl_error.h"
//#include "04_llamadas_file_glsl.h"
//#include "05_triangulo.h"
//#include "06_move_triangulo.h"
//#include "2_01_escalar_pixel.h"
//#include "2_02_triangulo_isosceles.h"
#include "01_proyectando.h"

int main(void) {
	if (!glfwInit()) { exit(EXIT_FAILURE); }//inicializa library glfw
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);

	GLFWwindow* window = glfwCreateWindow(1500, 1500, "Chapter2 - program1", NULL, NULL);
	glfwMakeContextCurrent(window); // / ? 

	if (glewInit() != GLEW_OK) { exit(EXIT_FAILURE); } //inicializa glew
	//if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) { exit(EXIT_FAILURE); }

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
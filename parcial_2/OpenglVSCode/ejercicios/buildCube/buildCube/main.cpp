//#include"Program4_1_Plai_Red_Cube.h"
#include"Program4_1_1_Plai_Colors_Cube.h"
//#include "Rotate_Traslation_Cube.h"
//#include "Render_multiple_objects.h"
//#include "Program4_2_instanciando.h"
//#include "Program4_3_Cube_and_Pyramid.h"
//#include "Simple_Solar_System.h"
//#include "Simple_Solar_System_2.h"

int main(void) { // main() is unchanged from before
	if (!glfwInit()) { exit(EXIT_FAILURE); }
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	GLFWwindow* window = glfwCreateWindow(600, 600, "Chapter 4 - program 1 CUBO", NULL, NULL);
	glfwMakeContextCurrent(window);
	if (glewInit() != GLEW_OK) { exit(EXIT_FAILURE); }
	glfwSwapInterval(1);
	init(window);
	while (!glfwWindowShouldClose(window)) {
		display(window, glfwGetTime());
		glfwSwapBuffers(window);
		glfwPollEvents();
	}
	glfwDestroyWindow(window);
	glfwTerminate();
	exit(EXIT_SUCCESS);
}
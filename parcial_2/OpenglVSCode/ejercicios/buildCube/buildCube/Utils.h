#pragma once
#include <GL\glew.h>
#include <GLFW\glfw3.h>
#include <string>
#include <iostream>
#include <fstream>
#include <cmath>
#include <glm\glm.hpp>
#include <glm\gtc\type_ptr.hpp>
#include <glm\gtc\matrix_transform.hpp>
using namespace std;

class Utils {
public:
	Utils(){}
	//leendo archivos glsl
	static string readShaderSource(const char* filePath) {
		string content;

		ifstream fileStream(filePath, ios::in);
		string line = "";
		while (!fileStream.eof()) {
			getline(fileStream, line);
			content.append(line + "\n");
		}

		fileStream.close();
		return content;
	}

	// functions to catch errors in GLSL
	static void printShaderLog(GLuint shader) {
		int len = 0;
		int chWrittn = 0;
		char* log;
		glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &len);
		if (len > 0) {
			log = (char*)malloc(len);
			glGetShaderInfoLog(shader, len, &chWrittn, log);
			cout << "Shader Info Log: " << log << endl;
			free(log);
		}
	}
	static void printProgramLog(int prog) {
		int len = 0;
		int chWrittn = 0;
		char* log;
		glGetProgramiv(prog, GL_INFO_LOG_LENGTH, &len);
		if (len > 0) {
			log = (char*)malloc(len);
			glGetProgramInfoLog(prog, len, &chWrittn, log);
			cout << "Program Info Log: " << log << endl;
			free(log);
		}
	}
	static bool checkOpenGLError() {
		bool foundError = false;
		int glErr = glGetError();
		while (glErr != GL_NO_ERROR) {
			cout << "glError: " << glErr << endl;
			foundError = true;
			glErr = glGetError();
		}
		return foundError;
	}

	static GLuint createShaderProgram(const char* vertShader, const char* fragShader) {
		GLint vertCompiled;
		GLint fragCompiled;
		GLint linked;

		string vertShaderStr = readShaderSource(vertShader);
		string fragShaderStr = readShaderSource(fragShader);
		GLuint vShader = glCreateShader(GL_VERTEX_SHADER); //generando shader for vertex  vacios
		GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);//generando shader for fragment vacios

		const char* vertShaderSrc = vertShaderStr.c_str();
		const char* fragShaderSrc = fragShaderStr.c_str();

		glShaderSource(vShader, 1, &vertShaderSrc, NULL);
		glShaderSource(fShader, 1, &fragShaderSrc, NULL);

		glCompileShader(vShader);
		checkOpenGLError();
		glGetShaderiv(vShader, GL_COMPILE_STATUS, &vertCompiled);
		if (vertCompiled != 1) {
			cout << "vertex compilation failed" << endl;
			printShaderLog(vShader);
		}
		glCompileShader(fShader);
		checkOpenGLError();
		glGetShaderiv(fShader, GL_COMPILE_STATUS, &fragCompiled);
		if (fragCompiled != 1) {
			cout << "fragment compilation failed" << endl;
			printShaderLog(fShader);
		}
		//compiladores 
		GLuint vfProgram = glCreateProgram();

		glAttachShader(vfProgram, vShader);
		glAttachShader(vfProgram, fShader);
		glLinkProgram(vfProgram);
		checkOpenGLError();
		glGetProgramiv(vfProgram, GL_LINK_STATUS, &linked);
		if (linked != 1) {
			cout << "linking failed" << endl;
			printProgramLog(vfProgram);
		}
		return vfProgram;
	}
};


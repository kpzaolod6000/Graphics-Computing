# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build

# Include any dependencies generated for this target.
include CMakeFiles/triangulo_isosceles.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/triangulo_isosceles.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/triangulo_isosceles.dir/flags.make

CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.o: CMakeFiles/triangulo_isosceles.dir/flags.make
CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.o: ../dep/include/glad/glad/glad.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.o   -c /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/dep/include/glad/glad/glad.c

CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/dep/include/glad/glad/glad.c > CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.i

CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/dep/include/glad/glad/glad.c -o CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.s

CMakeFiles/triangulo_isosceles.dir/main.cpp.o: CMakeFiles/triangulo_isosceles.dir/flags.make
CMakeFiles/triangulo_isosceles.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/triangulo_isosceles.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/triangulo_isosceles.dir/main.cpp.o -c /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/main.cpp

CMakeFiles/triangulo_isosceles.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/triangulo_isosceles.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/main.cpp > CMakeFiles/triangulo_isosceles.dir/main.cpp.i

CMakeFiles/triangulo_isosceles.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/triangulo_isosceles.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/main.cpp -o CMakeFiles/triangulo_isosceles.dir/main.cpp.s

# Object files for target triangulo_isosceles
triangulo_isosceles_OBJECTS = \
"CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.o" \
"CMakeFiles/triangulo_isosceles.dir/main.cpp.o"

# External object files for target triangulo_isosceles
triangulo_isosceles_EXTERNAL_OBJECTS =

triangulo_isosceles: CMakeFiles/triangulo_isosceles.dir/dep/include/glad/glad/glad.c.o
triangulo_isosceles: CMakeFiles/triangulo_isosceles.dir/main.cpp.o
triangulo_isosceles: CMakeFiles/triangulo_isosceles.dir/build.make
triangulo_isosceles: /usr/lib/x86_64-linux-gnu/libGL.so
triangulo_isosceles: /usr/lib/x86_64-linux-gnu/libGLU.so
triangulo_isosceles: CMakeFiles/triangulo_isosceles.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable triangulo_isosceles"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/triangulo_isosceles.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/triangulo_isosceles.dir/build: triangulo_isosceles

.PHONY : CMakeFiles/triangulo_isosceles.dir/build

CMakeFiles/triangulo_isosceles.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/triangulo_isosceles.dir/cmake_clean.cmake
.PHONY : CMakeFiles/triangulo_isosceles.dir/clean

CMakeFiles/triangulo_isosceles.dir/depend:
	cd /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo_isosceles/build/CMakeFiles/triangulo_isosceles.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/triangulo_isosceles.dir/depend

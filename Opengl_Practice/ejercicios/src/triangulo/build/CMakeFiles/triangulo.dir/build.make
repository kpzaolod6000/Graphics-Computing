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
CMAKE_SOURCE_DIR = /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build

# Include any dependencies generated for this target.
include CMakeFiles/triangulo.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/triangulo.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/triangulo.dir/flags.make

CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.o: CMakeFiles/triangulo.dir/flags.make
CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.o: ../dep/include/glad/glad/glad.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.o   -c /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/dep/include/glad/glad/glad.c

CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/dep/include/glad/glad/glad.c > CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.i

CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/dep/include/glad/glad/glad.c -o CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.s

CMakeFiles/triangulo.dir/main.cpp.o: CMakeFiles/triangulo.dir/flags.make
CMakeFiles/triangulo.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/triangulo.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/triangulo.dir/main.cpp.o -c /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/main.cpp

CMakeFiles/triangulo.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/triangulo.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/main.cpp > CMakeFiles/triangulo.dir/main.cpp.i

CMakeFiles/triangulo.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/triangulo.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/main.cpp -o CMakeFiles/triangulo.dir/main.cpp.s

# Object files for target triangulo
triangulo_OBJECTS = \
"CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.o" \
"CMakeFiles/triangulo.dir/main.cpp.o"

# External object files for target triangulo
triangulo_EXTERNAL_OBJECTS =

triangulo: CMakeFiles/triangulo.dir/dep/include/glad/glad/glad.c.o
triangulo: CMakeFiles/triangulo.dir/main.cpp.o
triangulo: CMakeFiles/triangulo.dir/build.make
triangulo: /usr/lib/x86_64-linux-gnu/libGL.so
triangulo: /usr/lib/x86_64-linux-gnu/libGLU.so
triangulo: CMakeFiles/triangulo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable triangulo"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/triangulo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/triangulo.dir/build: triangulo

.PHONY : CMakeFiles/triangulo.dir/build

CMakeFiles/triangulo.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/triangulo.dir/cmake_clean.cmake
.PHONY : CMakeFiles/triangulo.dir/clean

CMakeFiles/triangulo.dir/depend:
	cd /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build /home/judal/Documentos/COMPUTACION/Graphics-Computing/Opengl_Practice/ejercicios/src/triangulo/build/CMakeFiles/triangulo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/triangulo.dir/depend


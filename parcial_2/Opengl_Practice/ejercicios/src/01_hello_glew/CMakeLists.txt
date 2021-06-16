cmake_minimum_required(VERSION 3.10)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

#set( CMAKE_BUILD_TYPE Release )
set( CMAKE_BUILD_TYPE Debug )

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Debug")
  message(STATUS "\nBuild type not specified: Use Debug by default")
endif(NOT CMAKE_BUILD_TYPE)

set( DEPENDENCY_DIR 
${CMAKE_CURRENT_SOURCE_DIR}/dep)

message( "\nCurrent directory is: ${CMAKE_CURRENT_SOURCE_DIR}" )
message( "\nDependency directory is: ${DEPENDENCY_DIR}" )
message( "\nBuild mode is: ${CMAKE_BUILD_TYPE}" )

project( GLFW_Tutorials )

if ( WIN32 )
	message( "\nCONFIGURING FOR WINDOWS\n" )

else()
	message( "\nCONFIGURING FOR LINUX\n" )
	
endif()

# add_subdirectory( src )
project( 01_hello_glew )

message( "Configuring main application - ${PROJECT_NAME} : " )

# OpenGL
find_package(OpenGL REQUIRED)

message( "\n After find package OpenGL  \n" )


file(GLOB SOURCES "*.cpp" ${DEPENDENCY_DIR}/include/glad/glad/glad.c )
file(GLOB HEADERS "*.h" )
file(GLOB SHADERS "*.vert" "*.frag" "*.vs" "*.fs" )

include_directories( 
${DEPENDENCY_DIR}/include/glad/ 
${DEPENDENCY_DIR}/include/glfw/

)
message( "${DEPENDENCY_DIR}" ) #ver donde apunta esta weada
message( "\nBuild mode test is: ${CMAKE_BUILD_TYPE}" )

if ( CMAKE_BUILD_TYPE STREQUAL "Debug")
    message("\nOpenGL_GLUT_GLFW_Program -- Debug mode ****************")
	link_directories(
	${DEPENDENCY_DIR}/lib/glad/Debug/
	${DEPENDENCY_DIR}/lib/glfw/Debug/
	)
else()
    message("\nOpenGL_GLUT_GLFW_Program -- Release mode ****************")
	link_directories(
	${DEPENDENCY_DIR}/lib/glad/Release/
	${DEPENDENCY_DIR}/lib/glfw/Release/
	)
endif ()
 
add_executable( ${PROJECT_NAME}  ${HEADERS} ${SOURCES} ${SHADERS} )

if ( CMAKE_BUILD_TYPE STREQUAL "Debug")
	if ( WIN32 )
	    message("\nOpenGL_GLUT_GLFW_Program -- Debug mode Windows ****************")
		target_link_libraries( ${PROJECT_NAME} 
						   opengl32
						   glad.lib
	                       glfw3.lib
						   
						    )
	else()
		message("\nOpenGL_GLUT_GLFW_Program -- Debug mode Linux ****************")
		target_link_libraries( ${PROJECT_NAME} 
						   ${OPENGL_LIBRARY}
							-lm
							-lGL
							-lGLU
							-lX11
							-lXi
							-lXxf86vm 
							-lXrandr 
							-pthread 
							-ldl
							-lm							
						   libglad.a
	                       libglfw3.a
						    )

	endif()					    	
else()
	if ( WIN32 )
		message("\nOpenGL_GLUT_GLFW_Program -- Release mode Windows ****************")
		target_link_libraries( ${PROJECT_NAME} 
						   opengl32
						   glad.lib
	                       glfw3.lib
						    )
	else()
		message("\nOpenGL_GLUT_GLFW_Program -- Release mode Linux ****************")
		target_link_libraries( ${PROJECT_NAME} 
						  ${OPENGL_LIBRARY}
												    
							-lm
							-lGL
							-lGLU
							-lX11
							-lXi
							-lXxf86vm 
							-lXrandr 
							-pthread 
							-ldl
							-lm							
						   libglad.a
	                       libglfw3.a
							)

	endif()	
endif ()                      

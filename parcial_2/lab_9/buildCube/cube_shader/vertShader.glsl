#version 430

layout (location=0) in vec3 position;

uniform mat4 mv_matrix;
uniform mat4 proj_matrix;

void main(void)
{
    gl_Position = proj_matrix * mv_matrix * vec4(position,1.0);
    //vec4(x,y,z,1.0)
    //Esos valores se colocan en la variable de salida incorporada de OpenGL gl_Position, 
    //y luego continúan a través de la canalización y son interpolados por el rasterizador.
}
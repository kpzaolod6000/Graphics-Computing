#version 430

layout (location=0) in vec3 position;
//layout (location=1) in vec3 colorDensity;

uniform mat4 mv_matrix;
uniform mat4 proj_matrix;

out vec4 varyingColor;

void main(void)
{ 
    gl_Position = proj_matrix * mv_matrix * vec4(position,1.0);
    varyingColor = vec4(1.0, 0.0, 0.0, 1.0);
    //varyingColor = vec4(colorDensity,1.0);
}
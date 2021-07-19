#version 430

void main(void)
{
    double scale = 0.01;
    if (gl_VertexID == 0) gl_Position = vec4( 61.73 * scale, 14.04 * scale, 0.0, 1.0);
    else if (gl_VertexID == 1) gl_Position = vec4(37.26 * scale, 14.04 * scale, 0.0, 1.0);
    else if (gl_VertexID == 2) gl_Position = vec4(62.96 * scale, 42.1667 * scale, 0.0, 1.0);
    else if (gl_VertexID == 3) gl_Position = vec4(62.96 * scale, 42.1667 * scale, 0.0, 1.0);
    else if (gl_VertexID == 4) gl_Position = vec4( 37.26 * scale, 14.04 * scale, 0.0, 1.0);
    else gl_Position = vec4(36.03 * scale, 42.16 * scale, 0.0, 1.0);
}
#version 330

uniform vec4 in_color;
uniform vec3 eye;
uniform vec3 light;

in vec4 vertex;
in vec4 normal;
// in vec4 gl_FragCoord;

out vec4 out_color;

vec4 shadeDiffuse() {
  vec3 n = vec3(normalize(normal));
  vec3 out_vec = normalize(eye - vec3(vertex));
  float diffuse = abs(dot(out_vec, n));
  return vec4(diffuse) * in_color;
}

void main() {
  out_color = shadeDiffuse();
  out_color.a = in_color.a;
}

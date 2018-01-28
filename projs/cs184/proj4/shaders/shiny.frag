#version 330

uniform vec4 in_color;
uniform vec3 eye;
uniform vec3 light;
uniform sampler2D envmap;

in vec4 vertex;
in vec4 normal;
// in vec4 gl_FragCoord;

out vec4 out_color;
#define PI 3.1415926



vec4 shadeShiny() {
	float p = 8.0;

	vec4 color = in_color * 0.35;

	vec3 lightVec = light - vertex.xyz;
	vec3 lightDir = normalize(lightVec);
	vec3 outDir = normalize(eye - vertex.xyz);
	vec3 n = normalize(normal.xyz);

	float distFactor = 1.0 / sqrt(dot(lightVec, lightVec));

	vec4 ambient = color * 0.9;
	// ambient.a = 0.5;

	float diffuseDot = dot(n, lightDir);
	vec4 diffuse = color * clamp(diffuseDot, 0.0, 1.0);

	vec3 halfAngle = normalize(outDir + lightDir);
	vec4 specularColor = min(color + 0.2, 1.0);
	float specularDot = dot(n, halfAngle);
	vec4 specular = 0.5 * specularColor * pow(clamp(specularDot, 0.0, 1.0), p);

	vec4 soft_shade = specular + diffuse + ambient;
	// vec4 specular = shadePhong();
	vec4 one = vec4(1.0);
	if (dot(specular, one) > 0.8) {
		return vec4(1.0);
	}
	if (dot(soft_shade, one) < 0.7) {
		return vec4(vec3(0.1), 1.0) * in_color;
	} else if (dot(soft_shade, one) < 0.8) {
		return vec4(vec3(0.3), 1.0) * in_color;
	} else if (dot(soft_shade, one) < 0.97) {
		return vec4(vec3(0.5), 1.0) * in_color;
	} else {
		return vec4(vec3(1.0), 1.0) * in_color;
	}
}

void main() {
  out_color = shadeShiny();
  out_color.a = in_color.a;
}

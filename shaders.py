
vertex_shader = """
#version 440

layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;
layout (location = 1) in vec3 cColor;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

uniform float time;
varying vec3 vPosition;

out vec4 vertexColor;
out vec2 vertexTexcoords;
out vec3 miColor;

varying float intensity;

void main()
{
    float intensity = dot(model * normal, normalize(light - pos));

    gl_Position = projection * view * model * pos;
    vertexColor = color * intensity;
    vertexTexcoords = texcoords;
    miColor = cColor;
}
"""
#r.shaderList.append(vertex_shader)

fragment_shader ="""
#version 440

layout (location = 0) out vec4 diffuseColor;

in vec4 vertexColor;
in vec2 vertexTexcoords;

uniform sampler2D tex;

void main()
{
    diffuseColor =  vertexColor * texture(tex, vertexTexcoords);
}
"""
#r.shaderList.append(fragment_shader)

colors_shader = """
#version 440

layout(location = 0) out vec4 fragColor;

in vec3 miColor;

void main()
{
    fragColor = vec4(miColor, 1);
}
"""
#r.shaderList.append(colors_shader)

toon_shader = """
#version 440

varying float intensity;

void main()
{
	vec4 color;
	if (intensity > 0.95)

		color = vec4(1.0,0.5,0.5,1.0);
	else if (intensity > 0.5)
		color = vec4(0.6,0.3,0.3,1.0);
	else if (intensity > 0.25)
		color = vec4(0.4,0.2,0.2,1.0);
	else
		color = vec4(0.2,0.1,0.1,1.0);
	gl_FragColor = color;

}
"""
#r.shaderList.append(toon_shader)

# http://shdr.bkcore.com/#1/lZAxT8MwEIX/yslTClGbiLK0YkJiAzGxUFSZxEldOb7Idlraqv+ds92kUGBgiGL7fXf37h1YiUXXCO0sm72y1ohCWokaVrJetVAp5G6+0BtudlLXsBHFDVRPaBqu6JkElCU0XOpktNCHhYaIlNLAXTgmWZqn2WgOk0noCRpRD1yBCgcyP5M7oRRuPea/4IJ6VlVnBdHjW7iGEl1ycpLSuNHck7VaPhhe35/bTpO+7ipOSyEfZ54+svTPfblzRr53TkSbLVrpiPqp6D6KTsuKzpSF618fOaEf37UpNFgK9SLF9ne5NbgWhR826P8I/6TS6tGC3IvkqxkKIV5jXD4fvxzxF7YIDOH1mw+phYyfT69Ud+mXCqkmxPuWstCVzeLfTmy351qLpQ97vLbs+Ak=
yellow_shader = """
#version 440

varying vec3 miColor;

void main()
{
  vec3 dir = vec3(0,1,0); // high noon
  vec3 color = vec3(1,1,0); // yellow
  
  float diffuse = .5 + dot(miColor,dir);
  gl_FragColor = vec4(diffuse * color, 1.0);
}
"""
#r.shaderList.append(yellow_shader)

blue_shader = """
#version 440

varying vec3 miColor;

void main()
{
  vec3 dir = vec3(0,1,0); // high noon
  vec3 color = vec3(0,0,1); // blue
  
  float diffuse = .5 + dot(miColor,dir);
  gl_FragColor = vec4(diffuse * color, 1.0);
}
"""
#r.shaderList.append(blue_shader)

green_shader = """
#version 440

varying vec3 miColor;

void main()
{
  vec3 dir = vec3(0,1,0); // high noon
  vec3 color = vec3(0,1,0); // green
  
  float diffuse = .5 + dot(miColor,dir);
  gl_FragColor = vec4(diffuse * color, 1.0);
}
"""
#r.shaderList.append(green_shader)
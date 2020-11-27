import pygame
import glm
from pygame.locals import *
from gl import Renderer, Model
import shaders



deltaTime = 0.0

pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)


renderer = Renderer(screen)
renderer.camPosition.z = 3
renderer.pointLight.x = 5
#renderer.pointLight.x = -5

renderer.setShaders(shaders.vertex_shader, shaders.fragment_shader)


barrel = Model('models/barrel/barrel.obj', 'models/barrel/barrel.bmp')
barrel.scale = glm.vec3(0.5,0.5,0.5)
renderer.modelList.append(barrel)

key = Model('models/key/key.obj', 'models/key/key.bmp')
key.scale = glm.vec3(0.5,0.5,0.5)
key.rotation = glm.vec3(0,90,0)
renderer.modelList.append(key)

boat = Model('models/boat/boat.obj', 'models/boat/boat.bmp')
boat.scale = glm.vec3(0.1,0.1,0.1)
#boat.rotation = glm.vec3(0,0,0)
renderer.modelList.append(boat)

boat2 = Model('models/boat2/boat2.obj', 'models/boat2/boat2.bmp')
boat2.scale = glm.vec3(0.003, 0.003, 0.003)
boat2.rotation = glm.vec3(0,90,0)
renderer.modelList.append(boat2)

# renderer.shaderList.append(shaders.fragment_shader)
# renderer.shaderList.append(shaders.colors_shader)
# print(renderer.shaderList)

pygame.mixer.music.load('gnr.mp3')
pygame.mixer.music.play(0)

isPlaying = True
while isPlaying:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        #renderer.camPosition.x += 1 * deltaTime
        renderer.angle -= 100 * deltaTime
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        #renderer.camPosition.x -= 1 * deltaTime
        renderer.angle += 100 * deltaTime
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        renderer.camPosition.y += 1 * deltaTime
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        renderer.camPosition.y -= 1 * deltaTime

    # if keys[pygame.K_r] or keys[pygame.K_c]:
    #     renderer.rotaYaw()
    # if keys[pygame.K_q] or keys[pygame.K_x]:
    #     renderer.rotaPitch()
    # if keys[pygame.K_e] or keys[pygame.K_z]:
    #     renderer.rotaRoll()


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                renderer.filledMode()
            elif ev.key == pygame.K_2:
                renderer.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_SPACE:
                renderer.activeModelIndex = (renderer.activeModelIndex + 1) % len(renderer.modelList)
            elif ev.key == pygame.K_z:
                renderer.setShaders(shaders.vertex_shader, shaders.colors_shader)
            elif ev.key == pygame.K_x:
                renderer.setShaders(shaders.vertex_shader, shaders.toon_shader)
            elif ev.key == pygame.K_c:
                renderer.setShaders(shaders.vertex_shader, shaders.yellow_shader)
            elif ev.key == pygame.K_v:
                renderer.setShaders(shaders.vertex_shader, shaders.blue_shader)
            elif ev.key == pygame.K_b:
                renderer.setShaders(shaders.vertex_shader, shaders.green_shader)
            elif ev.key == pygame.K_n:
                renderer.setShaders(shaders.vertex_shader, shaders.fragment_shader)
        elif ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 4:
                if renderer.camPosition.z >= 0.75:
                    renderer.camPosition.z -= 2 * deltaTime
            elif ev.button == 5:
                if renderer.camPosition.z <= 10:
                    renderer.camPosition.z += 2 * deltaTime
            elif ev.button == 1:
                renderer.activeShaderIndex = (renderer.activeShaderIndex + 1) % len(renderer.shaderList)

    renderer.cameraView()
    renderer.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time()/1000

pygame.quit()

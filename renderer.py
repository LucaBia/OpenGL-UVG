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
# renderer.camPosition.z = 300
renderer.camPosition.z = 3
renderer.pointLight.x = 5

renderer.setShaders(shaders.vertex_shader, shaders.fragment_shader)

man = Model('models/model.obj', 'models/textures/model.bmp')
#black.scale = glm.vec3(0.5,0.5,0.5)
renderer.modelList.append(man)

barrel = Model('models/barrel/barrel.obj', 'models/barrel/barrel.bmp')
barrel.scale = glm.vec3(0.5,0.5,0.5)
renderer.modelList.append(barrel)

key = Model('models/key/key.obj', 'models/key/key.bmp')
key.scale = glm.vec3(0.5,0.5,0.5)
renderer.modelList.append(key)

boat = Model('models/boat/boat.obj', 'models/boat/boat.bmp')
boat.scale = glm.vec3(0.1,0.1,0.1)
renderer.modelList.append(boat)
#renderer.modelList.append(Model('models/Skull/Boat.obj', 'models/Skull/boat.bmp'))



isPlaying = True
while isPlaying:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        renderer.camPosition.x += 1 * deltaTime
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        renderer.camPosition.x -= 1 * deltaTime
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        renderer.camPosition.z -= 1 * deltaTime
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        renderer.camPosition.z += 1 * deltaTime

    if keys[pygame.K_r] or keys[pygame.K_c]:
        renderer.rotaYaw()
    if keys[pygame.K_q] or keys[pygame.K_x]:
        renderer.rotaPitch()
    if keys[pygame.K_e] or keys[pygame.K_z]:
        renderer.rotaRoll()


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

    renderer.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time()/1000

pygame.quit()

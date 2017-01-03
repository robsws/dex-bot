from gopigo import *
from enum import Enum
import sys
import pygame

pygame.init()
# pygame.key.set_repeat(100,100)

speed = 50

leftspeed = 0
rightspeed = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == K_UP:
        leftspeed += speed
        rightspeed += speed
      elif event.key == K_LEFT:
        leftspeed += speed
      elif event.key == K_RIGHT:
        rightspeed += speed
    elif event.type == pygame.KEYUP:
      if event.key == K_UP:
        leftspeed -= speed
        rightspeed -= speed
      elif event.key == K_LEFT:
        leftspeed += speed
      elif event.key == K_RIGHT:
        rightspeed += speed
    set_left_speed(leftspeed)
    set_right_speed(rightspeed)
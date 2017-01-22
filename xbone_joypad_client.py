import sys, pygame
import xmlrpc.client
from pygame.locals import *

# Initialise pygame
pygame.init()
size = width, height = 1000, 800
black = 0, 0, 0
clock = pygame.time.Clock()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(str(len(joysticks)) + " joysticks detected.")
for joystick in joysticks:
  joystick.init()
  name = joystick.get_name()
  print("Joystick found: " + name)
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# Initialise RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Event loop
speed = [0,0]
while 1:
  i = 0
  for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      # Get joypad input
      if event.type == JOYAXISMOTION:
        if event.axis == 0:
          speed[0] = int(event.value * 10)
        elif event.axis == 1:
          speed[1] = int(event.value * 10)


  ballrect = ballrect.move(speed)

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()
  clock.tick(60)
  if i % 20 == 0:
    # Move the robot
    server.move_robot(speed[0], speed[1])

  i += 1
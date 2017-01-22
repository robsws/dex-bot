import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 1000, 800
# speed = [1, 1]
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

speed = [0,0]

while 1:
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
  # if ballrect.left < 0 or ballrect.right > width:
  #     speed[0] = -speed[0]
  # if ballrect.top < 0 or ballrect.bottom > height:
  #     speed[1] = -speed[1]

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()
  clock.tick(60)
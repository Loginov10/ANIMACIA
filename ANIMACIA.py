
import pygame
import sys
from random import*
import random

def Päri(): #По часовой
    global posX, posY, sammX, sammY
    if posX == X - pilt.get_rect().width and posY == Y - pilt.get_rect().height:
        sammX, sammY = -1, 0
    elif posX == X - pilt.get_rect().width and posY == 0:
        sammX, sammY = 0, 1
    elif posX == 0 and posY == 0:
        sammX, sammY = 1, 0
    elif posX == 0 and posY == Y - pilt.get_rect().height:
        sammX, sammY = 0, -1
    posX += sammX
    posY += sammY
    ekraan.blit(pilt, (posX, posY))
    pygame.display.flip()
    pygame.time.delay(10)


def Vastu(): #Против часовой
    global posX, posY, sammX, sammY
    if posY <= 0 and posX >= ekraan.get_width() - pilt.get_width():
        sammX = -2
        sammY = 0
    elif posY >= ekraan.get_height() - pilt.get_height() and posX >= ekraan.get_width() - pilt.get_width():
        sammX = 0
        sammY = -2
    elif posY >= ekraan.get_height() - pilt.get_height() and posX <= 0:
        sammX = 2
        sammY = 0
    elif posY <= 0 and posX <= 0:
        sammX = 0
        sammY = 2
    posX += sammX
    posY += sammY
    ekraan.blit(pilt, (posX, posY))
    pygame.display.flip()
    pygame.time.delay(10)


def Randm():#Оталкивается от кроёв
    global posX, posY, sammX, sammY
    if posY <= 0:
        sammX = random.choice([-2, -1, 1, 2])
        sammY = random.choice([1, 2])
    elif posY >= ekraan.get_height() - pilt.get_height():
        sammX = random.choice([-2, -1, 1, 2])
        sammY = random.choice([-1, -2])
    elif posX >= ekraan.get_width() - pilt.get_width():
        sammX = random.choice([-1, -2])
        sammY = random.choice([-2, -1, 1, 2])
    elif posX <= 0:
        sammX = random.choice([1, 2])
        sammY = random.choice([-2, -1, 1, 2])
    posX += sammX
    posY += sammY
    ekraan.blit(pilt, (posX, posY))
    pygame.display.flip()
    pygame.time.delay(10)


pygame.init()
X, Y = 640, 480
ekraan = pygame.display.set_mode([X, Y])
pygame.display.set_caption("raketa")
# цвет фона
fon = (100, 255, 100)
ekraan.fill(fon)


pilt=pygame.image.load("among.png")
posX, posY = X - pilt.get_rect().width, Y - pilt.get_rect().height
sammX, sammY = 0, 0

lõpp=False

kell=pygame.time.Clock()


lõpp=False
kell=pygame.time.Clock()
v=[Päri,Vastu,Randm]
while not lõpp:
    kell.tick(400)
    events = pygame.event.get()
    for i in pygame.event.get():       
        if i.type == pygame.QUIT:
            lõpp = True
    random.choice(v)()
    ekraan.fill(fon)
pygame.quit()

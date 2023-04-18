
import pygame,sys

pygame.init()
#värvid
koolane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
among=pygame.image.load("among.png")

posX=X-among.get_rect().width
posY=Y-among.get_rect().height

lopp=False
sammX=2
sammY=0
while not lopp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    posX-=sammX
    if posX>X-among.get_rect().width or posX<0:
        sammX=-sammX
    if posY>Y-among.get_rect().height or posY<0:
        sammY=-sammY
    if posX<0:
        sammY=2
        sammX=0
    posX-=sammX
    posY-=sammY
    
    ekraan.blit(among,(posX,posY))     
    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()
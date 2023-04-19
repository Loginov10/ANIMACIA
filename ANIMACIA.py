
import pygame,sys
import random
def Liik():
	global posX,posY
	sammX=0
	sammY=0
	
	if posX==0 and posY==0:
		sammX=1
		sammY=0		
	if posX==X-among.get_rect().width and posY<=Y-among.get_rect().height:	
		sammX=0
		sammY=1
	if posX<=X-among.get_rect().width and posY==Y-among.get_rect().height:		
		sammX=1
		sammY=0
		sammX=-sammX
	if posX==0 and posY>=Y-among.get_rect().height:					
		sammX=0
		sammY=1
		sammY=-sammY
	
	posX+=sammX
	posY+=sammY
	ekraan.blit(among,(posX,posY))	
	pygame.display.flip()
	ekraan.fill(hall)


def Likk2():
	global posX,posY
	sammX=0
	sammY=0
	
	if posX==0 and posY==0:
		sammX=1
		sammY=0		
	if posX==X-among.get_rect().width and posY<=Y-among.get_rect().height:	
		sammX=0
		sammY=1
	if posX<=X-among.get_rect().width and posY==Y-among.get_rect().height:		
		sammX=1
		sammY=0
		sammX=-sammX
	if posX==0 and posY>=Y-among.get_rect().height:					
		sammX=0
		sammY=1
		sammY=-sammY
		 
	posX+=sammX
	posY+=sammY
	ekraan.blit(among,(posX,posY))	
	pygame.display.flip()
	ekraan.fill(roheline)
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
r=random.randint(1,2)
while not lopp:
	kell.tick(200)
	events=pygame.event.get()
	
	for i in pygame.event.get():
		if i.type==pygame.QUIT():
			sys.exit()
	if r==1:
		Liik()
		
	if r==2:
		Likk2()
		
pygame.quit()

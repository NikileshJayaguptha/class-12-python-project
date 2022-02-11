import pygame
import os

#! initialising
pygame.init()

#! window setup
height = 600

width = 1100

WIN = pygame.display.set_mode((width,height))

pygame.display.set_caption("Dino Run")


#! Loading Images

Running = [
	pygame.image.load(os.path.join("Chrome Dinosaur/assets/Dino","DinoRun1.png")),
	pygame.image.load(os.path.join("Chrome Dinosaur/assets/Dino","DinoRun2.png"))
]

Ducking = [
	pygame.image.load(os.path.join("Chrome Dinosaur/assets/Dino","DinoDuck1.png")),
	pygame.image.load(os.path.join("Chrome Dinosaur/assets/Dino","DinoDuck2.png"))
]

bg = pygame.image.load(os.path.join("Chrome Dinosaur/assets/Other","Track.png"))


#! classes for drawings

class Ground():
	def __init__(self) :
		self.img = bg
		self.rect = self.img.get_rect()

		self.width = self.img.get_width()
		self.x1 = 0
		self.x2 = self.width
		self.y = 400
	
	def update(self,vel):
		self.x1 -= vel
		self.x2 -=vel

		if self.x1<= -self.width:
			self.x1 = self.width

		if self.x2<= -self.width:
			self.x2 = self.width

	def draw(self,window):
		window.blit(self.img,(self.x1,self.y))
		window.blit(self.img,(self.x2,self.y))

#!Dino class
class Dino():
	def __init__(self,x,y):
		self.x = x
		self.y = y

		self.runlist = Running
		self.ducklist=Ducking
		self.run_count = 0
		self.img = self.runlist[self.run_count]
		self.rect = self.img.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
			self.run_count+=1
			if self.run_count+1>=4:
				self.run_count = 0

	def draw(self,win):
		win.blit(self.img,self.rect)	


#! animation functions
def groundanimation():
	ground.draw(WIN)
	ground.update(4)

def dinoanimation():
	dino.draw(WIN)

#! object initialisation
ground = Ground()
dino = Dino(50,320)

#! Colours
WHITE = (255,255,255)
GRAY =(32, 32, 32)

#! Draw Window
def draw_window():
	WIN.fill(GRAY)
	#! ground animation
	groundanimation()

	#!dino animation
	dinoanimation()

	#!updating the window
	pygame.display.update()

#!loop variables
run = True
clock = pygame.time.Clock()
FPS= 60

#! main loop
while run:

	#! setting the fps for game
	clock.tick(FPS)

	#! quitting the loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run =False

	#! drawing things
	draw_window()

pygame.quit()
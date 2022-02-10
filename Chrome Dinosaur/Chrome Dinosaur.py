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


#! animation functions
def groundanimation():
	ground.draw(WIN)
	ground.update(4)

#! object initialisation
ground = Ground()

#! Colours
WHITE = (255,255,255)
GRAY =(128, 128, 128)

#! Draw Window
def draw_window():
	WIN.fill(GRAY)
	#! ground animation
	groundanimation()
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
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run =False
	#! drawing things
	draw_window()


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

		self.index=0
		self.run_count=0
		self.rect = self.img.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

		self.vel = 0
		self.gravity = 1
		self.jumpHeight = 20
		self.isJumping = False
		
		

	def update(self, duck,jump):
		if not duck:
			if not self.isJumping and jump:
				self.vel = -self.jumpHeight
				self.isJumping = True

			self.vel += self.gravity
			if self.vel >= self.jumpHeight:
				self.vel = self.jumpHeight

			self.rect.y += self.vel
			if self.rect.y > self.y:
				self.rect.y = self.y
				self.isJumping = False
	
	
			
		if duck:
			self.run_count+=1
			if self.run_count+1>=6:
				self.index = (self.index+1) % len(self.ducklist)
				self.img = self.ducklist[self.index]
				self.rect = self.img.get_rect()
				self.rect.x = self.x
				self.rect.y = self.y+35
				self.run_count=0

		elif self.isJumping:
				self.index = 0
				self.run_count = 0
				self.image = self.runlist[self.index]
			
		else:
			self.run_count+=1
			if self.run_count+1>=6:
				self.index = (self.index+1) % len(self.runlist)
				self.img = self.runlist[self.index]
				self.rect = self.img.get_rect()
				self.rect.x = self.x
				self.rect.y = self.y
				self.run_count=0
		

	def draw(self,win):
		win.blit(self.img,self.rect)	

#! Cactus class

class Cactus(pygame.sprite.Sprite):
	def __init__(self,type):
		super(Cactus,self).__init__()
	
	


#! animation functions
def groundanimation():
	ground.draw(WIN)
	ground.update(6)

def dinoanimation():
	global duck
	duck = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_DOWN]:
		duck = True
	dino.draw(WIN)
	dino.update(duck,jump)

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
FPS= 30
duck = False
jump = False


#! main loop
while run:
	
	#! setting the fps for game
	clock.tick(FPS)

	#! quitting the loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	#! key bindings
	keys = pygame.key.get_pressed()

	if keys[pygame.K_DOWN]:
		duck = True
	else:
		duck =False
	if keys[pygame.K_UP]:
		jump =True
	else:
		jump = False
	

	
	#! drawing things
	draw_window()

pygame.quit()
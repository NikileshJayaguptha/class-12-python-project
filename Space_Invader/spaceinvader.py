lvl=0
def spaceinvader(id1):
	from tkinter import N
	import pygame
	import os
	import time
	import random
	from DB import cursor,mydb 
	pygame.font.init()
	#* window setup

	width = 750
	height = 750
		
	WIN = pygame.display.set_mode((width,height))
	pygame.display.set_caption("space invader")

	#*Loading all images

	#!main player assets
	PLAYER_SHIP = pygame.image.load(os.path.join("Space_invader/assets","player.png"))
	BLUEBULLET = pygame.image.load(os.path.join("Space_invader/assets","bluebullet.png"))

	#! enemy stuffs
	REDSPACESHIP= pygame.image.load(os.path.join("Space_invader/assets","redspaceship.png"))
	REDBULLET= pygame.image.load(os.path.join("Space_invader/assets","redbullet.png"))

	GREENSPACESHIP= pygame.image.load(os.path.join("Space_invader/assets","greenspaceship.png"))
	GREENBULLET= pygame.image.load(os.path.join("Space_invader/assets","greenbullet.png"))

	YELLOWSPACESHIP= pygame.image.load(os.path.join("Space_invader/assets","yellowspaceship.png"))
	YELLOWBULLET= pygame.image.load(os.path.join("Space_invader/assets","yellowbullet.png"))

	#!background
	BG= pygame.transform.scale(pygame.image.load(os.path.join("Space_invader/assets","bg.jpg")),(width,height))

	#* classes for drawings

	#!Player class
	class Player():
		COOLDOWN = 30 
		def __init__(self,x,y,health = 100):
			self.x = x
			self.y = y
			self.health = health
			self.img = PLAYER_SHIP
			self.bullet = YELLOWBULLET
			self.mask = pygame.mask.from_surface(self.img)
			self.max_health = health
			self.lasers = []
			self.cd =0

			self.db=False
			

		def draw(self,window):
			window.blit(self.img,(self.x,self.y))
			for laser in self.lasers:
				laser.draw(window)
			
			self.healthbar(window)
			
		
		def shootlasers(self,vel,obj):
			self.cooldown()
			for laser in self.lasers:
				laser.move(vel)
				if laser.off_screen(height):
					self.lasers.remove(laser)
				else:
					for ob in obj:
						if laser.collision(ob):
							obj.remove(ob)
							self.lasers.remove(laser)

		
		def cooldown(self):
			if self.cd >= self.COOLDOWN:
				self.cd = 0
			elif self.cd>0:
				self.cd+=1

		
		def shoot(self):
			if self.cd == 0:
				laser = Laser(self.x-20,self.y-30,self.bullet)
				self.lasers.append(laser)
				self.cd = 1
		
		def healthbar(self,window):
			pygame.draw.rect(window,(255,0,0),(self.x,self.y + self.img.get_height() +10 ,self.img.get_width(),10))
			pygame.draw.rect(window,(0,255,0),(self.x,self.y + self.img.get_height() +10 ,self.img.get_width()*(1-((self.max_health-self.health)/self.max_health)),10))

		
	#!Enemies class
	class Enemy():
		color = {
			"red":(REDSPACESHIP,REDBULLET),
			"green":(GREENSPACESHIP,GREENBULLET),
			"yellow":(YELLOWSPACESHIP,YELLOWBULLET)
		}
		COOLDOWN = 30
		def __init__(self,x,y,clr,health = 100):
			self.x = x
			self.y = y
			self.health = health
			self.img ,self.bullet= self.color[clr]
			self.cd = 0
			self.mask = pygame.mask.from_surface(self.img)
			self.max_health = health
			self.lasers = []

			

		def cooldown(self):
			if self.cd >= self.COOLDOWN:
				self.cd = 0
			elif self.cd>0:
				self.cd+=1

		def shootlasers(self,vel,obj):
			self.cooldown()
			for laser in self.lasers:
				laser.move(-vel)
				if laser.off_screen(height):
					self.lasers.remove(laser)
				elif laser.collision(obj):
					obj.health-=10
					self.lasers.remove(laser)
					
		
		def shoot(self):
			if self.cd == 0:
				laser = Laser(self.x,self.y,self.bullet)
				self.lasers.append(laser)
				self.cd = 1

		def draw(self,window):
			window.blit(self.img,(self.x,self.y))
			for laser in self.lasers:
				laser.draw(window)

			

	#!Laser class
	class Laser:
		def __init__(self,x,y,img):
			self.x = x
			self.y = y
			self.img = img
			self.mask = pygame.mask.from_surface(self.img)
		
		def draw(self,window):
			window.blit(self.img,(self.x,self.y))
		
		def move(self,vel):
			self.y-=vel
		
		def off_screen(self,height):
			return not(self.y <height and self.y >=0)

		def collision(self,img2):
			return collide(img2,self)
		
	def collide(a,b):
		x = b.x-a.x
		y = b.y - a.y 
		return a.mask.overlap(b.mask,(x,y)) != None



	#* Draw Function
	def draw_window():
		WIN.blit(BG,(0,0))
		#!writing text
		lives_draw = font.render(f"LIVES: {lives}",1,(255,255,255))
		level_draw = font.render(f"LEVEL: {lvl}",1,(255,255,255))
		WIN.blit(lives_draw,(10,10))
		WIN.blit(level_draw,(590,10))
		
		mainship.draw(WIN)

		for enemy in enemies:
			enemy.draw(WIN)


		
		if gameover == True:
			llabel = lostfont.render("GAME OVER!!",1,(255,255,255))
			WIN.blit(llabel,(350-llabel.get_width()/2,350))

			if not mainship.db:
				cursor.execute(f"insert into scores values('{id1}','{lvl}','spaceinvader')")
				mydb.commit()
				mainship.db = True


		
		
		pygame.display.update()


	#* variables for mainloop
	run = True
	gameover = False
	fps = 60
	lvl = 0
	lives = 5
	font = pygame.font.SysFont("comicsans",50)
	lostfont = pygame.font.SysFont("comicsans",70)
	clock = pygame.time.Clock()

	enemies = []
	enemyno = 0  

	#! ship class
	mainship = Player(300,650)



	#* mainloop
	while run:

		#!FPS
		clock.tick(fps)
		#! endgame
		if lives<=0 or mainship.health<=0:
			gameover = True

		#! spawning enemies
		if len(enemies) == 0 and gameover == False:
			lvl +=1
			enemyno+=2
			for i in range(enemyno):
				enemies.append(Enemy(random.randrange(100,650),random.randrange(-750,0),random.choice(["red","green","yellow"])))
		
		

		#! Player Keybindings
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]: #? left
			if mainship.x - 5 >0:
				mainship.x-=5
		if keys[pygame.K_d]:#? right
			if mainship.x +60 +  5 <width:
				mainship.x+=5
		if keys[pygame.K_w]:#? up
			if mainship.y-5>0:
				mainship.y-=5
		if keys[pygame.K_s]:#? down
			if mainship.y + 50 +5 <height:
				mainship.y+=5
		if keys[pygame.K_SPACE]:
			mainship.shoot()


	#! enemy movement
		for i in enemies:
			i.y+=2
			i.shootlasers(4,mainship)

			if random.randrange(1,250) == 1:
				i.shoot()

			if i.y + 5>height:
				if lives>0:
					lives-=1
				enemies.remove(i)

			if collide(i,mainship):
				mainship.health-=10
				enemies.remove(i)
		mainship.shootlasers(4,enemies)
		draw_window()
	pygame.quit()	

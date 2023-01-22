# 1 - Import Library ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pygame
from pygame.locals import *
import time, math

# 2 - Initialize the Game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

running = True

playerpos = [15, 15] # initial position for player

sampah_posisi_temp = [[0,3], [1,2], [3,4], [2,4]]
sampah_posisi = []

for posisi in sampah_posisi_temp:
	posisi_temp = posisi.copy()
	posisi_temp[0] = 15 + (80*posisi_temp[0])
	posisi_temp[1] = 15 + (80*posisi_temp[1])
	sampah_posisi.append(posisi_temp)

white = "#cfcfcf"

tujuan = playerpos.copy()
tujuan[0] = tujuan[0] + (80*3)
tujuan[1] = tujuan[1] + (80*4)

count = 0
arah = 'horizontal'

# 3 - Load Game Assets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3.1 - Load Images
player = pygame.image.load("vacuum.png")
player = pygame.transform.smoothscale(player, (50, 50)) 

sampah = []
for i in range(len(sampah_posisi)):
	sampah_temp = pygame.image.load("trash.png")
	sampah_temp = pygame.transform.smoothscale(sampah_temp, (50, 50))
	sampah.append(sampah_temp)

def kotak():
	y = 0
	for i in range(5):
		x = 0
		for j in range(5):
			pygame.draw.rect(screen, "#000000",(x, y, 80, 80),1)
			x += 80
		y += 80

## 4 - The Game Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while(running):
    
	# 5 - Clear the screen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	screen.fill(white)
	kotak()

	# 6 - Draw the game object ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	for i in range(len(sampah)):
		screen.blit(sampah[i], sampah_posisi[i])
	screen.blit(player, playerpos)

	# 7 - Update the sceeen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	pygame.display.flip()

	# 8 - Event Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	for event in pygame.event.get():
		# event saat tombol exit diklik
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)

	# print("X : "+str(playerpos[0]))
	# print("Y : "+str(playerpos[1]))
	if playerpos[0] == tujuan[0]:
		arah = 'vertikal'
	else:
		if arah == 'horizontal':
			count += 1
			if(playerpos[0] < tujuan[0]):
				playerpos[0] += 0.1
			if count == 800:
				count = 0
				arah = 'vertikal'
				playerpos[0] = math.ceil(playerpos[0])

	if playerpos[1] == tujuan[1]:
		arah = 'horizontal'
	else:
		if arah == 'vertikal':
			count += 1
			if(playerpos[1] < tujuan[1]):
				playerpos[1] += 0.1
			if count == 800:
				count = 0
				arah = 'horizontal'
				playerpos[1] = math.ceil(playerpos[1])
    
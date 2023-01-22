"""
    PROGRAM SIMULASI AGEN PENYEDOT DEBU V.0.0.1
    abdiansah@unsri.ac.id - Agustus 2021
"""

import pygame
import time, math
from pygame.locals import *

class UI:

	__lingkungan = None
	__agen = None

	__screen = None
	__running = True
	__width, __height = 640+100, 480+100
	__playerpos = [15, 15]
	__agen_obj = None
	__bg_color = "#cfcfcf"
	__lokasi_sampah = []
	__sampah = []
	__baris = 0
	__kolom = 0
	__count = 0
	__arah = 'horizontal'
	__max_baterai = 0

	__KIRI = 'kiri'
	__ATAS = 'atas'
	__KANAN = 'kanan'
	__BAWAH = 'bawah'

	def __init__(self, agen, lingkungan, baris, kolom):
		self.__lingkungan = lingkungan
		self.__agen = agen
		pygame.init()
		self.__screen = pygame.display.set_mode((self.__width, self.__height))
		self.__agen_obj = pygame.image.load("vacuum.png")
		self.__agen_obj = pygame.transform.smoothscale(self.__agen_obj, (50, 50))
		lokasi_sampah_temp = [lokasi_temp for lokasi_temp in self.__lingkungan.get_lokasi() if lokasi_temp[2] == 1]
		self.__set_posisi_sampah(lokasi_sampah_temp)
		self.__set_sampah()
		self.__baris = baris
		self.__kolom = kolom

	def __set_posisi_sampah(self, lokasi_sampah_temp):
		posisi_sampah_temp = lokasi_sampah_temp.copy()
		for posisi in posisi_sampah_temp:
			posisi_temp = posisi.copy()
			posisi_temp[0] = 15 + (80*posisi_temp[0])
			posisi_temp[1] = 15 + (80*posisi_temp[1])
			posisi_temp[0], posisi_temp[1] = posisi_temp[1], posisi_temp[0]
			posisi_temp.pop(2)
			self.__lokasi_sampah.append(posisi_temp)

	def __set_sampah(self):
		for i in range(len(self.__lokasi_sampah)):
			sampah_temp = pygame.image.load("trash.png")
			sampah_temp = pygame.transform.smoothscale(sampah_temp, (50, 50))
			self.__sampah.append(sampah_temp)

	def __gambar_kotak(self):
		y = 0
		for i in range(self.__baris):
			x = 0
			for j in range(self.__kolom):
				pygame.draw.rect(self.__screen, "#000000",(x, y, 80, 80),1)
				x += 80
			y += 80

	def __gambar_baterai(self):

		x = (self.__kolom+1)*80
		

		kons_baterai_temp = self.__agen.get_baterai()/self.__max_baterai
		kons_baterai = int(kons_baterai_temp*100)
		myfont = pygame.font.SysFont('Comic Sans MS', 15)
		textsurface = myfont.render(str(kons_baterai)+'%', False, (0, 0, 0))
		self.__screen.blit(textsurface,(x+20,15))

		y = 50
		batas_y = 150
		# y = 45
		tes = (kons_baterai_temp*(batas_y-y))+y
		
		y += int(tes)
		batas_y -= int(tes)

		if kons_baterai <= 50:
			warna = "#cf4523"
		else:
			warna = "#29cf23"
		# batas_y = (5*(self.__max_baterai+1))+(3*(self.__max_baterai-1))+5
		
		pygame.draw.rect(self.__screen, "#000000",(x, 45, 80, 160),3)
		pygame.draw.rect(self.__screen, warna,(x+5, 50, 70, 150))
		pygame.draw.rect(self.__screen, "#cfcfcf",(x+5, y, 70, batas_y))

	def __jalan(self, posisi_tujuan):
		# print(self.__playerpos)
		# print(posisi_tujuan)
		if self.__playerpos[0] == posisi_tujuan[0]:
				self.__arah = 'vertikal'
		else:
			if self.__arah == 'horizontal':
				# print(self.__count)
				if self.__count >= 400 and self.__playerpos[0] < posisi_tujuan[0]:
					self.__count = 0
					self.__arah = 'vertikal'
					self.__playerpos[0] = math.ceil(self.__playerpos[0])
				elif self.__count >= 400 and self.__playerpos[0] > posisi_tujuan[0]:
					self.__count = 0
					self.__arah = 'vertikal'
					self.__playerpos[0] = math.floor(self.__playerpos[0])
				self.__count += 1
				if(self.__playerpos[0] < posisi_tujuan[0]):
					self.__playerpos[0] += 0.2
				else:
					self.__playerpos[0] -= 0.2
				
		if self.__playerpos[1] == posisi_tujuan[1]:
			self.__arah = 'horizontal'
		else:
			if self.__arah == 'vertikal':
				# print(self.__count)
				if self.__count >= 400 and self.__playerpos[1] < posisi_tujuan[1]:
					self.__count = 0
					self.__arah = 'horizontal'
					self.__playerpos[1] = math.ceil(self.__playerpos[1])
				elif self.__count >= 400 and self.__playerpos[1] > posisi_tujuan[1]:
					self.__count = 0
					self.__arah = 'horizontal'
					self.__playerpos[1] = math.floor(self.__playerpos[1])
				self.__count += 1
				if(self.__playerpos[1] < posisi_tujuan[1]):
					self.__playerpos[1] += 0.2
				else:
					self.__playerpos[1] -= 0.2
				

	def run(self):
		# tujuan = self.__playerpos.copy()
		# tujuan = tujuan_temp.copy()
		# tujuan[0] = 15 + (80*tujuan[0])
		# tujuan[1] = 15 + (80*tujuan[1])
		# tujuan[0], tujuan[1] = tujuan[1], tujuan[0]
		# tujuan.pop(2)

		# lokasi_sampah_temp = [lokasi_temp for lokasi_temp in self.__lingkungan.get_lokasi() if lokasi_temp[2] == 1]
		# self.__set_posisi_sampah(lokasi_sampah_temp)
		# self.__set_sampah()
		self.__max_baterai = self.__agen.get_baterai()

		tujuan_temp = self.__agen.alg_agen_cerdas()
		# print(tujuan_temp)
		tujuan = tujuan_temp.copy()
		tujuan[0] = 15 + (80*tujuan[0])
		tujuan[1] = 15 + (80*tujuan[1])
		tujuan[0], tujuan[1] = tujuan[1], tujuan[0]
		tujuan.pop(2)



		while(self.__running):
    
			self.__screen.fill(self.__bg_color)
			self.__gambar_kotak()
			self.__gambar_baterai()

			for i in range(len(self.__sampah)):
				self.__screen.blit(self.__sampah[i], self.__lokasi_sampah[i])
			self.__screen.blit(self.__agen_obj, self.__playerpos)

			pygame.display.flip()

			for event in pygame.event.get():
				# event saat tombol exit diklik
				if event.type == pygame.QUIT:
					pygame.quit()
					exit(0)

			
			self.__jalan(tujuan)
			
			# print(self.__playerpos)
			# print(tujuan)
			

			if self.__playerpos == tujuan:

				# lokasi_sampah_temp = [lokasi_temp for lokasi_temp in self.__lingkungan.get_lokasi() if lokasi_temp[2] == 1]
				# self.__set_posisi_sampah(lokasi_sampah_temp)
				# self.__set_sampah()
				idx = self.__lokasi_sampah.index(tujuan)
				self.__sampah.pop(idx)
				self.__lokasi_sampah.pop(idx)

				temp = tujuan.copy()
				temp[0] = (temp[0]-15)/80
				temp[1] = (temp[1]-15)/80
				temp[0], temp[1] = temp[1], temp[0]
				lokasi_awal = list(self.__agen.get_koordinat_agen(self.__agen.no_lokasi_agen))
				self.__agen.jalan(lokasi_awal, temp)

				self.__playerpos = tujuan.copy()
				tujuan_temp = self.__agen.alg_agen_cerdas()
				# print(tujuan_temp)
				tujuan = tujuan_temp.copy()
				tujuan[0] = 15 + (80*tujuan[0])
				tujuan[1] = 15 + (80*tujuan[1])
				tujuan[0], tujuan[1] = tujuan[1], tujuan[0]
				tujuan.pop(2)

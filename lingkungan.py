"""
    PROGRAM SIMULASI AGEN PENYEDOT DEBU V.0.0.1
    abdiansah@unsri.ac.id - Agustus 2021
"""

import random


class Lingkungan:
    __lokasi = []
    __dimensi = 0

    def __init__(self, baris, kolom, sampah):
        print('\nINFORMASI LINGKUNGAN')
        self.__dimensi = (baris, kolom)
        self.__set_lokasi(baris, kolom, sampah)  # baris, kolom, sampah

    def __generate_sampah(self, jml_lokasi, jml_sampah):
        if jml_lokasi > jml_sampah:
            randomlist = random.sample(range(1, jml_lokasi), jml_sampah)
            return randomlist
        else:
            print('- Error: Jumlah lokasi sampah tidak boleh lebih banyak dari jumlah lokasi!')
            return []

    def __set_lokasi(self, baris, kolom, sampah):
        lokasi2d = [[0 for i in range(kolom)] for j in range(baris)]
        print(f'- Jumlah baris\t: {baris}')
        print(f'- Jumlah kolom\t: {kolom}')
        print(f'- Jumlah lokasi\t: {baris * kolom}')
        print(f'- Jumlah sampah\t: {sampah}')
        lokasi_sampah = self.__generate_sampah((baris * kolom), sampah)
        print(f'- Lokasi sampah\t: {sorted(lokasi_sampah)} - ACAK')

        no_lokasi = 1
        for r in range(len(lokasi2d)):
            for c in range(len(lokasi2d[r])):
                # lokasi2d[r][c] = no_lokasi
                if no_lokasi in lokasi_sampah:
                    self.__lokasi.append([r, c, 1])
                else:
                    self.__lokasi.append([r, c, 0])
                no_lokasi += 1

        self.info_lokasi()

    def info_lokasi(self):
        print('\nREPRESENTASI LINGKUNGAN')
        baris, kolom = self.__dimensi
        idx_lokasi = 0
        for r in range(baris):
            str = ''
            for c in range(kolom):
                a, b, s = self.__lokasi[idx_lokasi]
                # str += f'L{idx_lokasi + 1}-{self.__lokasi[idx_lokasi]} \t'
                # str += f'L{idx_lokasi + 1} - S({a}, {b}, {s})  \t'
                if s==0:
                    str += f'L{idx_lokasi + 1} - (-----)\t'
                else:
                    str += f'L{idx_lokasi + 1} - (KOTOR)\t'
                idx_lokasi += 1
            print(str)

    def get_lokasi(self):
        return self.__lokasi

    def get_dimensi(self):
        return self.__dimensi

    def get_status(self, no_lokasi):
        return self.__lokasi[no_lokasi - 1][2]

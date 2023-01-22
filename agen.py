"""
    PROGRAM SIMULASI AGEN PENYEDOT DEBU V.0.0.1
    abdiansah@unsri.ac.id - Agustus 2021
"""

import sys
import time
import math
from os import system


class Agen:
    # LINGKUNGAN
    __lingkungan = None

    # PROPERTY
    no_lokasi_agen = 1
    __koordinat_lokasi = []
    __isi_baterai = 0
    __jml_langkah = 0
    __KIRI = 'kiri'
    __ATAS = 'atas'
    __KANAN = 'kanan'
    __BAWAH = 'bawah'
    __BERSIHKAN = 'sedot'

    # FUNGSI
    def __init__(self, lingkungan, no_lokasi_agen):
        self.__lingkungan = lingkungan
        self.no_lokasi_agen = no_lokasi_agen
        for lokasi in self.__lingkungan.get_lokasi():
            self.__koordinat_lokasi.append((lokasi[0], lokasi[1]))

        # (2 * baris) - 2 (tambahan jika kena tembok (kanan/kiri!)
        self.__isi_baterai = len(self.__lingkungan.get_lokasi()) + (self.__lingkungan.get_dimensi()[0]-1)

        print('\nINFORMASI AGEN')
        print(f'- No. lokasi awal Agen\t: L{self.no_lokasi_agen}')
        print(f'- Koordinat lokasi Agen\t: {self.get_koordinat_agen(self.no_lokasi_agen)}')
        status = self.__lingkungan.get_status(self.no_lokasi_agen)
        if status == 1:
            print(f'- Status lokasi\t\t: {status} - KOTOR')
            print(f'\t^ Lokasi kotor, lakukan pembersihan...')
            self.__tindakan(self.__BERSIHKAN, no_lokasi_agen)
        else:
            print(f'- Status lokasi\t\t: {status} - BERSIH')
        print(f'- Isi baterai\t\t: {self.__isi_baterai}')
        print(f'- Jumlah langkah\t: {self.__jml_langkah}')
        if status == 1:
            self.__lingkungan.info_lokasi()

    def get_baterai(self):
        return self.__isi_baterai
        
    def get_koordinat_agen(self, no_lokasi):
        return (self.__lingkungan.get_lokasi()[no_lokasi - 1][0], self.__lingkungan.get_lokasi()[no_lokasi - 1][1])

    def __set_no_lokasi_agen(self, koordinat):
        a, b = koordinat
        i = 0
        for lokasi in self.__lingkungan.get_lokasi():
            if (lokasi[0] == a) and (lokasi[1] == b):
                self.no_lokasi_agen = i + 1
                break
            i += 1

    def __set_status_bersih(self, no_lokasi_agen):
        self.__lingkungan.get_lokasi()[no_lokasi_agen - 1][2] = 0

    def __cek_baterai(self):
        if self.__isi_baterai != 0:
            self.__isi_baterai -= 1
            self.__jml_langkah += 1
            return True
        else:
            return False

    def __gerakan_legal(self, gerak):
        koordinat_agen = self.get_koordinat_agen(self.no_lokasi_agen)
        a, b = koordinat_agen
        if gerak == self.__KIRI:
            b -= 1
        elif gerak == self.__ATAS:
            a -= 1
        elif gerak == self.__KANAN:
            b += 1
        elif gerak == self.__BAWAH:
            a += 1
        else:
            print('\t* Error: Gerakan tidak tersedia!')
        koordinat_agen = (a, b)
        if koordinat_agen in self.__koordinat_lokasi:
            self.__set_no_lokasi_agen(koordinat_agen)
            return True
        else:
            return False

    def __gerakan(self, gerak):
        kode = 0  # baterai habis
        if self.__cek_baterai():
            clear = lambda: system('clear')
            clear()
            print('\nINFORMASI AGEN')
            print(f'- Aksi Agen: Bergerak ke {gerak.upper()}')
            if self.__gerakan_legal(gerak):
                no_lokasi_agen = self.no_lokasi_agen
                print(f'\t* Agen berhasil bergerak...')
                print(f'\t* No. lokasi Agen skg.\t: L{no_lokasi_agen}')
                print(f'\t* Koordinat lokasi Agen\t: {self.get_koordinat_agen(no_lokasi_agen)}')
                status = self.__lingkungan.get_status(no_lokasi_agen)
                if status == 1:
                    print(f'\t* Status lokasi\t\t: {status} - KOTOR')
                    print(f'\t\t^ Lokasi kotor, lakukan pembersihan...')
                    self.__tindakan(self.__BERSIHKAN, no_lokasi_agen)
                else:
                    print(f'\t* Status lokasi\t\t: {status} - BERSIH')
                print(f'\t* Isi baterai\t\t: {self.__isi_baterai}')
                print(f'\t* Jumlah langkah\t: {self.__jml_langkah}')
                if self.__cek_lokasi_bersih():
                    self.__lingkungan.info_lokasi()
                    print('\n- SELURUH LOKASI TELAH BERSIH DARI KOTORAN :D\n')
                    sys.exit()
                kode = 1  # berhasil bergerak
            else:
                no_lokasi_agen = self.no_lokasi_agen
                print(f'\t* Error: Agen tidak bisa bergerak, terhalang tembok!')
                print(f'\t* No. lokasi Agen\t: L{self.no_lokasi_agen}')
                print(f'\t* Koordinat lokasi Agen\t: {self.get_koordinat_agen(self.no_lokasi_agen)}')
                status = self.__lingkungan.get_status(no_lokasi_agen)
                if status == 1:
                    print(f'\t* Status lokasi\t\t: {status} - KOTOR')
                else:
                    print(f'\t* Status lokasi\t\t: {status} - BERSIH')
                print(f'\t* Isi baterai\t\t: {self.__isi_baterai}')
                print(f'\t* Jumlah langkah\t: {self.__jml_langkah}')
                kode = -1  # terhalang tembok
            self.__lingkungan.info_lokasi()
        else:
            print('\nError: Agen tidak bisa berjalan, kehabisan baterai!!! :(\n')
            sys.exit()
        return kode

    def __tindakan(self, aksi, no_lokasi_agen):
        if aksi == self.__BERSIHKAN:
            self.__set_status_bersih(self.no_lokasi_agen)
        else:
            print('Error: Aksi tidak tersedia!')

    def __cek_lokasi_bersih(self):
        flag = True
        for lokasi in self.__lingkungan.get_lokasi():
            if lokasi[2] == 1:
                flag = False
                break
        return flag

    def __alg_manual(self):
        while (True):
            print('\nINSTRUKSI')
            print('- Gunakan tombol panah KIRI, ATAS, KANAN, dan BAWAH untuk menggerakkan Agen')
            print('- Tekan tombol ESC untuk keluar')
            key = input('\nMasukan perintah: ')
            if key == '\x1b[D':  # tombol panah kiri
                self.__gerakan(self.__KIRI)
            elif key == '\x1b[A':  # tombol panah atas
                self.__gerakan(self.__ATAS)
            elif key == '\x1b[C':  # tombol panah kanan
                self.__gerakan(self.__KANAN)
            elif key == '\x1b[B':  # tombol panah bawah
                self.__gerakan(self.__BAWAH)
            elif key == chr(27):
                break
            else:
                print('Tombol yang anda masukan salah!')

    def __alg_agen_malas(self):
        """ Agen akan bergerak terus sampai lokasi bersih atau habis baterai """
        arah = 'kanan'  # bagian dari problem formulation
        sec = 3
        time.sleep(5)
        while (True):
            if not self.__cek_lokasi_bersih():
                if arah == 'kanan':
                    if self.__gerakan(self.__KANAN) == -1:  # kena dinding!
                        arah = 'kiri'
                        time.sleep(sec)
                        self.__gerakan(self.__BAWAH)
                        time.sleep(sec)
                    else:
                        time.sleep(sec)
                elif arah == 'kiri':
                    if self.__gerakan(self.__KIRI) == -1:  # kena dinding!
                        arah = 'kanan'
                        time.sleep(sec)
                        self.__gerakan(self.__BAWAH)
                        time.sleep(sec)
                    else:
                        time.sleep(sec)

    def __euclidean(self, lokasi_awal, lokasi_akhir):
        x = math.pow((lokasi_awal[0]-lokasi_akhir[0]), 2)
        y = math.pow((lokasi_awal[1]-lokasi_akhir[1]), 2)
        return math.sqrt(x + y)

    def jalan(self, lokasi_awal, lokasi_tujuan):
        sec = 0
        while lokasi_awal != lokasi_tujuan:
            if lokasi_awal[0] != lokasi_tujuan[0]:
                if lokasi_awal[0] < lokasi_tujuan[0]:
                    self.__gerakan(self.__BAWAH)
                    time.sleep(sec)
                    lokasi_awal[0] += 1
                else :
                    self.__gerakan(self.__ATAS)
                    time.sleep(sec)
                    lokasi_awal[0] -= 1
            if lokasi_awal[1] != lokasi_tujuan[1]:
                if lokasi_awal[1] < lokasi_tujuan[1]:
                    self.__gerakan(self.__KANAN)
                    time.sleep(sec)
                    lokasi_awal[1] += 1
                else :
                    self.__gerakan(self.__KIRI)
                    time.sleep(sec)
                    lokasi_awal[1] -= 1

    def alg_agen_cerdas(self):

        sec = 1
        # time.sleep(5)
        # while (True):
        #     if not self.__cek_lokasi_bersih():
        # Ambil Lokasi Sampah
        lokasi_sampah = [lokasi_temp for lokasi_temp in self.__lingkungan.get_lokasi() if lokasi_temp[2] == 1]
        # Hitung Jarak Seluruh Sampah
        jarak_sampah = [self.__euclidean(self.get_koordinat_agen(self.no_lokasi_agen), lokasi_temp) for lokasi_temp in lokasi_sampah]

        jarak_min = min(jarak_sampah)
        index_jarak_min = jarak_sampah.index(jarak_min)

        # Set Lokasi awal dan tujuan (jarak sampah terdekat)
        lokasi_awal = list(self.get_koordinat_agen(self.no_lokasi_agen))
        lokasi_tujuan = (lokasi_sampah[index_jarak_min]).copy()
        lokasi_awal.append(1)

        # print(lokasi_tujuan)
        # lokasi_awal = lokasi_tujuan.copy()
        # print(lokasi_awal)

        # Bergerak dari lokasi awal ke tujuan
        # while lokasi_awal != lokasi_tujuan:
        #     if lokasi_awal[0] != lokasi_tujuan[0]:
        #         if lokasi_awal[0] < lokasi_tujuan[0]:
        #             self.__gerakan(self.__BAWAH)
        #             time.sleep(sec)
        #             lokasi_awal[0] += 1
        #         else :
        #             self.__gerakan(self.__ATAS)
        #             time.sleep(sec)
        #             lokasi_awal[0] -= 1
        #     if lokasi_awal[1] != lokasi_tujuan[1]:
        #         if lokasi_awal[1] < lokasi_tujuan[1]:
        #             self.__gerakan(self.__KANAN)
        #             time.sleep(sec)
        #             lokasi_awal[1] += 1
        #         else :
        #             self.__gerakan(self.__KIRI)
        #             time.sleep(sec)
        #             lokasi_awal[1] -= 1

        return lokasi_tujuan

    def run(self):
        # self.__alg_manual()
        # self.__alg_agen_malas()
        self.__alg_agen_cerdas()
        # self.__ui.run(lokasi_tujuan)
        # self.__ui.run()

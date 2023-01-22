"""
    PROGRAM SIMULASI AGEN PENYEDOT DEBU V.0.0.1
    abdiansah@unsri.ac.id - Agustus 2021
"""

from os import system

from agen import Agen
from lingkungan import Lingkungan
from ui import UI
import random

if __name__ == "__main__":
    """ set sistem """
    clear = lambda: system('cls')  # windows ganti dengan 'cls'
    clear()


    """ set lingkungan """
    baris, kolom, sampah = (5, 5, 10)
    lingkungan = Lingkungan(baris, kolom, sampah)

    """ set dan jalankan agen """
    no_lokasi_agen = 1
    # no_lokasi_agen = random.randint(1, baris * kolom) # lokasi agen random
    agen = Agen(lingkungan, no_lokasi_agen)
    # agen.run()

    """ set UI """
    ui = UI(agen, lingkungan, baris, kolom)
    ui.run()

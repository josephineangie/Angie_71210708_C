class Mobil:
    _merk = ""
    _tipe = ""
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe

    def setmerk(self, merk):
        self._merk = merk

    def settipe(self, tipe):
        self._tipe = tipe

    def setkapasitasBBM(self, kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    def setjenisBahanBakar(self, jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def getmerk(self):
        return self._merk

    def gettipe(self):
        return self._tipe

    def getkapasitasBBM(self):
        return self._kapasitasBBM

    def getjenisBahanBakar(self):
        return self._jenisBahanBakar

    def printInfo(self):
        print("============ INFO ============")
        print("Merk \t\t: " + self.getmerk())
        print("Tipe \t\t: " + self.gettipe())
        print("Bahan Bakar \t: " + str(self.getjenisBahanBakar()))
        print("Kapasitas BBM \t: " + str(self.getkapasitasBBM()))

    def isiBBM(self, harga):
        if self.getkapasitasBBM() is None:
            print("ERROR! Kapasitas BBM atau Jenis bahan Bakar belum di inputkan")
        elif self.getjenisBahanBakar() is None:
            print("ERROR! Kapasitas BBM atau Jenis bahan Bakar belum di inputkan")
        else:
            print("Mengisi " + str(self.getkapasitasBBM()) + " Liter")
            print("Total Harga : Rp" + str(harga * self.getkapasitasBBM()))


if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()

    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setjenisBahanBakar("Bensin")
    mobil2.setkapasitasBBM(20)
    mobil2.printInfo()

    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)

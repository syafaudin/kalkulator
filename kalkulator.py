class Kalkulator:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def penjumlahan(self):
        return self.no1 + self.no2

    def pengurangan(self):
        return self.no1 - self.no2
    
    def perkalian(self):
        return self.no1 * self.no2

    def pembagian(self):
        if self.no2 == 0:
            return "Tidak bisa di bagi 0"
        else:
            return self.no1 / self.no2


no1 = int(input("Masukkan nilai pertama = "))
no2 = int(input("Masukkan nilai kedua = "))

cal = Kalkulator(no1, no2)
print("1. penjumlahan ")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")

pilih = int(input("masukkan pilihan ="))
if pilih == 1:
    print("hasil penjumlahan =", cal.penjumlahan())
elif pilih == 2:
    print("hasil pengurangan =", cal.pengurangan())
elif pilih == 3:
    print("hasil perkalian =", cal.perkalian())
elif pilih == 4:
    print("hasil pembagian =", cal.pembagian())
else:
    print("pilihan kamu tidak terdaftar :)")








class Handphone:
    def __init__(self, ram, kamera, harga):
        self.ram = ram
        self.kamera = kamera
        self.harga = harga

    def mengirim_pesan(self, nomor, pesan):
        print(f"Mengirim pesan ke {nomor}: {pesan}")

    def menelfon(self, nomor):
        print(f"Menelfon {nomor}...")

    def memotret(self):
        print(f"Memotret dengan kamera {self.kamera} MP...")

hp1 = Handphone("8GB", 64, 5000000)
hp2 = Handphone("12GB", 108, 8000000)

print(f"HP1: RAM {hp1.ram}, Kamera {hp1.kamera}MP, Harga Rp{hp1.harga}")
print(f"HP2: RAM {hp2.ram}, Kamera {hp2.kamera}MP, Harga Rp{hp2.harga}")

hp1.mengirim_pesan("08123456789", "Halo, ini HP1!")
hp1.menelfon("08123456789")
hp1.memotret()

hp2.mengirim_pesan("08987654321", "Halo, ini HP2!")
hp2.menelfon("08987654321")
hp2.memotret()
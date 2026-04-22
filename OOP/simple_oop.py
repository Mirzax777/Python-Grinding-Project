class Mobil:
    def __init__(self, brand, color, status=False):
        self.brand = brand
        self.color = color
        self.status = status

    def info(self):
        return f"Mobil {self.brand} berwarna {self.color}"

    def nyalakan(self):
        if self.status:
            print("Mobil", self.brand, self.color, "Sudah Nyala")
        else:
            print("Mobil", self.brand, self.color, "Dinyalakan")
            self.status = True

    def matikan(self):
        if self.status:
            print("Mobil", self.brand, self.color, "Dimatikan")
            self.status = False
        else:
            print("Mobil", self.brand, self.color, "Tidak Nyala")



mobil1 = Mobil("Tokoko", "red")
print(mobil1.color)
print(mobil1.info())
mobil1.nyalakan()

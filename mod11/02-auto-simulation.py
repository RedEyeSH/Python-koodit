from random import randint

class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = 0

    def accelerate(self, nopeuden_muutos: float):
        self.hetkellinen_nopeus += nopeuden_muutos

        if self.hetkellinen_nopeus < 0:
            self.hetkellinen_nopeus = 0

        if self.hetkellinen_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus

    def kulje(self, aika: float):
        self.kuljettu_matka += self.hetkellinen_nopeus * aika

class ElectricCar(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku_kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku_kapasiteetti = akku_kapasiteetti

class GasolineCar(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensa_tilavuus):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensa_tilavuus = bensa_tilavuus

class Kilpailu:
    def __init__(self, nimi, pituus, auto_lista: list):
        self.nimi = nimi
        self.pituus = pituus
        self.auto_lista = auto_lista

    def tunti_kuluu(self):
        for auto in self.auto_lista:
            satunnainen = randint(-10, 15)
            auto.accelerate(satunnainen)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<20} {'Huippinopeus':<20} {'Hetkellinen nopeus':<20} {'Kuljettu matka':<20}")
        for auto in self.auto_lista:
            print(
                f"{auto.rekisteritunnus:<20} {auto.huippunopeus:<20} {auto.hetkellinen_nopeus:<20} {auto.kuljettu_matka:<20}")

    def kilpailu_ohi(self):
        for auto in self.auto_lista:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

# autot = []

# for i in range(1, 11):
#     random_huippunopeus = randint(100, 200)
#     auto = Auto(f"ABC-{i}", random_huippunopeus)
#     autot.append(auto)

# kilpailu = Kilpailu("Auto kilpailu", 8000, autot)

# tunti = 0
# while not kilpailu.kilpailu_ohi():
#     tunti += 1
#     kilpailu.tunti_kuluu()
#     if tunti % 10 == 0:
#         print(f"\nTilanne {tunti} tunnin jälkeen:")
        # kilpailu.tulosta_tilanne()

# for a in autot:
#     if a.kuljettu_matka >= kilpailu.pituus:
#         print(f"\n{a.rekisteritunnus} on voittanut kilpailun! Auto on ajanut {a.kuljettu_matka} km.")
#         break

# print("\nKilpailu on päättynyt!")
# kilpailu.tulosta_tilanne()

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(60)
gasoline_car.accelerate(80)

electric_car.kulje(3)
gasoline_car.kulje(3)

print("Electric car: ")
print(f"Rekisteritunnus: {electric_car.rekisteritunnus}")
print(f"Huippunopeus: {electric_car.huippunopeus} km/h")
print(f"Battery Capacity: {electric_car.akku_kapasiteetti} kWh")
print(f"Kuljettu matka: {electric_car.kuljettu_matka} km\n")

print("Gasoline car: ")
print(f"Rekisteritunnus: {gasoline_car.rekisteritunnus}")
print(f"Huippunopeus: {gasoline_car.huippunopeus} km/h")
print(f"Battery Capacity: {gasoline_car.bensa_tilavuus} l")
print(f"Kuljettu matka: {gasoline_car.kuljettu_matka} km")
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
            self.hetkellinen_nopeus =  self.huippunopeus

    def kulje(self, aika: float):
        self.kuljettu_matka += self.hetkellinen_nopeus * aika

auto = None

autot = []

for i in range(1, 11):
    random_huippunopeus = randint(100, 200)
    auto = Auto(f"ABC-{i}", random_huippunopeus)
    autot.append(auto)

kilpailu = True

while kilpailu:
    for auto in autot:
        satunnainen = randint(-10, 15)
        auto.accelerate(satunnainen)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu = False
            break

for auto in autot:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, hetkellinen nopeus: {auto.hetkellinen_nopeus}, kuljettu matka: {auto.kuljettu_matka}")

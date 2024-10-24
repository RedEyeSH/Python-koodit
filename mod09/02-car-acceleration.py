class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.matka = 0

    def accelerate(self, nopeuden_muutos: int):
        self.hetkellinen_nopeus += nopeuden_muutos

        if self.hetkellinen_nopeus < 0:
            self.hetkellinen_nopeus = 0

        if self.hetkellinen_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus

        print("Tämänhetkinen nopeus:", auto.hetkellinen_nopeus, "km/h")

    def ominaisuudet(self):
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.hetkellinen_nopeus, "km/h")
        print("Kuljettu matka:", self.matka, "km\n")

auto = Auto("ABC-123", 142)
auto.ominaisuudet()

auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)
auto.accelerate(-200)

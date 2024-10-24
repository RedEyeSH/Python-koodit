class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int):
        self. rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.matka = 0

    def ominaisuudet(self):
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.hetkellinen_nopeus, "km/h")
        print("Kuljettu matka:", self.matka, "km")

auto = Auto("ABC-123", 142)
auto.ominaisuudet()

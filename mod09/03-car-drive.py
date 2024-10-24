class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: float, kuljettu_matka: float, nopeus: float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = kuljettu_matka
        self.nopeus = nopeus

    def accelerate(self, nopeuden_muutos: float):
        self.hetkellinen_nopeus += nopeuden_muutos

        if self.hetkellinen_nopeus < 0:
            self.hetkellinen_nopeus = 0

        if self.hetkellinen_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus

    def kulje(self, aika: float):
        self.kuljettu_matka += self.nopeus * aika
        print(f"Kuljetaan {aika} tuntia...\n")
        print(f"Tämänhetkinen nopeus: {self.nopeus} km/h")
        print(f"Tämänhetkinen kuljettu matka: {self.kuljettu_matka} km\n")


auto = Auto("ABC-123", 142, 2000, 60)

print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
print(f"Tämänhetkinen kuljettu matka: {auto.kuljettu_matka} km\n")

auto.kulje(1.5)
auto.kulje(2)


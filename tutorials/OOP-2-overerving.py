"""
Tutorial Object-Oriented-Programming OOP

Deel 1: Inheritance of overerving
"""

from datetime import datetime

class Persoon:
    def __init__(self, naam, voornaam, geboortedatum, lengte, gewicht):
        self.naam = naam
        self.voornaam = voornaam
        self.geboortedatum = datetime.strptime(geboortedatum, "%Y-%m-%d")
        self.lengte = lengte
        self.gewicht = gewicht

    def volledigenaam(self):
        return self.voornaam + " " + self.naam

    def leeftijd(self):
        leeftijd_delta = datetime.now() - self.geboortedatum
        return leeftijd_delta // 365    #ongeveer

    def BMI(self):
        return int((self.gewicht*10000)/(self.lengte*self.lengte))

class Leerling(Persoon):
    def __init__(self, naam, voornaam, geboortedatum, lengte, gewicht, klas, klasnr):
        Persoon.__init__(self, naam, voornaam, geboortedatum, lengte, gewicht) # parameter self niet vergeten hier!
        self.klas = klas
        self.klasnr = klasnr
        self.afwezigheden = 0

    def NieuweAfwezigheid(self, aantal_dagen):
        self.afwezigheden += 1
        if aantal_dagen > 3:
            self.afwezigheden += aantal_dagen - 3

Robin = Leerling("Berger", "Robin", "2006-01-12", 182, 55,"6WEWI",2)
Robin.NieuweAfwezigheid(2)
Robin.NieuweAfwezigheid(5)

print("Fiche van", Robin.volledigenaam())
print(" - naam:", Robin.volledigenaam())
print(" - klas:", Robin.klas)
print(" - klasnr:", Robin.klasnr)
print(" - afwezigheden:", Robin.afwezigheden)


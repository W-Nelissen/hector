"""
Tutorial Object-Oriented-Programming OOP

Deel 1: Objecten maken
"""
# Stel dat je 20 personen hebt en die hebben allemaal
#    een voornaam
#    een achternaam
#    een geboortedatum
#    een lengte
#    en een gewicht hebben
# en je moet dat gestructureerd bijhouden
#
# Oplossing: Definieer een template van wat een persoon is
# Die template noemen we een class

#import om met datums te kunnen werken
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


Robin = Persoon("Berger", "Robin", "2006-01-12", 182, 55)		# zonder self
Batman = Persoon("Wayne", "Bruce", "2016-02-23", 175, 75)		# zonder self

print("---------------------------------------------------")
print("BMI van", Robin.volledigenaam(), "is", Robin.BMI())
print("---------------------------------------------------")
print("Fiche van", Batman.volledigenaam())
print(" - naam:", Batman.naam)
print(" - voornaam:", Batman.voornaam)
print(" - verjaardag:", Batman.geboortedatum.strftime("%d-%b-%Y"))
print(" - lengte: ", Batman.lengte)
print(" - gewicht: ", Batman.gewicht)
print(" - BMI:", Batman.BMI())
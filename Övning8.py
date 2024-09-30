class Kalkylator:
    def __init__(self) -> None:
        self._aktuella_värde = 0

    def get_värde(self):
        return self._aktuella_värde

    def addera(self, värde):
        self._aktuella_värde += värde
        return self._aktuella_värde 
    
    def subtrahera(self, värde):
        self._aktuella_värde -= värde
        return self._aktuella_värde
    
    def multiplicera(self, värde):
        self._aktuella_värde *= värde
        return self._aktuella_värde
    
    def dividera(self, värde):
        self._aktuella_värde /= värde
        return self._aktuella_värde
    
kalkylator = Kalkylator()

print(kalkylator.addera(6))
print(kalkylator.multiplicera(3))
print(kalkylator.subtrahera(8))
print(kalkylator.dividera(2))
print(kalkylator.get_värde())

class Person:   
    def __init__(self, namn, personnummer, ålder) -> None:
        self.namn = namn
        self.ålder = ålder
        self._personnummer = personnummer
        
    @property
    def personnummer(self):
        return self._personnummer
    
    @property
    def ålder(self):
        return self._ålder
    
    @ålder.setter
    def ålder(self, ny_ålder):
        if 0<= ny_ålder <= 123:
            self._ålder = ny_ålder
        else:
            raise ValueError("Ålder måste vara en integer mellan 0 och 123")


p = Person("Sebastian", "18890101-2823", 23)
print(p.ålder)
p.ålder = 99
print(p.ålder)
# p.ålder = 200 # <-- kommer krascha
# new_p = Person("Kalle","18888888-8888", -10) # <-- kommer krascha
# print(new_p.ålder)
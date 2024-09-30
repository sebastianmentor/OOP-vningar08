class Person:
    def __init__(self, förnamn, efternamn, ålder) -> None:
        self._förnamn = förnamn
        self._efternamn = efternamn
        self._ålder = ålder

    def get_förnamn(self):
        return self._förnamn
    
    def get_efternamn(self):
        return self._efternamn
    
    def get_ålder(self):
        return self._ålder
    
    def set_förnamn(self, förnamn):
        self._förnamn = förnamn
    
    def set_efternamn(self, efternamn):
        self._efternamn = efternamn

    def set_ålder(self, ålder):
        self._ålder = ålder


def skriv_ut_info(person):
    print(person.get_förnamn(), person.get_efternamn(), person.get_ålder())

anna = Person("Anna", "Lundin", 22)
kalle = Person("Kalle", "Anka", 33)

skriv_ut_info(anna)
skriv_ut_info(kalle)

anna.set_förnamn("ANNA")
anna.set_efternamn("LUNDIN")
anna.set_ålder(23)

kalle.set_förnamn("KALLE")
kalle.set_efternamn("ANKA")
kalle.set_ålder(55)

skriv_ut_info(anna)
skriv_ut_info(kalle)
class Bankkonto:
    
    def __init__(self, kontonummer, saldo=0) -> None:
        self._kontonummer = kontonummer
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo
    
    def insättning(self, insättning):
        if insättning > 0:
            self._saldo += insättning
        else:
            print("Kan inte sätta in negativa pengar")

    def uttag(self, uttag):
        if uttag < 0:
            print("Kan inte ta ut negativa pengar")
        elif self._saldo < uttag:
            print("Otillräckligt saldo")
        else:
            self._saldo -= uttag


konto1 = Bankkonto("1234")
konto2 = Bankkonto("5555")

konto1.insättning(100)
konto2.insättning(-10)

konto1.uttag(101)
konto2.uttag(0)

print(konto1.get_saldo())
print(konto2.get_saldo())
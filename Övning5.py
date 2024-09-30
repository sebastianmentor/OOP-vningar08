import random

class Tärning:
    def __init__(self, antal_sidor = 6) -> None:
        self._antal_sidor = antal_sidor

    def get_antal_sidor(self):
        return self._antal_sidor
    
    def kasta(self):
        return random.randint(1,self._antal_sidor)
    

tärning1 = Tärning()
tärning2 = Tärning()
tärning3 = Tärning()
tärning4 = Tärning()
tärning5 = Tärning()

yatsy_tärningar = (tärning1, tärning2, tärning3, tärning4, tärning5) 

def kasta_hand(hand):
    for id, tärning in enumerate(hand, start=1):
        print(f"Tärning {id} rullade {tärning.kasta()}")

kasta_hand(hand=yatsy_tärningar)
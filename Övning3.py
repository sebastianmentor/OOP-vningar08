class Produkt:
    def __init__(self, produktID, namn, pris) -> None:
        self._produkt_id = produktID
        self._namn = namn
        self._pris = pris

    
    def get_produktID(self):
        return self._produkt_id
    
    def get_namn(self):
        return self._namn
    
    def get_pris(self):
        return self._pris
    
    def set_produkt_id(self, id):
        self._produkt_id = id

    def set_namn(self, namn):
        self._namn = namn

    def set_pris(self, pris):
        if pris < 0:
            self._pris = 0
        else: 
            self._pris = pris


bröd = Produkt(1234, "Bröd", 24.9)
smör = Produkt(5555, "Smör", 53.5)
ost = Produkt(8888, "Ost", 120)

smörgås = (bröd, smör, ost)

kostnad = 0
for ingridiens in smörgås:
    kostnad += ingridiens.get_pris()

print(f"Du behöver handla varor för {kostnad} för att kunna göra en smörgås!")
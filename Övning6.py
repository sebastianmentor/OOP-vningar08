class Bibliotek:
    def __init__(self, namn) -> None:
        self._namn = namn
        self._böcker = []

    def lägg_till_böcker(self, bok):
        self._böcker.append(bok)

    def lista_alla_böcker(self):
        for bok in self._böcker:
            print(f"{bok}")    


bok1 = "Titel 1"
bok2 = "Titel 2"
bok3 = "Titel 3"

bibliotek = Bibliotek("Västerås Stadsbibliotek")

bibliotek.lägg_till_böcker(bok1)
bibliotek.lägg_till_böcker(bok2)
bibliotek.lägg_till_böcker(bok3)

bibliotek.lista_alla_böcker()
class TV:
    KANALER = [1,2,3,4,5,6,7,8,9,10]
    VOLYM_MIN = 0
    VOLYM_MAX = 100

    def __init__(self, märke, modell) -> None:
        self._märke = märke
        self._modell = modell
        self._kanal = 1
        self._volym = 10

    def get_kanal(self):
        return self._kanal
    
    def get_volym(self):
        return self._volym

    def byt_kanal(self, kanal):
        if kanal in self.KANALER:
            self._kanal = kanal

    def öka_volymen(self, ökning=1):
        if ökning < 0: return
        self._ändra_volymen(1,ökning)

    def minska_volymen(self, minskning=1):
        if minskning < 0: return
        self._ändra_volymen(-1, minskning)


    def _ändra_volymen(self, ändring, värde):
        ny_volym = self._volym + ändring*värde

        if ny_volym > self.VOLYM_MAX: 
            self._volym = self.VOLYM_MAX

        elif ny_volym < self.VOLYM_MIN: 
            self._volym = self.VOLYM_MIN

        else:
            self._volym = ny_volym


tv1 = TV("Samsung", "Frame 2")
tv1.byt_kanal(6)
tv1.öka_volymen(200)
print(tv1.get_kanal())
print(tv1.get_volym())

tv1.minska_volymen()
tv1.minska_volymen()
tv1.byt_kanal(200)

print(tv1.get_volym())
print(tv1.get_kanal())

class TV:
    KANALER = [1,2,3,4,5,6,7,8,9,10]
    VOLYM_MIN = 0
    VOLYM_MAX = 100

    def __init__(self, märke, modell) -> None:
        self._märke = märke
        self._modell = modell
        self._kanal = 1
        self._volym = 10

    def byt_kanal(self, kanal):
        if kanal in self.KANALER:
            self._kanal = kanal

    def öka_volymen(self, ökning=1):

        if ökning < 0: return

        ny_volym = self._volym + ökning

        if ny_volym > self.VOLYM_MAX: 
            self._volym = self.VOLYM_MAX
        else:
            self._volym = ny_volym

    def minska_volymen(self, minskning=1):

        if minskning < 0: return

        ny_volym = self._volym - minskning

        if ny_volym < self.VOLYM_MIN: 
            self._volym = self.VOLYM_MIN
        else:
            self._volym = ny_volym

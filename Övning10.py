class Klocka:
    def __init__(self) -> None:
        self._timmar = 0
        self._minuter = 0
        self._sekunder = 0

    def set_timmar(self, timmar):
        if isinstance(timmar, int) and 0 <= timmar <= 23:
            self._timmar = timmar

    def set_minuter(self, minuter):
        if isinstance(minuter, int) and 0 <= minuter <= 59:
            self._minuter = minuter

    def set_sekunder(self, sekunder):
        if isinstance(sekunder, int) and 0 <= self._sekunder <= 59:
            self._sekunder = sekunder

    def tick(self):
        self._tick_sekunder()

    def _tick_timmar(self):
        if self._timmar == 23: 
            self._timmar = 0
        else:
            self._timmar += 1
            
    def _tick_minuter(self):
        if self._minuter == 59:
            self._tick_timmar()
        
        self._minuter = (self._minuter + 1) % 60

    def _tick_sekunder(self):
        if self._sekunder == 59:
            self._tick_minuter()
        
        self._sekunder = (self._sekunder + 1) % 60

    def __str__(self) -> str:
        return f"{self._timmar:02}:{self._minuter:02}:{self._sekunder:02}"



klocka = Klocka()

for _ in range(200*60):
    klocka.tick()

print(klocka)
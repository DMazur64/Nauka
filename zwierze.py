class Zwierze:
    def __init__ (self, wiek, typ, gdzie_zyje):
        self.wiek = wiek
        self.typ = typ
        self.gdzie_zyje = gdzie_zyje
    def say (self):
        return f"To zwierze to {self.typ}, ma {self.wiek} lat i zyje w {self.gdzie_zyje}"
class Ptak(Zwierze):
    def __init__(self, wiek, typ, gdzie_zyje, barwa):
        super().__init__ (wiek, typ, gdzie_zyje)
        self.barwa = barwa
    def say(self):
        return f"{super().say()} i ma {self.barwa} kolor"
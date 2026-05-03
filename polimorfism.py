# Polimorfism


class Forma:
    def arie(self)->int:
        return 0


class Patrat(Forma):
    def __init__(self, latura: int):
        super().__init__()
        self.latura: int = latura

    def arie(self)->int:
        return self.latura * self.latura

class Cerc(Forma):
    def __init__(self, raza: int):
        super().__init__()
        self.raza: int = raza
    
    def arie(self)->float:
        return 3.14 * self.raza ** 2

obiecte: list = [Patrat(4), Cerc(5)]

for elem in obiecte:
    print(elem.arie())
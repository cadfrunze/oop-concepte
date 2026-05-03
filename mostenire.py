
# Mostenire


class Animal:
    """Clasa mama"""
    def __init__(self, nume:str, varsta:int):
        self.nume: str = nume
        self.varsta: int = varsta
    
    def descriere(self)->None:
        print(f"Numele animalului este {self.nume} și are {self.varsta} ani")


class Caine(Animal):
    """Va mosteni clasa Animal"""
    def __init__(self, nume: str, varsta: int, rasa: str):
        super().__init__(nume, varsta)
        self.rasa: str = rasa
    
    def latra(self)->None:
        print(f"{self.nume} latra: Ham ham!")


rex: Caine = Caine(varsta=3, nume="rex", rasa="ciobanesc")
rex.descriere()
rex.latra()

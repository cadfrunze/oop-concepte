from abc import ABC, abstractmethod

# Abstractizare


class Vehicul(ABC):

    def __init__(self, marca: str):
        super().__init__()
        self.marca: str = marca

    @abstractmethod
    def descriere_vehicul(self):
        ...


class Masina(Vehicul):

    def __init__(self, marca, nr_usi: int):
        super().__init__(marca)
        self.nr_usi: int = nr_usi

    def descriere_vehicul(self):
        print(f"Masina marca {self.marca} are {self.nr_usi} usi")

class Motocicleta(Vehicul):

    def __init__(self, marca, tip: str):
        super().__init__(marca)
        self.tip: str = tip
    
    def descriere_vehicul(self):
        print(f"Motocicleta marca {self.marca} este de tip {self.tip}")


Masina("bmw", 4).descriere_vehicul()
Motocicleta("yamaha", "sport").descriere_vehicul()

# Incapsulare



class ContBancar:

    def __init__(self, sold: float):
        self.__sold: float = sold
    
    def get_sold(self)->float:
        return self.__sold
    
    def set_sold(self, suma: float)->None:
        if suma > 0:
            self.__sold += suma
    
    def descriere(self)->None:
        print(f"Soldul contului este: {self.__sold} lei")
    

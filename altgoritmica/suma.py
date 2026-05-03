# Exercițiul 1 – Ușor
# Scrie o funcție care primește o listă de numere și returnează suma elementelor pare:
# lista = [1, 2, 3, 4, 5, 6]
from typing import List

def suma(lista: List[int])->int:
    suma: int = 0
    for i in lista:
        if i % 2 == 0:
            suma += i
    return suma

print(suma([1, 2, 3, 4, 5, 6]))


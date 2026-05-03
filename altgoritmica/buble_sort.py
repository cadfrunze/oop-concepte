# Lista: [5, 3, 1, 4, 2]
from typing import List

def buble_sort(lista: List[int])->List[int]:
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[i]:
                aux: int = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

print(buble_sort([5, 3, 1, 4, 2]))


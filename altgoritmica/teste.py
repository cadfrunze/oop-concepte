from typing import List, Dict

# lista = [3, 7, 1, 9, 4]

# num_prov: int = 0

# for elem in lista:
#     if elem > num_prov:
#         num_prov = elem

# print(num_prov)

#"radar"  # True
#"python" # False
#"coc"    # True

# def palidrom(cuvant: str)->bool:
#     if cuvant == cuvant[::-1]:
#         return True
#     return False

# def elemente_unice(lista_elem: List[int])-> List[int]:
#     lista_finala: List[int] = []
#     for i in lista_elem:
#         if lista_elem.count(i) >= 1 and i not in lista_finala:
#             lista_finala.append(i)
#     return lista_finala

# print(elemente_unice([1, 3, 2, 1, 5, 3, 4]))

def text_contor(text: str)->Dict[str, int]:
    rezultat: Dict[str, int] = {}
    for lit in text:
        rezultat[lit] = text.count(lit)
    return rezultat

print(text_contor("banana"))


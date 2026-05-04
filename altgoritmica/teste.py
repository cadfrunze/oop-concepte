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

# def text_contor(text: str)->Dict[str, int]:
#     rezultat: Dict[str, int] = {}
#     for lit in text:
#         rezultat[lit] = text.count(lit)
#     return rezultat

# print(text_contor("banana"))

# Exercițiul 5 – Mediu
# Scrie o funcție care primește o listă de numere și returnează al doilea cel mai mare element:
# lista = [3, 7, 1, 9, 4]
#
# def second_num(list_num: List[int])->int:
#     max_num: int = list_num[0]
#     sec_num: int = list_num[0]
#     for num in list_num:
#         if num > max_num:
#             max_num = num
#     for num1 in list_num:
#         if num1 > sec_num and sec_num < max_num and num1 < max_num:
#             sec_num = num1
#     return sec_num

# print(second_num([3, 7, 1, 9, 4]))


# Exercițiul 6 – Mediu
# Scrie o funcție care primește un string și returnează primul caracter care nu se repetă:
# pythontext = "aabbcde"
# rezultat: "c"  ← primul caracter care apare o singură dată

# def first_char(word: str)->str:
#     litera: str = ""
#     for lit in word:
#         if word.count(lit) == 1:
#             litera = lit
#             break
#     return litera
# print(first_char("aabbcde"))

# Exercițiul 7 – Mediu/Greu
# Scrie o funcție care verifică dacă o listă este sortată crescător:
# python[1, 2, 3, 4, 5]  # True
# [1, 3, 2, 4, 5]  # False

# def sortted_list(brut_list: List[int])->bool:
#     for i in range(len(brut_list)):
#         if i == (len(brut_list) - 1):
#             return True
#         elif (brut_list[i]) >= brut_list[i + 1]:
#             return False

# print(sortted_list([1, 2, 3, 4, 5]))
# print(sortted_list([1, 3, 2, 4, 5]))

# Exercițiul 8 – Mediu
# Scrie o funcție care primește o listă de cuvinte și returnează cuvântul cel mai lung:
# pythoncuvinte = ["ana", "calculator", "masa", "televizor"]
# rezultat: "calculator"

# def big_word(words_list: List[str])-> str:
#     big_word: str = words_list[0]
#     for word in words_list:
#         if len(word) > len(big_word):
#             big_word = word
#     return big_word

# print(big_word(["ana", "calculator", "masa", "televizor"]))

# Exercițiul 9 – Greu
# Scrie o funcție care primește un număr și returnează dacă este prim:
# python7   # True  ← divizibil doar cu 1 și 7
# 10  # False ← divizibil cu 2 și 5
# 2   # True

# def prime_number(number: int)->bool:
#     if number < 2:
#         return False
#     for num in range(2, number):
#         if number % num == 0:
#             return False
#     return True

# print(prime_number(7))

# Exercițiul 10 – Greu
# Scrie o funcție care primește o listă de numere și returnează numerele prime din listă:
# pythonlista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # rezultat: [2, 3, 5, 7, 11]
def prime_numbers(numbers: List[int])->List[int]:
    final_list: List[int] = []
    for number in numbers:
        if number < 2:
            pass
        elif number == 2:
            final_list.append(number)
        else:
            for num in range(2, number):
                if number % num == 0:
                   break
                elif num == number - 1 and number not in final_list:
                    final_list.append(number)
                    
    return final_list

print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


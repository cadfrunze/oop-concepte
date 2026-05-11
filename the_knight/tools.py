from typing import List, Any, Tuple, Dict
import random as rd
from prettytable import PrettyTable





def __add_choice(len_seg: int)->int:
    if len_seg <= 3:
        return  rd.randint(1, 2)
    elif len_seg > 3 and len_seg <= 7:
        return rd.randint(2, 4)
    return rd.randint(3, 5)
    







def make_tabel(nr_col: int, nr_raw: int)->List[int]:
        choice: int
        index: int
        final_list: List[int] = []
        segment_list: List[int] = []
        for _ in range(nr_raw):
            segment_list = []
            for _  in range(nr_col):
                segment_list.append(0)
            final_list.append(segment_list)

        for seg in final_list:
             choice: int = __add_choice(len(seg))
             for _ in range(choice):
                index: int = rd.randint(0, len(seg) - 1)
                seg[index] = -1
        final_list[0][0] = 0
        final_list[-1][-1] = 2
        return final_list


def draw_table(tabel: list)->PrettyTable:
    draw_schema: PrettyTable = PrettyTable()
    with open(r'char.txt', 'r') as char:
          char_str: str = char.readline()
    title_col: List[str] = [char_str[i].upper() for i in range(len(tabel[0]))]
    title_col.insert(0, 'IDX')
    draw_schema.field_names = title_col
    for i in range(len(tabel)):
        tabel[i].insert(0, i+1)
        draw_schema.add_row(tabel[i])
    draw_schema.align = 'c'
    return draw_schema



print(draw_table(make_tabel(5, 5)))
        


                  
                  

                  
            
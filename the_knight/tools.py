import random as rd
from prettytable import PrettyTable





def __add_choice(len_seg: int)->int:
    if len_seg <= 3:
        return  rd.randint(1, 2)
    elif len_seg > 3 and len_seg <= 7:
        return rd.randint(2, 4)
    return rd.randint(3, 5)
    







def make_tabel(nr_col: int, nr_raw: int)->list[int]:
    choice: int
    index: int
    final_list: list[int] = []
    segment_list: list[int] = []
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
    # return [
    #     [ 0, 0,-1],
    #     [0, 0, -1],
    #     [-1, 0, 2]
    # ]




def draw_table(tabel: list, raspuns: bool=False)->PrettyTable:
    draw_schema: PrettyTable = PrettyTable()
    with open(r'char.txt', 'r') as char:
          char_str: str = char.readline()
    title_col: list[str] = [char_str[i].upper() for i in range(len(tabel[0]))]
    title_col.insert(0, 'IDX')
    draw_schema.field_names = title_col
    for i in range(len(tabel)):
        row_copy = tabel[i].copy()  # copie!
        row_copy.insert(0, i)
        draw_schema.add_row(row_copy)
    draw_schema.align = 'c'
    if raspuns == False:
         with open("draw_firtst_table.txt", "w") as draw_table:
            draw_table.write(f"Primul tabel pentru verificare\n{str(draw_schema)}")
    else:
        with open("draw_last_table.txt", "w") as draw_table:
            draw_table.write(f"Raspuns\n{str(draw_schema)}")
    return draw_schema



# def correct_table(tabel: list[int | str], mark: str, raw: int, col: int)->None:
#         for i in range(len(tabel[raw])):
#             for j in range(col, len(tabel)):
#                 if tabel[i][j] == mark:
#                     tabel[i][j] = 0


        


                  
                  

                  
            
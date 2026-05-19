from tools import make_tabel, draw_table

MARK_CELL: str = "*"

class Knight:

    def __init__(self):
        
        self.total_coordonate: list[tuple[int, int]] = [] # tuple[0] = rand, tuple[1] = coloana
        self.coordonate_bune: list[tuple[int, int]] = []
        self.current_pos : dict[str, int] = {
                                    'x': 0, 
                                    'y': 0
                                }


    def step_by_step(self, tabel: list[int | str])->str:
        pos_x: int = 0
        pos_y: int = 0
        while True:
            if (pos_y > len(tabel[0]) - 1): return 'ratacit'
            elif tabel[pos_x][pos_y] == 0:
                tabel[pos_x][pos_y] = MARK_CELL
                try:
                    tabel[pos_x + 1]
                except IndexError:
                    try:
                        tabel[pos_x][pos_y]
                    except IndexError: return 'ratacit'
                    else: 
                        pos_y += 1
                else: 
                    # if tabel[pos_x + 1][pos_y] == -1 and tabel[pos_x][pos_y] == -1: return 'ratacit'
                    if tabel[pos_x + 1][pos_y] == 0:
                        pos_x += 1
                    elif tabel[pos_x + 1][pos_y] == 2: return 'gasit'
                    else: 
                        pos_y += 1
                        pos_x = 0
            
            elif tabel[pos_x][pos_y] == -1: return 'ratacit'
            elif tabel[pos_x][pos_y] == 2: return 'gasit'
                        










class Tabela:
    def __init__(self, nr_col:int, nr_raw:int):
        self.nr_col : int = nr_col
        self.nr_raw: int  = nr_raw
        self.tabel: list[int] = make_tabel(self.nr_col, self.nr_raw)
        print(self.tabel)
        self.deseneaza_tabela(False)
    
    def deseneaza_tabela(self, raspuns: bool)->None:
        tabel_draw = self.tabel
        draw_table(tabel_draw, raspuns)


    



# tabel : Tabela = Tabela(3, 3)
# cavaler: Knight = Knight()

# print(cavaler.step_by_step(tabel.tabel))
# print(tabel.tabel)





    

    

    

        
        




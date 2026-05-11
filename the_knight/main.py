from typing import List, Any
from model import Knight
import os
import time

tabel: List[int | str] = [[0, 0, -1], [-1, 0, -1], [-1, 0, 2]]

cavalerul: Knight = Knight()

def afiseaza_tabel()->None:
    for elem in tabel:
        print(elem)

# afiseaza_tabel()

def step(x: int, y: int)-> None:
     for x in range(len(tabel[y])):
         print(tabel[y][x])


step(cavalerul.current_pos['x'], cavalerul.current_pos['y'])
# afiseaza_tabel()
time.sleep(1)
    
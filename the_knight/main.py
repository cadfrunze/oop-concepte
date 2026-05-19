from model import Knight, Tabela
import os
import time


NR_COL: int = 3
NR_RAW: int = 3


tabela: Tabela = Tabela(NR_COL, NR_RAW)
cavalerul: Knight = Knight()


tabela.deseneaza_tabela(False)
print(cavalerul.step_by_step(tabela.tabel))
print(tabela.tabel)
tabela.deseneaza_tabela(True)


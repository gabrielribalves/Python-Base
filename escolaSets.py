#!/usr/bin/env python
"""Show report of children by lessons

Print list of children grouped by class
"""

__version__ = "0.1.0"

sala1 = ["Michael", "Francisco", "Josemaria", "Joana D'arc", "Tomas"]
sala2 = ["Gabriel", "Pedro", "Lucas", "Abraão", "Jose", "Maria"]

aula_teologia = ["Michael", "Abraão", "Gabriel", "Tomas", "Pedro"]
aula_filosofia = ["Francisco", "Tomas", "Maria", "Lucas"]
aula_fisiculturismo = ["Michael", "Jose", "Josemaria", "Joana D'arc"]

atividades = [
    ("Teologia",aula_teologia),
    ("Filosofia",aula_filosofia),
    ("Fisiculturismo",aula_fisiculturismo)
]
for nome_aula, atividade in atividades:
    aula_sala1 = set(atividade) & set(sala1)
    aula_sala2 = set(atividade).intersection(sala2)

    print(nome_aula + ": sala1 ", aula_sala1)
    print(nome_aula + ": sala2 ", aula_sala2)

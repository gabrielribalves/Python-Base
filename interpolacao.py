#!/user/bin/env python
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]

path = os.curdir

filepathTmpl = os.path.join(path, "email_tmpl.txt")

# print(email_tmpl)

filepathEmail = os.path.join(path, "emails.txt")
clientes = []
for line in open(filepathEmail):
    #TODO: Substituir por list comprehension
    name, email =line.split(",")
    
    print("-"*50)
    print(
        open(filepathTmpl).read()
        % {
            "name": name,
            "product": "caneta",
            "text": "Escreve bem",
            "link":"http//canetaslegais.com",
            "quantity": 1,
            "price": 50.5,
        }
    )
    print("email ", email)
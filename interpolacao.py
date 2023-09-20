#!/user/bin/env python
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.1.1"

import sys
import os
import smtplib

from email.mime.text import MIMEText

arguments = sys.argv[1:]

path = os.curdir

filepathTmpl = os.path.join(path, "email_tmpl.txt")

# print(email_tmpl)

filepathEmail = os.path.join(path, "emails.txt")
clientes = []

with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepathEmail):
        # TODO: Substituir por list comprehension
        name, email = line.split(",")
        text = (open(filepathTmpl).read()
            % {
                "name": name,
                "product": "caneta",
                "text": "Escreve bem",
                "link": "http//canetaslegais.com",
                "quantity": 1,
                "price": 50.5,
            })
        from_ = "gabriel.ribalves@gmail.com"
        to = ", ".join([email])

        msg = MIMEText(text)
        msg["Subject"] = "Compre mais"
        msg["From"] = from_
        msg["To"] = to

        server.sendmail(from_, to, msg.as_string())
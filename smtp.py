"""Exemplo de envio de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "gabriel.ribalves@gmail.com"
TO = ["lauryn.souza13@gmail.com", "bieldestroy@gmail.com"]
SUBJECT = "Teste de e-mail automático via Python"
TEXT = """\
Teste de um e-mail automático via <b>Python</b> ❤
"""

msg = f"""\
From:  {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(user="1695236678", password="6060fe62d47793224c8b9dc964f1f8c8")
    server.sendmail(FROM, TO, msg.encode("utf-8"))
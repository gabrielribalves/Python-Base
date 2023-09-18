#!/usr/bin/env python3
"""Calculadora infix."""

import logging
import os

logLevel = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("gab", logLevel)

ch = logging.StreamHandler()
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s " 
    "l:%(lineno)d f:%(filename)s %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

log.debug("Mensagem pro dev")
log.info("Mensagem geral")
log.warning("Aviso sem erro")
log.error("Erro mesmo")
log.critical("Erro geral")


print("-----")

# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.error("Deu erro %s", str(e))
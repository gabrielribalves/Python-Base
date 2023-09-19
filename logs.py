#!/usr/bin/env python3
"""Calculadora infix."""

import logging
import os
from logging import handlers

logLevel = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("gab", logLevel)
# ch = logging.StreamHandler()
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=10**6,
    backupCount=10
)
fh.setLevel(logLevel)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s " 
    "l:%(lineno)d f:%(filename)s %(message)s"
)
fh.setFormatter(fmt)
log.addHandler(fh)

log.debug("Mensagem pro dev")
log.info("Mensagem geral")
log.warning("Aviso sem erro")
log.error("Erro mesmo")
log.critical("Erro geral")


# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.error("Deu erro %s", str(e))
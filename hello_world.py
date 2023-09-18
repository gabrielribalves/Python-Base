#!/usr/bin/python
"""Hello World multi language

The "Hello World" change by the user's language.

Usage:
The environment variable LANG need to be configured:
    export LANG=pt-BR

Execution:

    python3 hello_world
    or
    ./hello_world
"""
#source .venv/bin/activate
__version__ = "0.0.1"
__author__ = "Gabrier"
__license__ = "Unlicense"

import os
import sys
import logging

logLevel = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("gab", logLevel)

ch = logging.StreamHandler()
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s " 
    "l:%(lineno)d f:%(filename)s %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)  

arguments = {
    "lang": None, 
    "count": 1
}


for arg in sys.argv[1:]:
    #TODO: Tratar value error
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "Please, put `=`. You passed %s. try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("invalid argument: ", key)
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO: Usar repedição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "pt_BR": "Eae mundo",
    "it_IT": "Ciao, Mondo",
    "en_US": "Hello, world",
}

#message = msg.get(current_language, msg["en_US"])

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[Error] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)


print(message * int(arguments["count"]))
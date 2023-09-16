#!/usr/bin/python
"""Hello World multi language

The "Hello World" change by the user's language.

Usage:
The environment variable LANG need to be configured:
    export LANG=pt-BR

Execution:

    python3 first.py
    or
    ./first.py
"""
#source .venv/bin/activate
__version__ = "0.0.1"
__author__ = "Gabrier"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = ""

if current_language == "pt_BR":
    msg = "Eae mundo"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
elif current_language == "en_US":
    msg = "Hello, world"

print(msg)
print(current_language[:5])


teste = "🤬"
teste.encode("utf-8")
teste_encoded = teste.encode("utf-8")
teste_encoded.decode()
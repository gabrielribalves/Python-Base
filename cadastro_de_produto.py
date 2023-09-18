#!/usr/bin/env python
"""Product register"""
__version__ = "0.1.0"

product = {
    "name": "Caneta",
    "colors": ("azul", "branco"),
    "price": 3.23,
    "dimension_high": {
        "hight":12.5,
        "width": 0.9
    },
    "in_stock": True,
    "code": 4652,
    "codebar": None
}
testeDic = "name"
compra  = ("Bruno", product["name"], 3)

print(product[testeDic])
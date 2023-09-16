email = """
... Eae, %(nome)s
... Tem interesse em comprar %(produdo)s?
... Preço promocional %(preco).2f
... """

clientes = ["Maria","Joao", "Gabriel"]

for cliente in clientes:
    print(email % {"nome": cliente, "produdo": "Azul Canetal", "preco": 47.9})


msg = "Ola, {} você é o player {:02d} com {} pontos"
msg.format("Gabriel", 3, 987.3)
"{:-^11}".format("Gabriel")


array = [2,654,0,351,]
array.insert()
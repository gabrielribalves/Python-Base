import os
# import sys

clientName = input("Digite seu nome: ")
chosenCode = input("Digite o código do quarto: ")
days = int(input("Digite os dias: "))

dirPath = os.curdir
quartosFilePath = os.path.join(dirPath, "quartos.txt")
reservarFilePath = os.path.join(dirPath, "reservar.txt")

for room in open(quartosFilePath):
    roomCode, roomName, price = room.split(",")
    if roomCode == chosenCode:
        fullPrice = days * int(price)
        break

flgReserved = False
for reserv in open(reservarFilePath):
    reservName, reservCode, reservDays = reserv.split(",")
    if reservCode == chosenCode:
        flgReserved = True
        break

if flgReserved:
    print("O quarto está reservado 😪❌")
else:
    file_ = open(reservarFilePath, 'a')
    file_.write(f"{clientName},{chosenCode},{days}\n")
    print("O preço total é: ", fullPrice)
    print("O seu quarto foi reservado 😀✅")
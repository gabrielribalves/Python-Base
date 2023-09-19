while True:
    txt = input("Digite uma ou mais palavras(pressione enter para sair): ")
    if txt == "":
        break
    newTxt = ""
    vowels = "aeiou"
    for letter in txt:
        if letter.lower() in vowels:
            newTxt += letter * 2
        else:
            newTxt += letter
    print(newTxt)
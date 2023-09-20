names = ["Gab", "Lau", "Luana", "Marcelo", "Leonardo"]

def startsWithL(text):
    return text[0].lower() == "l"

print(*list(filter(lambda names: names[0].lower() == "l" , names)))
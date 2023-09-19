temperature = int(input("Qual é a temperatura: "))
moisture = int(input("Nível de umidade: "))

if temperature > 45:
    print("ALERTA! Calor extreme")
elif (temperature*3) >= moisture:
    print("Perigo de calor úmido")
elif temperature >= 10 and temperature <= 30:
    print("Normal")
elif  temperature >= 0 and temperature <= 10:
    print("Frio")
elif temperature < 0:
    print("Frio extremo")

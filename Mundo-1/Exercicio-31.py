d = float(input("Digite a distância da sua viagem: "))

if d <=200:
    p = d*0.50
    print(f"Sua passagem saira por R${p}")
else:
    p = d*0.45
    print(f"Sua passagem saira por R${p}")
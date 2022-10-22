n = int(input("Digite sua velocidade: "))

if n>80:
    nv = (n-80)*7
    print(f"\33[31mMULTADO!!! VOCÊ EXCEDEU O LIMITE DE VELOCIDADE PAGARÁ UMA MULTA DE R${nv}\33[m")
else:
    print("Muito bem! Dirija com cuidado")
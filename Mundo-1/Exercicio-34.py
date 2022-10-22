s = float(input("Digite seu salário: "))

if s <= 1250:
    n = s/100*15
    nr = s+n
    print(f"Seu novo salário é de R${nr:.2f}")
if s > 1250:
    n = s/100*10
    nv = s+n
    print(f"Seu novo salário é de R${nv:.2f}")

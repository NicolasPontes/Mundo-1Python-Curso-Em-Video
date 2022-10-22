print("Vamos calcular quanto você gastou com o alugel do carro")
input()
km = int(input("Digite os km percorridos: "))
d = int(input("Digite quantos dias foram o aluguel: "))
pkm = km*0.15
pd = d*60
pt = pd+pkm

print("Você deve R${}".format(pt))
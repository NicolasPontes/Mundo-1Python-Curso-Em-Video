n = int(input("Digite o preçodo produto: "))
d = (n/100)*5

print("Seu desconto é de R${}".format(d))
nv = n-d
print("Seu novo preço é de R${}".format(nv))
print("=+"*20)
print("Descobrindo Triângulos")
print("=+"*20)

a = float(input("Digite a primeira medida: "))
b = float(input("Digite a segunda medida: "))
c = float(input("Digite a terceria medida: "))

if a+b > c and a+c > b and c+b > a:
    print("É UM TRIÂNGULO")
else:
    print("NÂO È UM TRIÂNGULO")

p = int(input())
l = p//2
print(l)

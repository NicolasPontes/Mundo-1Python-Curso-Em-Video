a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
menor = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b


maior = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b


print(f"Maior número é {maior}")
print(f"Menor número é {menor}")

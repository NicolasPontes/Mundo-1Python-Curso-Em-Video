import math
a = float(input("Digite um ângulo: "))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
s = math.sin(math.radians(a))
print(f"O cosseno do seu ãngulo é: {c:.2}")
print(f"O seno do seu ângulo é: {s:.2}")
print(f"A tangente do seu ângulo é: {t:.2}")
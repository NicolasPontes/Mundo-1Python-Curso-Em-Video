import random
n1 = str(input("Digite o primeiro nome: "))
n2 = str(input("Digite o segundo  nome: "))
n3 = str(input("Digite o terceiro nome: "))
n4 = str(input("Digite o quarto nome: ")) 
listinha = [n1,n2,n3,n4]
a = random.choice(listinha)
print(f"O aluno escolhido foi {a}")
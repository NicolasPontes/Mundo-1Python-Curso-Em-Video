n = str(input("Digite uma frase: ")).capitalize().upper()
print("Sua frase contém {} letras A".format(n.count("A")))
print("O primeiro A aparece na posição {}".format(n.find("A")+1))
print("O ultimo A aparece na posição {}".format(n.rfind("A")+1))
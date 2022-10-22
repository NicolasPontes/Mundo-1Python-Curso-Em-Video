n = int(input("Digite o ano a ser analisado: "))

if n%4 == 0 and n%400 == 0 and  n%400 ==0:
    print(f"{n} È BISSEXTO")
else:
    print(f"{n} NÃO È BISSEXTO")
from random import randint
import time

print("\33[34m=+\33[m"*20)
print("\33[35m JOGO DA ADVINHAÇÂO\33[m")
print("\33[34m=+\33[m"*20)
n = int(input("Tente advinhar o número que eu pensei de 0 a 5: "))
if (n > 5):
    print("\33[36mLeia de novo as regras...\33[m")
    time.sleep(3)
    exit()

print("\33[35mProcessando...\33[m")
n1 = randint(0, 5)
time.sleep(5)
if (n == n1):
    print("\33[32mParabens!Você ganhou!\33[m")
else:
    print("\33[31mQue pena, mais sorte da proxima vez\33[m")
    print(f"\33[33mO número pensado foi {n1}\33[m")

import random

secret = random.randint(1, 10)
tries = 3

for i in range(tries):

    user = int(input("vgadai chislo ot 1-10: "))

    if secret == user:
        print(f"DA eto {secret}")
    if user < secret:
        print("bolshe")
    elif user > secret:
        print("menshe")
    print(f"ostalos {tries - 1} paputok")
else:
    print(f"paputki v minuse. chislo - {secret}")
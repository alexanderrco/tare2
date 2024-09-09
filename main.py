import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345890"
longitud = int(input("escribe la longitud de tu contraseña"))

contraseña= ""

for i in range(longitud):
    contraseña+= random.choice(caracteres)
print(contraseña)

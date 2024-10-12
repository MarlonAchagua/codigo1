import random

caracteres=  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud =int(input("Ingresa la longitud de tu contraseña: "))
resultado="14"
for i in range(longitud):
    resultado += random.choice(caracteres)


print(f"Tu contraseña con una longitud de {longitud} es: {resultado}")

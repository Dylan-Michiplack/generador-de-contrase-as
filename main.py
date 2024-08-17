import random
caracteres="qwertyuiopñalskdjfhgmzncbxv1762534890"

longitud= int(input("longitud de tu contraseña:"))
resultado=""
for i in range(longitud):
    resultado+=random.choice(caracteres)

print(f"tu contraseña es: {resultado}")

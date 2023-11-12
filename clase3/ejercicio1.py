"""
    Escribe un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
    como el de más abajo, de altura el número introducido.

"""

num = 4
for i in range(num):
    for j in range (i + 1):
         print("*", end="")
    print("")

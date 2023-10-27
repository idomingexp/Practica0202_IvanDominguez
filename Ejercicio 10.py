n = input("Dime tu contraseña:")
m = input("Introduce tu contraseña:")
while n != m:
    print("Contraseña errónea")
    m = input("Vuelve a introducir la contraseña:")
print("Contraseña correcta")
input()
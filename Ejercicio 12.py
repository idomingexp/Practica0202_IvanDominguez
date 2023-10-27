n = input("Dame una frase:")
m = input("Dime una letra de la frase:")
a = 0
for x in n:
    if x == m:
        a = a+1
print("La letra está en la frase ",a, "veces")
input()
n = int(input("Dime un Nº entero:"))
m = []
a = -1
for x in range(n):
    m.append(str(a + 2))
    print(" ".join(m[::-1]))
    a = a + 2
input()
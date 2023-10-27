n = input("Dime tu nombre:").lower()
m = input("Dime tu sexo:").lower()
if (ord(n[0]) < 109) and (m == "f"):
    print("Perteneces a Gryffindor")
elif (ord(n[0]) > 110) and (m == "m"):
    print("Perteneces a Gryffindor")
else:
    print("Perteneces a Slytheryn")
input()
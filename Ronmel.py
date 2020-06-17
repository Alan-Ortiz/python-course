lista1= ["jamón","huevito", 5, "catsup", .5, "#café", "agua"]
lista1[1]="huevo"
#print(lista1)
#if "CATSUP".lower() in lista1:
#    print("elemento dentro de la lista")
#else:
#    print("elemento no encontrado")


for elemento in lista1:
    print(str(type(elemento)))

    if str(type(elemento)) == "<class 'str'>":
        print(elemento)

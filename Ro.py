# # cadena="prueba"
# # #print(cadena[::-1])
# # #cadena[5]="o"
# # print(len(cadena))

# # #for x in cadena:
# # #    print(x)

# listaRon= ["pan", "salchicha", "mayonesa", "katsup", 2]
# print(len(listaRon))
# print(range(5))
# for e in range(5):
#     print (e)

# nuevoset = {"chocolate", "pan", "soda","sal", "pan", "sal"}
# #nuevoset[0]= "CHOCOLATE"
# nuevoset.add("pastel")
# print(nuevoset)

# diccionario = {"llave1": "valor", "llave2": "valor2", "llave3": "valor3"}
# for e1, e2 in diccionario.items():
#     print(e1)

# Var = 11
# while Var<10:
#     print(Var)

print("\tIniciando calculadora Básica") 
#while True:

    num1=input("\t\tIntroduzca el primer número: ") #Que se solicite por cada operación
#print(num1)
    num2=input("\t\tIntroduzca el segundo número: ") #Que se solicite por cada operación
#print(num2)
#print("\n\t\t\t\tQue quieres hacer?")
    num1 = int(num1)
    num2 = int(num2)
    print("\t1. suma\n\t2. resta\n\t3. división\n\t4. multiplicación\n\t5. potencia\n\n\t6. SALIR")
#oper=input("\n\n¿QUE DESEAS HACER?")
    while True:

        oper=input("\n¿QUE OPERACIÓN DESEAS HACER? ")
        if oper=="1":
            result=num1+num2
        elif oper=="2":
            result=num1-num2
        elif oper=="3":
            result=num1/num2
        elif oper=="4":
            result=num1*num2
        elif oper=="5":
            result=num1**num2
        elif oper=="6":
            break
        else:
            result=(oper, " Opción inválida")
        print(result)
        otra=input("¿Desea otra operación (S/N)?")
        if otra!="S" or "s": #Que acepte s/S
            break       
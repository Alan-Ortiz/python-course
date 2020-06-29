print("\tIniciando calculadora Básica")
continuar=True  
while continuar:
    num1=input("\t\tIntroduzca el primer número: ") 
    num2=input("\t\tIntroduzca el segundo número: ") 
    num1 = int(num1)
    num2 = int(num2)
    print("\t1. suma\n\t2. resta\n\t3. división\n\t4. multiplicación\n\t5. potencia\n\n\t6. SALIR")
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
    if otra!="S": 
        continuar=False 
        break
    

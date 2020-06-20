# print("Iniciando calculadora")
# print("1. suma")
# print("2. resta")
# print("3. división")
# print("4. multiplicación")
# print("5. potencia")
# num1=input("Introduzca el primer número: ")
# print(num1)
# num2=input("Introduzca el segundo número: ")
# print(num2)
# print(int(num1)+int(num2))
print("Iniciando calculadora")
num1=input("Introduzca el primer número: ")
#print(num1)
num2=input("Introduzca el segundo número: ")
#print(num2)
print("Que quieres hacer?")
print("\t1. suma\n\t2. resta\n\t3. división\n\t4. multiplicación\n\t5. potencia\n\n")
oper=input("\n\nIngrese su opción: ")
num1 = int(num1)
num2 = int(num2)
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
else:
    result=(oper, " Opción inválida")
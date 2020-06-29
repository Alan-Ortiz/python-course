# def prueba(a,b,c=3.14):
#     a=int(a)
#     b=int(b)
#     print(a+b+c)
# prueba("100","100")
#Duplicate encode
def duplicate_encode(word):
    new_word=word.upper()
    cadena_vacia=""
    print(new_word)
    for elemento in new_word:
        if new_word.count(elemento)>1:
            # print(")")
            cadena_vacia=cadena_vacia + ")"
        # print(elemento)
        else:
            # print("(")
            cadena_vacia=cadena_vacia + "("
    print(cadena_vacia)
    # print(new_word.count("H"))
duplicate_encode("hHOhHOLA")



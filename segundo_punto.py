
def cifrar_cesar(texto, clave): #función que se encarga de recorrer los caracteres de la palabra digitada para cifrar
    cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            cifrado += chr(((ord(caracter) - ord('a' ) + clave) % 26) + ord('a')) 
            """la primera parte Calcula el índice del carácter en el alfabeto, 
            luego se agrega la clave para realizar el desplazamiento y 
            luego se calcula el resultado módulo 26 para asegurarse de que el desplazamiento 
            se mantenga dentro de las letras del alfabeto"""
        else:
            cifrado += caracter #si se agrega un caracter por fuera del alfabeto se agrega al final del cifrado
    return cifrado

def descifrar_cesar(texto_cifrado, clave):
    return cifrar_cesar(texto_cifrado, -clave) #se pone la clave negativa para generar el desplazamiento inverso y lograr recuperar el mensaje original

def cifrar():
    texto = input("Ingresa el texto a cifrar: ").lower() #se recibe el texto a cifrar y se convierte a minusculas con .lower()
    clave = int(input("Ingrese el desplazamiento (un número entero): "))
    
    texto_cifrado = cifrar_cesar(texto, clave)
    print(f"Texto cifrado: {texto_cifrado}")

def descifrar():
    texto_cifrado = input("Ingresa el texto cifrado: ") #se recibe el texto a descifrar y se convierte a minusculas con .lower()
    clave = int(input("Ingrese el desplazamiento (un número entero): "))
    
    texto_descifrado = descifrar_cesar(texto_cifrado, clave)
    print(f"Texto descifrado: {texto_descifrado}")

def funcion_cesar():
    
    opcion = input("¿Quieres cifrar (C) o descifrar (D)? ").lower() #Permite escoger de entrada si se quiere cifrar o descifrar
    
    if opcion == 'c':
        cifrar()
    elif opcion == 'd':
        descifrar()
    else:
        print("Opción no válida. Debes elegir 'C' para cifrar o 'D' para descifrar.")

funcion_cesar()

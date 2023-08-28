
def cifrar_cesar(texto, clave):
    cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            cifrado += chr(((ord(caracter) - ord('a' ) + clave) % 26) + ord('a'))
        else:
            cifrado += caracter
    return cifrado

def descifrar_cesar(texto_cifrado, clave):
    return cifrar_cesar(texto_cifrado, -clave)

def cifrar():
    texto = input("Ingresa el texto a cifrar: ").lower()
    clave = int(input("Ingrese el desplazamiento (un número entero): "))
    
    texto_cifrado = cifrar_cesar(texto, clave)
    print(f"Texto cifrado: {texto_cifrado}")

def descifrar():
    texto_cifrado = input("Ingresa el texto cifrado: ")
    clave = int(input("Ingrese el desplazamiento (un número entero): "))
    
    texto_descifrado = descifrar_cesar(texto_cifrado, clave)
    print(f"Texto descifrado: {texto_descifrado}")

def funcion_cesar():
    
    opcion = input("¿Quieres cifrar (C) o descifrar (D)? ").lower()
    
    if opcion == 'c':
        cifrar()
    elif opcion == 'd':
        descifrar()
    else:
        print("Opción no válida. Debes elegir 'C' para cifrar o 'D' para descifrar.")

funcion_cesar()

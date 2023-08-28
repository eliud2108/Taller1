def evaluar_expresion(expresion, x0, y0, h, n):
    variables_permitidas = {'x', 'y'}
    operadores_permitidos = {'+', '-', '*', '/'}
    numeros_permitidos = set('0123456789 ')
    caracteres_permitidos = variables_permitidas | operadores_permitidos | numeros_permitidos | {'(', ')'}
    
    if all(char in caracteres_permitidos for char in expresion):
        vbles_remplazo = {'x': x0, 'y': y0}
        
        print(f"Iteración |    x    |    y    ")
        print("-" * 31)
        
        for i in range(n + 1):
            resultado = eval(expresion, vbles_remplazo)
            print(f"{i:^10} | {x0:^8.1f} | {y0:^8.3f}")
            
            x0 = x0 + h
            y0 = y0 + h * resultado
        return "Datos calculados"
        
        
    else:
        return "Expresión inválida"

print (f"Este código resuelve EDOs por el método de euler")
x0 = float(input("Ingresa el valor inicial de x (x0): "))
y0 = float(input("Ingresa el valor inicial de y (y0): "))
h = float(input("Ingresa el tamaño del paso (h): "))
n = int(input("Ingresa el número de pasos (n): "))
while True:
    ecuacion = input("Ingresa una expresión válida (usando x, y), o 'salir' para terminar: ")

    if ecuacion.lower() == 'salir':
        break
    
    resultado_evaluacion = evaluar_expresion(ecuacion, x0, y0, h, n)
    print(resultado_evaluacion)
    
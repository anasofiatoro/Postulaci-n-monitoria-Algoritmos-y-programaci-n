import random
import numpy as np

def validar_numeros(lista):
    # Validar que el argumento sea una lista
    if not isinstance(lista, list):
        return f"Error: Se esperaba una lista, pero se recibió un dato de tipo {type(lista).__name__}."

    # Validar que la lista tenga exactamente 10,000 elementos
    if len(lista) != 10000:
        return "Error: La lista no contiene 10,000 elementos."

    # Validar que todos los elementos de la lista sean números enteros dentro del rango -999 a 999
    for numero in lista:
        if not isinstance(numero, int):
            return f"Error: Se encontró un elemento no numérico: {numero}."
        if numero < -999 or numero > 999:
            return f"Error: El número {numero} está fuera del rango permitido (-999 a 999)."

    # Procesar los datos
    return procesar_datos(lista)

def procesar_datos(lista):
    # Convertir la lista a un array de numpy para cálculos eficientes
    array = np.array(lista)

    # Promedio de todos los números
    promedio_total = np.mean(array)

    # Varianza de todos los números
    varianza_total = np.var(array)

    # Números múltiplos de 3 y 7
    multiples_3_y_7 = [num for num in array if num % 3 == 0 and num % 7 == 0]
    promedio_multiples_3_y_7 = np.mean(multiples_3_y_7) if multiples_3_y_7 else 0

    # Números que terminan en combinación de par e impar
    def termina_en_par_impar(n):
        return (n % 10) % 2 != (n // 10 % 10) % 2

    numeros_par_impar = [num for num in array if termina_en_par_impar(num)]
    conteo_par_impar = len(numeros_par_impar)

    # Números con tres dígitos
    tres_digitos = [num for num in array if 100 <= abs(num) <= 999]
    conteo_tres_digitos = len(tres_digitos)

    # Números con tres dígitos diferentes
    tres_digitos_diferentes = [num for num in tres_digitos if len(set(str(abs(num)))) == 3]
    conteo_tres_digitos_diferentes = len(tres_digitos_diferentes)

    # Número más cercano al promedio y más lejano al promedio
    diferencia = np.abs(array - promedio_total)
    numero_cercano = array[np.argmin(diferencia)]
    numero_lejano = array[np.argmax(diferencia)]

    # Retornar los resultados en una tupla
    return (
        promedio_total,
        varianza_total,
        promedio_multiples_3_y_7,
        conteo_par_impar,
        conteo_tres_digitos,
        conteo_tres_digitos_diferentes,
        numero_cercano,
        numero_lejano
    )

# Generar la lista de 10,000 números aleatorios entre -999 y 999
lista_numeros = [random.randint(-999, 999) for _ in range(10000)]

# Imprimir la lista completa de números
print("Lista generada:")

# Llamar a la función y mostrar el resultado de las validaciones
print(lista_numeros)
resultado = validar_numeros(lista_numeros)
if isinstance(resultado, tuple):
    print("Resultados del procesamiento:")
    print(f"Promedio de todos los números: {resultado[0]}")
    print(f"Varianza de todos los números: {resultado[1]}")
    print(f"Promedio de números múltiplos de 3 y 7: {resultado[2]}")
    print(f"Cantidad de números terminan en combinación par-impar: {resultado[3]}")
    print(f"Cantidad de números con tres dígitos: {resultado[4]}")
    print(f"Cantidad de números con tres dígitos diferentes: {resultado[5]}")
    print(f"Número más cercano al promedio: {resultado[6]}")
    print(f"Número más lejano al promedio: {resultado[7]}")
else:
    print(resultado)
print()

    # Evaluación 1: Ingresar un dato diferente a una lista
print("Evaluación 1:")
resultado_1 = validar_numeros("no es una lista")
print(resultado_1)
print()

# Evaluación 2: Ingresar una lista con una mezcla de números y letras
print("Evaluación 2:")
lista_mixta = [random.randint(-999, 999) for _ in range(9999)] + ['a']  # Lista con un elemento no numérico
resultado_2 = validar_numeros(lista_mixta)
print(resultado_2)
print()

# Evaluación 3: Ingresar la lista de números aleatorios correctamente diligenciada
print("Evaluación 3:")
lista_numeros = [random.randint(-999, 999) for _ in range(10000)]

print(resultado_3)
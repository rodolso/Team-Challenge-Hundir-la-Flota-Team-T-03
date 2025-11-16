import numpy as np
import random
from variables import filas_tablero, cols_tablero

def pedir_coordenadas_usuario():
    """
    Pide al usuario las coordenadas donde quiere disparar.
    Devuelve una tupla (x, y)
    """
    while True:
        try:
            entrada = input("Introduce las coordenadas para disparar (formato: fila,columna o letra num, ej: 5,3 o E5): ").strip().upper()
            
            # Intentar formato letra+número (ej: E5)
            if len(entrada) >= 2 and entrada[0].isalpha() and entrada[1:].isdigit():
                letra = entrada[0]
                numero = int(entrada[1:])
                y = ord(letra) - ord('A')
                x = numero - 1
            # Intentar formato número,número (ej: 5,3)
            elif ',' in entrada:
                partes = entrada.split(',')
                x = int(partes[0].strip()) - 1  # Convertir a 0-based
                y = int(partes[1].strip()) - 1
            else:
                print("Formato incorrecto. Usa: fila,columna (ej: 5,3) o letra+num (ej: E5)")
                continue
            if 0 <= x < filas_tablero and 0 <= y < cols_tablero:
                return (x, y)
            else:
                print(f"Coordenadas fuera de rango. Usa filas 1-{filas_tablero} y columnas A-{chr(65 + cols_tablero - 1)}")
        except (ValueError, IndexError):
            print("Formato incorrecto. Usa: fila,columna (ej: 5,3) o letra+num (ej: E5)")

def pedir_coordenadas_maquina(tablero_enemigo=None):
    """
    Genera coordenadas aleatorias para el disparo de la maquina
    Si se da tablero enemigo, evita disparar a posiciones ya disparadas
    devuelve una tupla (x, y)
    """
    if tablero_enemigo is not None:
        tablero_oculto = tablero_enemigo.get_tablero_oculto()
        posiciones_disparadas = set()
        for i in range(filas_tablero):
            for j in range(cols_tablero):
                celda = tablero_oculto[i, j]
                # Si la celda tiene un disparo (perdido o acertado), ya fue disparada
                if celda == tablero_enemigo.disparo_perdido or celda == tablero_enemigo.disparo_acertado:
                    posiciones_disparadas.add((i, j))
        
        # Generar coordenadas hasta encontrar una no disparada
        intentos = 0
        while intentos < 100:  # Límite de intentos para evitar bucle infinito
            x = random.randint(0, filas_tablero - 1)
            y = random.randint(0, cols_tablero - 1)
            if (x, y) not in posiciones_disparadas:
                return (x, y)
            intentos += 1
        return (random.randint(0, filas_tablero - 1), random.randint(0, cols_tablero - 1))
    else:
        x = random.randint(0, filas_tablero - 1)
        y = random.randint(0, cols_tablero - 1)
        return (x, y)

def recibir_disparos(tablero, x, y):
    """
    Procesa un disparo en el tablero enemigo.
    Retorna el resultado: 'Tocado', 'Hundido', 'Agua' o 'Ya disparado'.
    """
    return tablero.recibir_disparo(x, y)

def procesar_disparo(tablero, x, y):
    """
    Procesa un disparo en el tablero propio.
    Retorna el resultado: 'Tocado', 'Hundido', 'Agua' o 'Ya disparado'.
    """
    return tablero.recibir_disparo(x, y)

def juego_terminado(tablero):
    """
    Comprueba si el juego ha terminado (no quedan barcos vivos).
    Retorna True si no hay barcos vivos, False en caso contrario.
    """
    return not tablero.hay_barcos_vivos()

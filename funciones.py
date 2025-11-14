import numpy as np
# Función para crear el tablero:
def crear_tablero(filas_tablero=10, cols_tablero = 10, agua ="~"):
    tablero = np.full((filas_tablero, cols_tablero,), agua)
    return tablero
tablero = crear_tablero()

def tablero_bonito(tablero):
    filas_tablero, cols_tablero = tablero.shape  
    # Encabezado
    print("\n   " + " ".join([chr(65 + i) for i in range(cols_tablero)]))
    print("  " + "─" * (cols_tablero * 2))
    # Filas
    for i in range(filas_tablero):
        print(f"{i+1:2}│" + " ".join(tablero[i]) + "│")
    
    print("  " + "─" * (cols_tablero * 2))

print(tablero_bonito(tablero))

# obtener coordenadas:
flota = {}
def pedir_coordenadas_usuario(coordenadas):
    list_ =[]
    b4_1_xy1 = input("Introduce las coordenadas para tu barco de 4 posiciones de eslora x.y:")
    b4_1_xy1 = int(b4_1_xy1.split( "," ))            
    list.append(b4_1_xy1)
    
    


# Función para colocar cada barco:
def colocar_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "0"
    return tablero  
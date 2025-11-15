from variables import
from tablero import Tablero 
from funciones import *

def juego ():

    respuesta = input("Hola! Bienvenido al juego Hundir la Flota. Sabes cómo funciona este juego? (si/no)").strip().lower().replace("í","i")
    if respuesta == "no":
        print ('''Instrucciones del juego: El objetivo del juego es hundir todos los barcos del enemigo antes de que él lo haga.
        El juego empieza teniendo cada uno de vosotros un tablero con unos barcos en posiciones que la otra persona no conoce.
        Tienes que decir a qué coordenada quieres impactar, como por ejemplo: Coordenada (1,2) o coordenada (3,5).
        Si aciertas, la otra persona dirá Tocado o Hundido. Sino, dirá Agua.
        Los turnos se alternan hasta que uno de los jugadores ya no tenga barcos.
        Gana la persona que hunda la flota primero. A por todas!''')
    elif respuesta == "si":
        print ("Pulsa Enter para empezar la partida")
    else:
        print ("Perdona, vuelve a introducir tu respuesta")
        return

    jugador = Tablero(1)
    maquina = Tablero(2)

    jugador.colocar_barcos()
    maquina.colocar_barcos()

    turno_jugador = True

    while True: #Empieza el turno del jugador

        if turno_jugador:
            print("\nTu tablero:")
            jugador.mostrar_tablero_propio() #Mostramos nuestros barcos
            print("\nTablero enemigo:")
            maquina.mostrar_tablero_enemigo() #Mostramos los disparos que ha hecho la máquina

            x, y = pedir_coordenadas_usuario()

            resultado = recibir_disparos (maquina,x,y)
            print ("Resultado:", resultado)
        
            if juego_terminado (maquina): #Revisamos si el jugador ha ganado
                print ("Has ganado! Enhorabuena!")
                break

            turno_jugador = False #Damos turno a la máquina
        
        else: #Turno de la máquina
        
            print ("\n Turno de la máquina")
        
            x,y = pedir_coordenadas_maquina()

            resultado = procesar_disparo (jugador, x,y)
            print (f"La máquina dispara a {x}, {y}: {resultado}")
    
            if juego_terminado (jugador):
                print ("Has perdido :( la máquina ha hundido todos tus barcos.")
                break

            turno_jugador = True         

if __name__ == "__main__":
    juego()


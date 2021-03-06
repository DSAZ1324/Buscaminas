from Casilla import Casilla
from Numero_casilla import Numero
from Mina_casilla import Mina
from Tablero import Tablero

tab = []


def ganar(tab):
    """
    funcion que revisa si el juego a concluido

    :param tab: list que representa el  con el tablero asignado
    :return: bool que repreenta si el juego a concluido efectivamente
    """
    casillas_libres = 0
    casillas_reveladas = 0
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if Casilla.numero(tab[x][y]) == 0:
                casillas_libres += 1
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if Casilla.numero(tab[x][y]) == 0 and Casilla.estado(tab[x][y]) == True:
                casillas_reveladas += 1
    if casillas_libres == casillas_reveladas:
        return True
    else:
        return False


def expandir(tab):
    """
    funcion que revela casillas en el buscaminas

    :param tab: list of list deltablero
    :return: list of list con las casillas reveladas
    """
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if Casilla.estado(tab[x][y]) == 0:
                if Numero(x, y).buscar_minas(tab) == 0:
                    for i in range(max(x - 1, 0), min(x + 2, len(tab))):
                        for j in range(max(y - 1, 0), min(y + 2, len(tab))):
                            Casilla.cambiar_estado(tab[i][j], True)
    return tab


def minas_numeros(tab, x, y):
    """
    Funcion que identifica cuantas minas hay en el tablero y crea los numeros para recuerdo

    :param tab:list of list con el tablero creado
    :param x:int con los parametros de minas y numeros en el tablero para x
    :param y: int con los parametros de minas y numeros en el tablero para y
    :return: list of list de tablero con las parametros de minas y numeros
    """
    for i in range(int(x)):
        for j in range(int(y)):
            if tab[i][j] == 1:
                tab[i][j] = Mina(i, j)
            else:
                tab[i][j] = Numero(i, j)
    return tab


def tablero_revelado(x, y):
    """
    Funcios que realza la creacion del tablero numerico

    :param x: int con las coordenadas del tablero en x
    :param y: int con las corrdenadas del tablero en y
    :return: list con la numeros en el tablero
    """
    tabl = []
    for i in range(int(x)):
        tabll = []
        for j in range(int(y)):
            tabll.append(Casilla(i, j).numero())
        tabl.append(tabll)
    return tabl


def turno_tablero(tabl, x, y):
    """
    Funcion que nos permite imprimir el tablero y a su vez actualizarlo luego de realizar algun
    movimiento.

    :param tabl: el tablero para el juego
    :param x: int que representa las dimensiones del tablero en el eje x
    :param y: int que representa las dimensiones del tablero en el eje y
    :return: list of list con los movimientos realizados al tablero

    """
    print('  |', end='')
    for i in range(int(y)):
        if i >= 10:
            print(f'{i}|', end='')
        else:
            print(f' {i}|', end='')
    print('\n' + (int(y) + 1) * '---')
    for i in range(int(x)):
        if i >= 10:
            print(f'{i}|', end='')
        else:
            print(f' {i}|', end='')
        for j in range(int(y)):
            if Casilla.estado(tabl[i][j]):
                if Casilla.numero(tabl[i][j]) == 0:
                    cant_de_minas = Numero(i, j).buscar_minas(tabl)
                    if cant_de_minas == 0:
                        print('  |', end='')
                    elif cant_de_minas > 0:
                        print(f" {str(cant_de_minas)}|", end="")
                else:
                    print(" X|", end="")
            else:
                if Casilla.opcion(tabl[i][j]) == '*':
                    print(" *|", end="")
                elif Casilla.opcion(tabl[i][j]) == '?':
                    print(" ?|", end="")
                else:
                    print(" x|", end='')
        print()


x = int(input('Introduzca el ancho '))
y = int(input('Introduzca el largo '))
tab = Tablero(x, y)
tab = Tablero.crear_tablero(tab)
tab = tablero_revelado(x, y)
tab = minas_numeros(tab, x, y)
fin = False
turno_tablero(tab, x, y)
try:
    while True:
        opcion = input("Ingrese jugada(Fila, columna, opción[*(Bomba),?(Quizas),q(Quitar),j(Jugada)]), o 'Salir: ")
        if opcion == 'Salir':
            break
        else:
            (opcion_1, opcion_2, opcion_3) = opcion.split(",")
        if not Casilla.estado(tab[int(opcion_1)][int(opcion_2)]):
            if opcion_3 == 'j':
                if Casilla.numero(tab[int(opcion_1)][int(opcion_2)]) == 1:
                    break
                else:
                    Casilla.cambiar_estado(tab[int(opcion_1)][int(opcion_2)], True)
            elif opcion_3 == '*':
                Casilla.posible_bomba(tab[int(opcion_1)][int(opcion_2)], '*')
            elif opcion_3 == '?':
                Casilla.posible_bomba(tab[int(opcion_1)][int(opcion_2)], '?')
            elif opcion_3 == 'q':
                Casilla.posible_bomba(tab[int(opcion_1)][int(opcion_2)], '')
        else:
            print('¡Ya presionaste esta opcion!')
        tab = expandir(tab)
        fin = ganar(tab)
        if fin:
            break
        turno_tablero(tab, x, y)
    if not fin:
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if not Casilla.estado(tab[i][j]):
                    Casilla.cambiar_estado(tab[i][j], True)
        turno_tablero(tab, x, y)
        print("¡Boom!")
    else:
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if not Casilla.estado(tab[i][j]):
                    Casilla.cambiar_estado(tab[i][j], True)
        turno_tablero(tab, x, y)
        print("¡Lo lograste!")
except:
    print('Metiste mal el dedo')
"rewrewrwer"
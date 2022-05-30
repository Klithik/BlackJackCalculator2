import PySimpleGUI as sg

n = 1
mano2 = False
cambio = False
layout = [
    [sg.Text('Cantidad de mazos: '),sg.Input('1'),sg.Button('Guardar'),sg.Text('Mazos en uso: 1',key = 'mazos')],
    [sg.Text('Seleccionar cartas del dealer:')],
    [sg.Button('As',key ='AsDealer'),sg.Button('2',key = '2Dealer'),sg.Button('3',key = '3Dealer'),sg.Button('4',key = '4Dealer'),
    sg.Button('5',key = '5Dealer'),sg.Button('6',key = '6Dealer'),sg.Button('7',key = '7Dealer'),sg.Button('8',key = '8Dealer'),
    sg.Button('9',key = '9Dealer'),sg.Button('10',key = '10Dealer'),sg.Button('J',key = 'JDealer'),sg.Button('Q',key = 'QDealer'),
    sg.Button('K',key = 'KDealer')],
    [sg.Text('Seleccionar cartas del jugador:')],
    [sg.Button('As',key = 'AsPlayer'),sg.Button('2',key = '2Player'),sg.Button('3',key = '3Player'),sg.Button('4',key = '4Player'),
    sg.Button('5',key = '5Player'),sg.Button('6',key = '6Player'),sg.Button('7',key = '7Player'),sg.Button('8',key = '8Player'),
    sg.Button('9',key = '9Player'),sg.Button('10',key = '10Player'),sg.Button('J',key = 'JPlayer'),sg.Button('Q',key = 'QPlayer'),
    sg.Button('K',key = 'KPlayer'),sg.Button('Split',key = 'split')],
    [sg.Text('Estado Jugador: 0',key = 'pjePlayer'),sg.Text('',key = 'pje2Player'),sg.Text('Estado Dealer: 0',key = 'pjeDealer'),
    sg.Button('Cambio de ronda',key = 'ronda'),sg.Button('Cambio de Mano',key = 'cambioMano')],
    [sg.Text('Conteo de cartas: ',key = 'cuenta')],
    [sg.Text('Probabilidad de 21: -',key = 'P21'),sg.Text('Probabilidad de 20: -',key = 'P20'),
    sg.Text('Probabilidad de 19: -',key = 'P19'),sg.Text('Probabilidad de 18: -',key = 'P18')]
]

window = sg.Window('BlackJack',layout)

baraja = [
    [4*n,1],
    [4*n,2],
    [4*n,3],
    [4*n,4],
    [4*n,5],
    [4*n,6],
    [4*n,7],
    [4*n,8],
    [4*n,9],
    [16*n,10]]

manoDealer = [
    [0,1],
    [0,2],
    [0,3],
    [0,4],
    [0,5],
    [0,6],
    [0,7],
    [0,8],
    [0,9],
    [0,10],
    [0,11],
    [0,12],
    [0,13]]

manoPlayer = [
    [0,1],
    [0,2],
    [0,3],
    [0,4],
    [0,5],
    [0,6],
    [0,7],
    [0,8],
    [0,9],
    [0,10],
    [0,11],
    [0,12],
    [0,13]]

mano2Player = [
    [0,1],
    [0,2],
    [0,3],
    [0,4],
    [0,5],
    [0,6],
    [0,7],
    [0,8],
    [0,9],
    [0,10],
    [0,11],
    [0,12],
    [0,13]]

#==========ZONA DE METODOS==========
def PuntajeDealer():
    suma = 0
    for t in manoDealer:
        if t[1] > 9:
            suma += t[0]*10
        else:
            suma += t[0]*t[1]
    if suma < 12 and manoDealer[0][0] != 0:
        suma += 10
    window['pjeDealer'].update('Estado Dealer: ' + str(suma))
    return suma

def PuntajePlayer():
    suma = 0
    for t in manoPlayer:
        if t[1] > 9:
            suma += t[0]*10
        else:
            suma += t[0]*t[1]
    if suma < 12 and manoPlayer[0][0] != 0:
        suma += 10
    window['pjePlayer'].update('Estado Jugador: ' + str(suma))
    return suma

def Puntaje2Player():
    suma = 0
    for t in mano2Player:
        if t[1] > 9:
            suma += t[0]*10
        else:
            suma += t[0]*t[1]
    if suma < 12 and mano2Player[0][0] != 0:
        suma += 10
    window['pje2Player'].update('Estado 2 Jugador: ' + str(suma))
    return suma

def cuentaCartas():
    conteo = 0
    for t in manoDealer:
        num = t[1]
        cantidad = t[0]
        if num > 1 and num < 7:
            conteo -= cantidad
        elif num > 9 or num == 1:
            conteo += cantidad
    
    for t in manoPlayer:
        num = t[1]
        cantidad = t[0]
        if num > 1 and num < 7:
            conteo -= cantidad
        elif num > 9 or num == 1:
            conteo += cantidad
    return conteo

def probSacar(num):
    return baraja[num-1][0]/cartasRestantes()

def nuevaCarta(carta,mano):
    baraja[carta-1][0] -= 1
    if mano == 1:
        manoDealer[carta-1][0] += 1
        PuntajeDealer()
    elif mano == 2:
        if mano2:
            mano2Player[carta-1][0] += 1
            Puntaje2Player()
        else:
            manoPlayer[carta-1][0] += 1
            PuntajePlayer()
    
    window['P21'].update(str(round(actualizaProbs(21),2)) + '%')
    window['cuenta'].update('Conteo de cartas: ' + str(cuentaCartas()))

def cartasRestantes():
    suma = 0
    for t in baraja:
        suma += t[0]
    return suma

def splitAs():
    total = 0
    repetido = 0
    for t in manoPlayer:
        total += t[0]
        if t[0] == 2:
            repetido = t[1]
    if total == 2:
        manoPlayer[repetido-1][0] -= 1
        mano2Player[repetido-1][0] += 1
    window['cambioMano'].update('Cambio mano')
    Puntaje2Player()
    PuntajePlayer()

def prob21(mano):
    return probSacar(21-mano)

def actualizaProbs(num):
    contenido = [num]
    posible = True
    prob = 0
    while posible:
        posible = False
        probCombinacion = 1
        total = 25
        for n in contenido:
            probCombinacion *= baraja[n-1][0]/total
            total -= 1
            baraja[n-1][0] -= 1
            if n != 1:
                contenido.remove(n)
                contenido.append(1)
                contenido.append(n-1)
                posible = True
                break
        prob += probCombinacion
    return prob

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Guardar':
        if(values[0] != n):
            n = values[0]
            window['mazos'].update('Mazos en uso: ' + str(n))
    
    #ACCIONAMIENTO BOTON DE CAMBIO DE RONDA
    if event == 'ronda':
        for t in manoDealer:
            t[0] = 0
        for t in manoPlayer:
            t[0] = 0
        
        mano2 = False
        cambio = False
        window['pjeDealer'].update('Estado Dealer: 0')
        window['pjePlayer'].update('Estado Jugador: 0')
        window['pje2Player'].update('')
    
    if event == 'split':
        splitAs()
        cambio = True
    
    if event == 'cambioMano':
        if cambio:
            mano2 = True
    
    #ACCIONES DE BOTONES DE SELECCION DE CARTAS
    if event == 'AsDealer':
        nuevaCarta(1,1)
    if event == 'AsPlayer':
        nuevaCarta(1,2)
    if event == '2Dealer':
        nuevaCarta(2,1)
    if event == '2Player':
        nuevaCarta(2,2)
    if event == '3Dealer':
        nuevaCarta(3,1)
    if event == '3Player':
        nuevaCarta(3,2)
    if event == '4Dealer':
        nuevaCarta(4,1)
    if event == '4Player':
        nuevaCarta(4,2)
    if event == '5Dealer':
        nuevaCarta(5,1)
    if event == '5Player':
        nuevaCarta(5,2)
    if event == '6Dealer':
        nuevaCarta(6,1)
    if event == '6Player':
        nuevaCarta(6,2)
    if event == '7Dealer':
        nuevaCarta(7,1)
    if event == '7Player':
        nuevaCarta(7,2)
    if event == '8Dealer':
        nuevaCarta(8,1)
    if event == '8Player':
        nuevaCarta(8,2)
    if event == '9Dealer':
        nuevaCarta(9,1)
    if event == '9Player':
        nuevaCarta(9,2)
    if event == '10Dealer':
        nuevaCarta(10,1)
    if event == '10Player':
        nuevaCarta(10,2)
    if event == 'JDealer':
        nuevaCarta(10,1)
    if event == 'JPlayer':
        nuevaCarta(10,2)
    if event == 'QDealer':
        nuevaCarta(10,1)
    if event == 'QPlayer':
        nuevaCarta(10,2)
    if event == 'KDealer':
        nuevaCarta(10,1)
    if event == 'KPlayer':
        nuevaCarta(10,2)

window.close()
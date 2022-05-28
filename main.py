import PySimpleGUI as sg

n = 1
layout = [
    [sg.Text('Cantidad de mazos: '),sg.Input('1'),sg.Button('Guardar'),sg.Text('Mazos en uso: ' + str(n))],
    [sg.Text('Seleccionar cartas del dealer:')],
    [sg.Button('As',key ='AsDealer'),sg.Button('2',key = '2Dealer'),sg.Button('3',key = '3Dealer'),sg.Button('4',key = '4Dealer'),
    sg.Button('5',key = '5Dealer'),sg.Button('6',key = '6Dealer'),sg.Button('7',key = '7Dealer'),sg.Button('8',key = '8Dealer'),
    sg.Button('9',key = '9Dealer'),sg.Button('10',key = '10Dealer'),sg.Button('J',key = 'JDealer'),sg.Button('Q',key = 'QDealer'),
    sg.Button('K',key = 'KDealer')],
    [sg.Text('Seleccionar cartas del jugador:')],
    [[sg.Button('As',key = 'AsPlayer'),sg.Button('2',key = '2Player'),sg.Button('3',key = '3Player'),sg.Button('4',key = '4Player'),
    sg.Button('5',key = '5Player'),sg.Button('6',key = '6Player'),sg.Button('7',key = '7Player'),sg.Button('8',key = '8Player'),
    sg.Button('9',key = '9Player'),sg.Button('10',key = '10Player'),sg.Button('J',key = 'JPlayer'),sg.Button('Q',key = 'QPlayer'),
    sg.Button('K',key = 'KPlayer')]]
]

window = sg.Window('BlackJack',layout)

while True:
    n = 1
    baraja = [
        [n,1],
        [n,2],
        [n,3],
        [n,4],
        [n,5],
        [n,6],
        [n,7],
        [n,8],
        [n,9],
        [n,10],
        [n,11],
        [n,12],
        [n,13]]
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Guardar':
        if(values[0] != n):
            n = values[0]
    
    #ACCIONES DE BOTONES DE SELECCION DE CARTAS
    if event == 'AsDealer':
        baraja[0][0] -= 1
    if event == 'AsPlayer':
        baraja[0][0] -= 1
    if event == '2Dealer':
        baraja[1][0] -= 1
    if event == '2Player':
        baraja[1][0] -= 1
    if event == '3Dealer':
        baraja[2][0] -= 1
    if event == '3Player':
        baraja[2][0] -= 1
    if event == '4Dealer':
        baraja[3][0] -= 1
    if event == '4Player':
        baraja[3][0] -= 1
    if event == '5Dealer':
        baraja[4][0] -= 1
    if event == '5Player':
        baraja[4][0] -= 1
    if event == '6Dealer':
        baraja[5][0] -= 1
    if event == '6Player':
        baraja[5][0] -= 1
    if event == '7Dealer':
        baraja[6][0] -= 1
    if event == '7Player':
        baraja[6][0] -= 1
    if event == '8Dealer':
        baraja[7][0] -= 1
    if event == '8Player':
        baraja[7][0] -= 1
    if event == '9Dealer':
        baraja[8][0] -= 1
    if event == '9Player':
        baraja[8][0] -= 1
    if event == '10Dealer':
        baraja[9][0] -= 1
    if event == '10Player':
        baraja[9][0] -= 1
    if event == 'JDealer':
        baraja[10][0] -= 1
    if event == 'JPlayer':
        baraja[10][0] -= 1
    if event == 'QDealer':
        baraja[11][0] -= 1
    if event == 'QPlayer':
        baraja[11][0] -= 1
    if event == 'KDealer':
        baraja[12][0] -= 1
    if event == 'KPlayer':
        baraja[12][0] -= 1

window.close()
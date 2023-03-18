import PySimpleGUI as sg
import img_base64

possibilidades = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ['1','4','7'],
    ['2','5','8'],
    ['3','6','9'],
    ['1','5','9'],
    ['3','5','7'],]

sg.theme('LightBlue3')

layout = [[sg.Text('Jogo da velha')],
          [sg.Button('', image_data=img_base64.button_empy, key='1', enable_events=True), sg.Button('', image_data=img_base64.button_empy, key='2'), sg.Button('', image_data=img_base64.button_empy, key='3'), sg.Button('', image_data=img_base64.button_2_p, key='2p')],
          [sg.Button('', image_data=img_base64.button_empy, key='4'), sg.Button('', image_data=img_base64.button_empy, key='5'), sg.Button('', image_data=img_base64.button_empy, key='6'), sg.Button('', image_data=img_base64.button_maquina, key='machine')],
          [sg.Button('', image_data=img_base64.button_empy, key='7'), sg.Button('', image_data=img_base64.button_empy, key='8'), sg.Button('', image_data=img_base64.button_empy, key='9'), sg.Button('', image_data=img_base64.button_zerar, key='zerar')]]

verifica_jogada = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}

window = sg.Window('Jogo da Velha', layout, grab_anywhere=True)
player = 1
jogadas = 0
x = []
o = []

while True:
    event, values = window.read()
    if event == '2p':
        continue #Vai vir por padrão para ser dois players, mas se optar por jogar contra maquina, esse botão vai voltar a ser 2 players
    elif event == 'machine':
        continue #Vai chamar uma função para jogar contra um Bot 

    elif event == 'zerar' or jogadas == 999:
        jogadas = 0
        player = 1
        x = []
        o = []
        for i in range(1,10):
            i = str(i)
            window[i].update(image_data=img_base64.button_empy)

    elif event and player == 1:
        window[event].update(image_data=img_base64.button_x)
        verifica_jogada[int(event)] = event
        print(verifica_jogada)
        x.append(event)
        jogadas += 1
        player = 2

    elif event and player == 2:
        window[event].update(image_data=img_base64.button_o)
        o.append(event)
        jogadas += 1
        player = 1

    # print(f'Casa {event} - Player {player} - N° Jogadas {jogadas}')
    # print(f'X = {x}')
    # print(f'O = {o}')

    if event == sg.WIN_CLOSED:
        break

window.close()

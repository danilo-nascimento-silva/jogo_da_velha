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

ganhador = []

def verifica_ganhador(lista):
    verifica = []
    for i in lista:
        for x in range(0, 7):
            for y in possibilidades[x]:
                if i == y:
                    print(i)
                    verifica.append(i)


sg.theme('LightBlue3')

layout = [[sg.Text('Jogo da velha')],
          [sg.Button('', image_data=img_base64.button_empy, key='1'), sg.Button('', image_data=img_base64.button_empy, key='2'), sg.Button('', image_data=img_base64.button_empy, key='3'), sg.Button('', image_data=img_base64.button_2_p, key='2p')],
          [sg.Button('', image_data=img_base64.button_empy, key='4'), sg.Button('', image_data=img_base64.button_empy, key='5'), sg.Button('', image_data=img_base64.button_empy, key='6'), sg.Button('', image_data=img_base64.button_maquina, key='machine')],
          [sg.Button('', image_data=img_base64.button_empy, key='7'), sg.Button('', image_data=img_base64.button_empy, key='8'), sg.Button('', image_data=img_base64.button_empy, key='9'), sg.Button('', image_data=img_base64.button_zerar, key='zerar')]]

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
        x.append(event)
        jogadas += 1
        player = 2
        if jogadas > 3:
            verifica_ganhador(x)

    elif event and player == 2:
        window[event].update(image_data=img_base64.button_o)
        o.append(event)
        jogadas += 1
        player = 1
        if jogadas > 3:
            verifica_ganhador(o)

    # print(f'Casa {event} - Player {player} - N° Jogadas {jogadas}')
    # print(f'X = {x}')
    # print(f'O = {o}')

    if event == sg.WIN_CLOSED:
        break

window.close()

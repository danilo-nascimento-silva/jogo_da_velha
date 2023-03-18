import PySimpleGUI as sg
import img_base64

def verifica_ganhador_x():
    global vencedor 
    if verifica_jogada[1] == 1 and verifica_jogada[2]  == 1 and verifica_jogada[3] == 1: vencedor = 1
    elif verifica_jogada[4] == 1 and verifica_jogada[5]  == 1 and verifica_jogada[6] == 1: vencedor = 1
    elif verifica_jogada[7] == 1 and verifica_jogada[8]  == 1 and verifica_jogada[9] == 1: vencedor = 1
    elif verifica_jogada[1] == 1 and verifica_jogada[4]  == 1 and verifica_jogada[7] == 1: vencedor = 1
    elif verifica_jogada[2] == 1 and verifica_jogada[5]  == 1 and verifica_jogada[8] == 1: vencedor = 1
    elif verifica_jogada[3] == 1 and verifica_jogada[6]  == 1 and verifica_jogada[9] == 1: vencedor = 1
    elif verifica_jogada[1] == 1 and verifica_jogada[5]  == 1 and verifica_jogada[9] == 1: vencedor = 1
    elif verifica_jogada[3] == 1 and verifica_jogada[5]  == 1 and verifica_jogada[7] == 1: vencedor = 1
    return 

def verifica_ganhador_o():
    global vencedor 
    if verifica_jogada[1] == 2 and verifica_jogada[2]  == 2 and verifica_jogada[3] == 2: vencedor = 2
    elif verifica_jogada[4] == 2 and verifica_jogada[5]  == 2 and verifica_jogada[6] == 2: vencedor = 2
    elif verifica_jogada[7] == 2 and verifica_jogada[8]  == 2 and verifica_jogada[9] == 2: vencedor = 2
    elif verifica_jogada[1] == 2 and verifica_jogada[4]  == 2 and verifica_jogada[7] == 2: vencedor = 2
    elif verifica_jogada[2] == 2 and verifica_jogada[5]  == 2 and verifica_jogada[8] == 2: vencedor = 2
    elif verifica_jogada[3] == 2 and verifica_jogada[6]  == 2 and verifica_jogada[9] == 2: vencedor = 2
    elif verifica_jogada[1] == 2 and verifica_jogada[5]  == 2 and verifica_jogada[9] == 2: vencedor = 2
    elif verifica_jogada[3] == 2 and verifica_jogada[5]  == 2 and verifica_jogada[7] == 2: vencedor = 2
    return 

sg.theme('LightBlue3')

layout = [[sg.Text('Jogo da velha')],
          [sg.Button('', image_data=img_base64.button_empy, key='1'), sg.Button('', image_data=img_base64.button_empy, key='2'), sg.Button('', image_data=img_base64.button_empy, key='3'), sg.Button('', image_data=img_base64.button_2_p, key='2p')],
          [sg.Button('', image_data=img_base64.button_empy, key='4'), sg.Button('', image_data=img_base64.button_empy, key='5'), sg.Button('', image_data=img_base64.button_empy, key='6'), sg.Button('', image_data=img_base64.button_maquina, key='machine')],
          [sg.Button('', image_data=img_base64.button_empy, key='7'), sg.Button('', image_data=img_base64.button_empy, key='8'), sg.Button('', image_data=img_base64.button_empy, key='9'), sg.Button('', image_data=img_base64.button_zerar, key='zerar')]]


verifica_jogada = {1: 0, 2: 0, 3: 0, 
                   4: 0, 5: 0, 6: 0, 
                   7: 0, 8: 0, 9: 0}

window = sg.Window('Jogo da Velha', layout, grab_anywhere=True)
player = 1
jogadas = 0
vencedor = 0

while True:
    event, values = window.read()
    if event == '2p':
        continue #Vai vir por padrão para ser dois players, mas se optar por jogar contra maquina, esse botão vai voltar a ser 2 players
    elif event == 'machine':
        continue #Vai chamar uma função para jogar contra um Bot 

    elif event == 'zerar' or event == 'ok':
        player = 1
        vencedor = False
        for i in range(1,10):
            verifica_jogada[i] = 0
            i = str(i)
            window[i].update(image_data=img_base64.button_empy)

    elif event and player == 1:
        if verifica_jogada[int(event)] == 1 or verifica_jogada[int(event)] == 2:
            player = 1 
            continue
        else:
            window[event].update(image_data=img_base64.button_x)
            verifica_jogada[int(event)] = 1
            jogadas += 1
            if jogadas >= 3:
                verifica_ganhador_x()
            player = 2

    elif event and player == 2:
        if verifica_jogada[int(event)]== 1 or verifica_jogada[int(event)]== 2:
            player = 2
            continue
        else:
            window[event].update(image_data=img_base64.button_o)
            verifica_jogada[int(event)] = 2
            if jogadas >= 3:
                verifica_ganhador_o()
            player = 1
    
    if vencedor == 1:
        for i in range(1,10):
            i = str(i)
            window[i].update(image_data=img_base64.button_x)    

    if vencedor == 2:
        for i in range(1,10):
            i = str(i)
            window[i].update(image_data=img_base64.button_o)        

    if event == sg.WIN_CLOSED:
        break

window.close()

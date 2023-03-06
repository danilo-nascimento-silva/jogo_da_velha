import PySimpleGUI as sg
import img_base64

sg.theme('LightBlue3')

layout = [[sg.Text('Jogo da velha')],
          [sg.Button('', image_data=img_base64.button_empy, key='1'), sg.Button('', image_data=img_base64.button_empy, key='2'), sg.Button('', image_data=img_base64.button_empy, key='3'), sg.Button('', image_data=img_base64.button_2_p, key='2p')],
          [sg.Button('', image_data=img_base64.button_empy, key='4'), sg.Button('', image_data=img_base64.button_empy, key='5'), sg.Button('', image_data=img_base64.button_empy, key='6'), sg.Button('', image_data=img_base64.button_maquina, key='machine')],
          [sg.Button('', image_data=img_base64.button_empy, key='7'), sg.Button('', image_data=img_base64.button_empy, key='8'), sg.Button('', image_data=img_base64.button_empy, key='9'), sg.Button('', image_data=img_base64.button_zerar, key='zerar')]]

window = sg.Window('Jogo da Velha', layout, grab_anywhere=True)
player = 1

while True:
    event, values = window.read()
    print(event, player)
    if event and player == 1:
        print('Jogada play 1')
        window[event].update(image_data=img_base64.button_x)
        player = 2

    elif event and player == 2:
        print('Jogada play 2')
        window[event].update(image_data=img_base64.button_o)
        player = 1

    if event == sg.WIN_CLOSED:
        break

window.close()



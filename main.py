import PySimpleGUI as sg
import qrcode

sg.theme('DarkBlue')

layout = [
    [sg.Text(f'QRcodeX', size=(25, 1), justification='center', font=('Helvetica', 14))],
    [sg.Text('Link', font=('Helvetica', 10)),
     sg.InputText(key='input', size=(35, 1), justification='r', font=('Lucida faz', 10))],
    [sg.Button('Create', font=('Helvetica', 10), size=(17, 3), button_color=('black', 'light blue')),
     sg.Button('Close', font=('Britannic', 10), size=(17, 3), button_color=('black', 'light blue'))],
    [sg.Image(r'Images\qrcreated.PNG', key=2, size=(290, 300))]

]
window = sg.Window('QRcodeX - Gerador de QRCode', layout, alpha_channel=0.9, grab_anywhere=True, no_titlebar=True, keep_on_top=True, auto_size_buttons=False)

while True:
    event, values = window.Read()

    if event == 'Close':
        window.close()
        sg.popup_auto_close('''Created by Cleo Menezes
        Github: github.com/CleoMenezes''', no_titlebar=True)
        break
    elif event == 'Create':
        values_on_input = (values['input'])
        img = qrcode.make(values_on_input, border=0, version=1)
        img.save(r'Images\qrcreated.PNG')
    window[2].Update(r'Images\qrcreated.PNG')

window.close()

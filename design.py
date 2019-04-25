import PySimpleGUI as sg
layout=[
    [sg.Text('Login')],
    [sg.Text('Email',size=(10,1)),sg.InputText()],
    [sg.Text("Password",size=(10,1)),sg.InputText(password_char='*')],
    [sg.Submit(),sg.Cancel()],
    [sg.Button("Chiudi")]
]
window=sg.Window("MANAGER OF CIGARETS",size=(1400,800),location=(0,0),no_titlebar='True').Layout(layout)
while(1):
    evento,values=window.Read()
    if evento == 'Chiudi':
        break;
    elif evento == 'Submit':
        print(values[0], values[1])
window.Close()

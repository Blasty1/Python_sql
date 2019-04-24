import PySimpleGUI as sg
layout=[
    [sg.Text('Login')],
    [sg.Text('Email',size=(10,1)),sg.InputText()],
    [sg.Text("Password",size=(10,1)),sg.InputText(password_char='*')],
    [sg.Submit(),sg.Cancel()],
    [sg.Button("Chiudi")]
]
window=sg.Window("MANAGER OF CIGARETS",size=(1350,700),location=(0,0)).Layout(layout)
while(1):
    evento,values=window.Read()
    if evento == 'chiudi':
        window.Close()
    elif evento == 'Submit':
        print(values[0], values[1])
window.Close()

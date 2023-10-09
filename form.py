import PySimpleGUI as rs

layout = [
    [rs.Text('Simple Form', font=('Helvetica', 20))],
    [rs.Text('Name:'), rs.InputText(key='name')],
    [rs.Text('Email:'), rs.InputText(key='email')],
    [rs.Text('Age:'), rs.InputText(key='age')],
    [rs.Button('Submit')],
    [rs.Text('', size=(20, 1), key='output_message')]
]


window = rs.Window('Simple Form', layout)


while True:
    event, values = window.read()

    if event == rs.WIN_CLOSED:
        break

    if event == 'Submit':
        name = values['name']
        email = values['email']
        age = values['age']

       
        output_message = f"Name: {name}, Email: {email}, Age: {age}"
        window['output_message'].update(output_message)


window.close()

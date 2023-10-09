import PySimpleGUI as rs

layout = [
    [rs.Text('Contact Us', font=('Helvetica', 20))],
    [rs.Text('Name:'), rs.InputText(key='name')],
    [rs.Text('Email:'), rs.InputText(key='email')],
    [rs.Text('Message:')],
    [rs.Multiline(key='message', size=(50, 10))],
    [rs.Button('Send'), rs.Button('Exit')]
]

window = rs.Window('Contact Us Form', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Send':
        name = values['name']
        email = values['email']
        message = values['message']

     
        print(f'Name: {name}\nEmail: {email}\nMessage: {message}\n')

# Close the window
window.close()
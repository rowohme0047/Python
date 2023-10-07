
Coding Exercise 1
Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 milliliters. 
For example, I was to call your function with foo(1) I would get an output of 29.57353. If I called it with  foo(5) I would get 147.86765, and so on.

def fluidTOmilliliters(ounces):
    milliliters = ounces * 29.57353
    return milliliters
res1 = fluidTOmilliliters(1)
print(res1)  
res2 = fluidTOmilliliters(5)
print(res2)


Coding Exercise 2
Create a desktop GUI program that gets feet and inches from the user and outputs the results in meters.

import PySimpleGUI as rs

def feet_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    return meters

sg.theme('LightBlue2')
layout = [
    [rs.Text('Enter feet:'), rs.InputText(key='-FEET-')],
    [rs.Text('Enter inches:'), rs.InputText(key='-INCHES-')],
    [rs.Button('Convert')],
    [rs.Text('', size=(20, 1), key='-OUTPUT-')],
]

window = rs.Window('Feet to Meters Converter', layout)
while True:
    event, values = window.read()

    if event == rs.WINDOW_CLOSED:
        break
    if event == 'Convert':
        feet = float(values['-FEET-']) if values['-FEET-'] else 0
        inches = float(values['-INCHES-']) if values['-INCHES-'] else 0
        meters = feet_to_meters(feet, inches)
        window['-OUTPUT-'].update(f'Result: {meters:.2f} meters')

window.close()

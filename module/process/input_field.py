import PySimpleGUI as sg

def input_field(text, isGUI=False, fieldType=None, options=[]):
    if isGUI:
        if fieldType == 'options':
            field = [sg.Radio(option, 1) for option in options]
        elif fieldType == 'range':
            field = [sg.Input(key='selected')]
        elif fieldType == 'number':
            field = [sg.Input(key='selected')]

        layout = [[sg.Text(text)],
                    field,
                    [sg.Button('Ok', key='submit')]]

        window = sg.Window('Input required', layout)
    
        event = ''

        while event != sg.WINDOW_CLOSED and event != 'submit':
            event, values = window.read()

            if event == 'submit':
                if fieldType == 'options':
                    value_list = list(values.values())
                    indx = 0
                    if True in value_list:
                        indx = value_list.index(True)
                    return options[indx]

                return values['selected']

        window.close()
        return None

    return input(text)
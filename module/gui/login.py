import PySimpleGUI as sg

from module.process import download

def render_login():
    # Define the window's contents
    layout = [[sg.Column([[sg.Text("User email", background_color='MediumPurple4')],
            [sg.Input(key='user_email')],
            [sg.Text("Password", background_color='MediumPurple4')],
            [sg.Input(key='password')],
            [sg.Text("Course link", background_color='MediumPurple4')],
            [sg.Input(key='url')],
            [sg.Text(size=(60,6), key='information_field', background_color='MediumPurple4')],
            [sg.Button('Log in and download', key='download_button'), sg.Button('Quit')]], size=(500, 350), element_justification='left', background_color='MediumPurple4')]]

    # Create the window background_color='5D38DB', button_color='7F00AC'
    
    window = sg.Window('Coursehunter.net Downloader', layout, font='Helvetica 13', background_color='MediumPurple4', button_color=['LightGrey', 'MediumPurple'])

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == "download_button":
            download.download(values['user_email'], values['password'], values['url'], window, 'information_field')

    # Finish up by removing from the screen
    window.close()
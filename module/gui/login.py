import PySimpleGUI as sg

from module.process import download

def render_login():
    # Define the window's contents
    layout = [[sg.Text("User email")],
            [sg.Input(key='user_email')],
            [sg.Text("Password")],
            [sg.Input(key='password')],
            [sg.Text("Course link")],
            [sg.Input(key='url')],
            [sg.Text(size=(60,6), key='information_field')],
            [sg.Button('Log in and download', key='download_button'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Coursehunter.net Downloader', layout)

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
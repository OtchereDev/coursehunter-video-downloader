import PySimpleGUI as sg

from module.create import create_folder, create_logger

from module.extractor import extract_video, extract_video_url

from module.extractor import extract_material_url_and_download , download_mode

from module.process import download

def initialise_gui():
    # Define the window's contents
    layout = [[sg.Text("User email")],
            [sg.Input(key='user_email')],
            [sg.Text("Password")],
            [sg.Input(key='password')],
            [sg.Text("Course link")],
            [sg.Input(key='url')],
            [sg.Text(size=(60,6), key='information_field')],
            [sg.Button('Start download', key='download_button'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Coursehunter.net Downloader', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == "download_button":
            window['download_button'].update(disabled=True)
            download.download(values['user_email'], values['password'], values['url'], window, 'information_field')
            window['download_button'].update(disabled=False)

    # Finish up by removing from the screen
    window.close()
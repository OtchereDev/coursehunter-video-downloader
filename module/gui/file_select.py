import PySimpleGUI as sg

from module.create import create_folder, create_logger

from module.extractor import extract_video, extract_video_url

from module.extractor import extract_material_url_and_download , download_mode

import threading

CHECKBOX_KEY_MOD = 'ck'
PROGRESS_BAR_KEY_MOD = 'pg'
PERCENT_KEY_MOD = 'percent'

# Threads for downloading
download_thread = None
course_mat_thread = None

def get_course_material_element():
    return {'progress_bar_key': 'progress_course_material', 'percent_key': 'percent_course_material'}

def render_file_select(zipped_title_url, course_path, logger_path, material_url, user_email):
    
    lessons_list = {}

    col_layout = []

    for title, url in zipped_title_url:
        checkbox_key = CHECKBOX_KEY_MOD + url
        progress_bar_key = PROGRESS_BAR_KEY_MOD + url
        percent_key = PERCENT_KEY_MOD + url

        lessons_list[url] = {'title': title, 'url': url, 'checkbox_key': checkbox_key, 'progress_bar_key': progress_bar_key, 'percent_key': percent_key}
        col_layout.append([sg.Checkbox(title, key=checkbox_key), sg.HSeparator(), sg.ProgressBar(100, size=(13, 10), key=progress_bar_key), sg.T(' ', size=(7, 1), key=percent_key)])

    layout = [[sg.Text("Logged in as:"), sg.Text(user_email)],
              [sg.Text("Select the files you want to download:")],
              [sg.Column(col_layout, scrollable=True, vertical_scroll_only=True, justification='c', size=(580, 440))],
              [sg.HorizontalSeparator()],
              [sg.Checkbox('Download course material', key='course_material', tooltip="Disabled if there is no materials", disabled=not bool(material_url)), 
                sg.HSeparator(), sg.ProgressBar(100, size=(13, 10), key='progress_course_material'), sg.T(' ', size=(7, 1), key='percent_course_material')],
              [sg.Column([[sg.B('Download', key='download'), sg.B('Quit', key='quit')]], justification='center')]]

    window = sg.Window('Coursehunter.net Downloader', layout, size=(700, 600))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "quit":
            break

        if event == "download":
            window['download'].update(disabled=True)

            # Disable download button and checkboxes until download is done
            _toggle_checkboxes(window, lessons_list, True)
            to_download = _get_files_to_download(window, values, lessons_list)

            download_thread = threading.Thread(target=download_mode.download_list_gui, args=[to_download, course_path, logger_path, window])
            download_thread.setDaemon(True)
            download_thread.start()

            #download_mode.download_list_gui(to_download, course_path, logger_path, window)

            if values['course_material']:
                extract_material_url_and_download.extract_course_material(material_url, course_path, 'course-material', True, 
                            get_course_material_element(), window)

            # Reenable them
            _toggle_checkboxes(window, lessons_list, False)
            window['download'].update(disabled=False)

        if event == "download_finished":
            window['download'].update(disabled=False)

    window.close()


def _toggle_checkboxes(window, lessons_list, disabled=False):
    for element in lessons_list:
        window[lessons_list[element]['checkbox_key']].update(disabled=disabled)

def _get_files_to_download(window, values, lessons_list):
    to_download = {}
    for element in lessons_list: 
        cur_element = lessons_list[element]
        if values[cur_element['checkbox_key']]:
            to_download[element] = cur_element

    return to_download

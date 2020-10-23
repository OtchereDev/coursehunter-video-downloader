
import requests

import os

from colorama import Fore

from colorama import Style

from module.extractor import download_iterator


def extract_video(url, title, path, isGUI=False, element={}, window=None):
    
    link = url

    lesson_number,title = format_vid_name(title)
    
    name = title

    title = os.path.join(path, title + '.mp4')
    
    chunk_size = 1025

    r = requests.get(link, stream=True)

    total_size = int(r.headers['content-length'])

    if not os.path.exists(fr'{title}'):

        if not isGUI:
            print(f'\nDownloading lesson {lesson_number} \
            titled {name}......\n')

        download_iterator.download_and_save_iterator(r, chunk_size, total_size, title, isGUI, window, element)

        if not isGUI:
            print(f'\n{Fore.GREEN}Done downloading {name}{Style.RESET_ALL}')

        return True

    else:

        if not isGUI:
            print(f'\n{Fore.RED}Already exist lesson {lesson_number} \
            titled {name}....{Style.RESET_ALL}\n')

        file_size = os.stat(title).st_size


        if file_size != total_size:
            if not isGUI:
                print('Updating old lesson...\n')

            download_iterator.download_and_save_iterator(r, chunk_size, total_size, title, isGUI, window, element)

            if not isGUI:
                print(f'{Fore.GREEN}Content updated.....{Style.RESET_ALL}\n')
        else:
            if isGUI:
                window[element['progress_bar_key']].update(100)
                window[element['percent_key']].update('-')

        if not isGUI:
            print('Moving to next lesson....\n')

 
def update_logger(logger_path,title):

    with open(logger_path,'a') as f:

        f.write(f'{title}\n')

    print(f'\n{Fore.BLUE} Logger file update{Style.RESET_ALL}')


def format_vid_name(title):

    lesson_number = title.split(')')[0].strip()

    for i in ['/',':','*','?','"','<','>','\\']:
        if i in title:
            title=title.replace(i,'')

    title=''.join(' '+ char if char.isupper() else \
        char.strip() for char in title).strip()

    return lesson_number, title
    
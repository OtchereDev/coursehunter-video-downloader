
import requests

import os

from colorama import Fore

from colorama import Style

from module.extractor import download_iterator

def extract_course_material_url(src):

    i = [ 
        a['href'] 
        for a in src.find_all('a',class_='btn mb-15 mr-10')
        ]

    if len(i) == 2:
        return i[1]


def extract_course_material(url, path, title='course-material', isGUI=False, element={}, window=None):

    title = os.path.join(path, title + '.zip')
    
    chunk_size = 1025

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])

    if not os.path.exists(fr'{title}'):

        if not isGUI:
            print(f'\nDownloading course material......\n')

        download_iterator.download_and_save_iterator(r, chunk_size, total_size, title, isGUI, window, element)

        if not isGUI:
            print(f'\n{Fore.GREEN}Done downloading course material {Style.RESET_ALL}')

    else:

        if not isGUI:
            print(f'\n{Fore.RED}Course material already exist....{Style.RESET_ALL}\n')

        file_size = os.stat(title).st_size


        if  file_size != total_size:
            if not isGUI:
                print('Updating old course material...\n')

            download_iterator.download_and_save_iterator(r, chunk_size, total_size, title, isGUI, window, element)
            
            if not isGUI:
                print(f'{Fore.GREEN}Content updated.....{Style.RESET_ALL}\n')
        else:
            if isGUI:
                window[element['progress_bar_key']].update(100)
                window[element['percent_key']].update('-')
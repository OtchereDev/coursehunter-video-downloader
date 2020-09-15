
import requests

import os

from tqdm import tqdm

from colorama import Fore

from colorama import Style


def extract_course_material_url(src):

    i = [ 
        a['href'] 
        for a in src.find_all('a',class_='btn mb-15 mr-10')
        ]

    if len(i) == 2:
        return i[1]


def extract_course_material(url,path,title='course-material'):

    title = os.path.join(path, title + '.zip')
    
    chunk_size = 1025

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])

    if not os.path.exists(fr'{title}'):

        print(f'\nDownloading course material......\n')

        with open(fr'{title}', 'wb') as f:

            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),
                total= total_size/chunk_size, unit='KB'):

                f.write(data)

        print(f'\n{Fore.GREEN}Done downloading course material {Style.RESET_ALL}')

    else:

        print(f'\n{Fore.RED}Course material already exist....{Style.RESET_ALL}\n')

        file_size = os.stat(title).st_size


        if  file_size != total_size:
            print('Updating old course material...\n')

            with open(title, 'wb') as f:

                for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),
                    total= total_size/chunk_size, unit='KB'):

                    f.write(data)
            
            print(f'{Fore.GREEN}Content updated.....{Style.RESET_ALL}\n')
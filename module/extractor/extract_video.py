
import requests

import os

from tqdm import tqdm

from colorama import Fore

from colorama import Style


def extract_video(url,title,path):
    
    link = url

    lesson_number,title = format_vid_name(title)
    
    name = title

    title = os.path.join(path, title + '.mp4')
    
    chunk_size = 1025

    r = requests.get(link, stream=True)

    total_size = int(r.headers['content-length'])

    if not os.path.exists(fr'{title}'):

        print(f'\nDownloading lesson {lesson_number} \
        titled {name}......\n')

        with open(fr'{title}', 'wb') as f:

            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),
                total= total_size/chunk_size, unit='KB'):

                f.write(data)

        print(f'\n{Fore.GREEN}Done downloading {name}{Style.RESET_ALL}')

        return True

    else:

        print(f'\n{Fore.RED}Already exist lesson {lesson_number} \
         titled {name}....{Style.RESET_ALL}\n')

        file_size = os.stat(title).st_size


        if  file_size != total_size:
            print('Updating old lesson...\n')

            with open(title, 'wb') as f:

                for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),
                    total= total_size/chunk_size, unit='KB'):

                    f.write(data)
            
            print(f'{Fore.GREEN}Content updated.....{Style.RESET_ALL}\n')

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
    
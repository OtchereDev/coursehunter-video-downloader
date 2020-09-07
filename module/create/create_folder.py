
import os

from colorama import Fore

from colorama import Style


def makeDownloadFolderPath(course_link:str):

    links_parts = course_link.split('/')

    base_folder = os.path.abspath('.')

    new_path = os.path.join(base_folder,links_parts[-1])

    return new_path


def createFolder(path: str):

    folder_path = path

    if  not os.path.exists(folder_path):

        print(f'{Fore.RED}Creating directory {folder_path}....{Style.RESET_ALL}')
        print()
        os.mkdir(folder_path)

    else:
        print(f'{Fore.YELLOW}Found directory {folder_path}.....{Style.RESET_ALL}')
        print()
        

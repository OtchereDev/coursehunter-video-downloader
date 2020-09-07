
import os

from colorama import Fore

from colorama import Style

def create_logger(course_path):

    logger_path = os.path.join(course_path,'video.txt')

    if not os.path.exists(logger_path):

        print(f'{Fore.RED}Creating logger file at {logger_path}....{Style.RESET_ALL}')

        with open(logger_path,'w'):

            pass
    
    else:

        print(f'{Fore.YELLOW}Found logger file {logger_path}....{Style.RESET_ALL}')

    return logger_path


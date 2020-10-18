from module.process import download

from module.gui import render_gui

from colorama import Fore

from colorama import Style


import sys

# By default use gui
gui_mode = True

if "-gui" in sys.argv:
    gui_mode = False

if "-cli" in sys.argv:
    gui_mode = False

from module.process import input_field


if gui_mode:
    render_gui.initialise_gui()
else:
    print(f'{Fore.GREEN}+++++++++++++++++++++++++++++++++++++++++++++++++++{Style.RESET_ALL}')
    print()
    print(f'{Fore.BLUE}         COURSEHUNTER DOWNLOADER{Style.RESET_ALL}')
    print()
    print(f'{Fore.GREEN}+++++++++++++++++++++++++++++++++++++++++++++++++++{Style.RESET_ALL}\n')

    user_email = input('Email : \n\t')
    print()
    password = input('Password : \n\t')
    print()
    course_link = input('Course_link : \n\t')
    print()

    download.download(user_email, password, course_link)

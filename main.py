from module.create import create_folder, create_logger

from module.extractor import extract_video, extract_video_url

from module.extractor import extract_material_url_and_download , download_mode

from colorama import Fore

from colorama import Style

import requests.exceptions

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

course_path = create_folder.makeDownloadFolderPath(course_link)

create_folder.createFolder(course_path)

logger_path = create_logger.create_logger(course_path)

try:

    src = extract_video_url.sign_in_and_extractHTML(user_email,password,course_link)

    search = extract_video_url.draw_out_script(src)

    try :

        break_with_title = extract_video_url.clean_out(search)

        zipped_title_url = extract_video_url.title_url(break_with_title)

        print(f'\nThere are {len(zipped_title_url)} lessons in this course !!!\n')

        download_type = input('Which type of download '
            + 'would you like to make: \n\t [S]ingle lesson, '
            + '[R]ange of lessons, [A]ll lessons:\n\t')

        if download_type.upper() == 'A':
            
            download_mode.download_all(zipped_title_url,course_path,logger_path)
        
        elif download_type.upper() =='R':
            
            user_range = input('Provide range of lesson to download:\n\t '
                + 'Use "," to seperate the range. eg. 1,20  :\n\t')
            
            download_mode.range_download(user_range,zipped_title_url,course_path,logger_path)

        elif download_type.upper() == 'S':
            
            user_esp = input('What a lesson number do you want eg. 10  :\n\t')

            download_mode.single_download(user_esp,zipped_title_url,course_path,logger_path)

        download_course_mat =input('Would you like to download the course material:'
                                    + '\n [Y]es to download or [N]o to skip: \n\t')

        if download_course_mat.upper()=='Y':
            
            material_url = extract_material_url_and_download.extract_course_material_url(src)

            if material_url:

                extract_material_url_and_download.extract_course_material(material_url,course_path)
            else:
                print('This course does not have materials attached !!!')

    except ValueError as ve:
        print('\nIncorrect log-in details...Retry with correct log-in details\n')
        print('Or it might be the url link to the course site\n')
        print('\n if not any of the above, report to github repo\n')

except requests.exceptions.ConnectionError as ce:

    print('\nYou are not connected to internet....Connect and retry\n')

except Exception as error:

    print(f'\nThere is an unknown error : "{error}"....Report issue github repo \n')


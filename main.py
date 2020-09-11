from module.create import create_folder, create_logger

from module.extractor import extract_video, extract_video_url, extract_material_url_and_download

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

        for title, url in zipped_title_url:

            url =str(url).strip('"')

            download = extract_video.extract_video(url,title,course_path)

            if download == True:

                extract_video.update_logger(logger_path, title)

        download_course_mat =input('Would you like to download the course material:'
                                    + '\n [Y]es to download or [N]o to skip: \n\t')

        if download_course_mat.upper()=='Y':
            
            material_url = extract_material_url_and_download.extract_course_material_url(src)

            extract_material_url_and_download.extract_course_material(material_url,course_path)

    except ValueError as ve:
        print('\nIncorrect log-in details...Retry with correct log-in details\n')
        print('Or it might be the url link to the course site\n')
        print('\n if not any of the above, report to github repo\n')

except requests.exceptions.ConnectionError as ce:

    print('\nYou are not connected to internet....Connect and retry\n')

except Exception as error:

    print(f'\nThere is an unknown error : "{error}"....Report issue github repo \n')


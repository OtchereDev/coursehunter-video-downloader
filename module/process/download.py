from colorama import Fore

from colorama import Style

from module.create import create_folder, create_logger

from module.extractor import extract_video, extract_video_url

from module.extractor import extract_material_url_and_download , download_mode

from module.gui import file_select

from module.process.display_text import display_text

import requests.exceptions

def download(user_email, password, course_link, window=None, information_field=None):
    isGUI = window != None

    course_path = create_folder.makeDownloadFolderPath(course_link)

    create_folder.createFolder(course_path)

    logger_path = create_logger.create_logger(course_path)

    try:

        src = extract_video_url.sign_in_and_extractHTML(user_email,password,course_link)

        search = extract_video_url.draw_out_script(src)

        try :

            break_with_title = extract_video_url.clean_out(search)

            zipped_title_url = extract_video_url.title_url(break_with_title)

            material_url = extract_material_url_and_download.extract_course_material_url(src)

            if isGUI:
                #window['file'].update(zipped_title_url[0])
                #window['path'].update(course_path)
                window.close()
                file_select.render_file_select(zipped_title_url, course_path, logger_path, material_url, user_email)

            else:

                print(f'\n{Fore.RED}There are {len(zipped_title_url)} lessons in this course !!!{Style.RESET_ALL}\n') 

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

                download_course_mat = input('Would you like to download the course material:'
                                            + '\n [Y]es to download or [N]o to skip: \n\t')

                if download_course_mat.upper()=='Y':

                    if material_url:

                        extract_material_url_and_download.extract_course_material(material_url, course_path, 'course-material', isGUI, file_select.get_course_material_element(), window)
                    else:
                        print('This course does not have materials attached !!!')

        except ValueError as ve:
            display_text('\nIncorrect log-in details...Retry with correct log-in details\n' 
                + 'Or it might be the url link to the course site\n' 
                + 'if not any of the above, report to github repo\n', window, information_field)

    except requests.exceptions.ConnectionError as ce:

        display_text('\nYou are not connected to internet....Connect and retry\n', window, information_field)

    except Exception as error:

        display_text(f'\nThere is an unknown error : "{error}"....Report issue github repo \n', window, information_field)
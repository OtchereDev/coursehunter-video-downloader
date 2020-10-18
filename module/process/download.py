from module.create import create_folder, create_logger

from module.extractor import extract_video, extract_video_url

from module.extractor import extract_material_url_and_download , download_mode

from module.process.display_text import display_text

from module.process.input_field import input_field

import requests.exceptions

def download(user_email, password, course_link, window=None, information_field=None):
    isGUI = window == None

    course_path = create_folder.makeDownloadFolderPath(course_link)

    create_folder.createFolder(course_path)

    logger_path = create_logger.create_logger(course_path)

    try:

        src = extract_video_url.sign_in_and_extractHTML(user_email,password,course_link)

        search = extract_video_url.draw_out_script(src)

        try :

            break_with_title = extract_video_url.clean_out(search)

            zipped_title_url = extract_video_url.title_url(break_with_title)

            display_text(f'\nThere are {len(zipped_title_url)} lessons in this course !!!\n', window, information_field)

            download_type = input_field('Which type of download '
                + 'would you like to make: \n\t [S]ingle lesson, '
                + '[R]ange of lessons, [A]ll lessons:\n\t', isGUI, 'options', ['Single Lesson', 'Range of lessons', 'All lessons'])

            if download_type.upper() == 'A':
                
                download_mode.download_all(zipped_title_url,course_path,logger_path)
            
            elif download_type.upper() =='R':
                
                user_range = input_field('Provide range of lesson to download:\n\t '
                    + 'Use "," to seperate the range. eg. 1,20  :\n\t', isGUI, 'range')
                
                download_mode.range_download(user_range,zipped_title_url,course_path,logger_path)

            elif download_type.upper() == 'S':
                
                user_esp = input_field('What a lesson number do you want eg. 10  :\n\t', isGUI, 'number')

                download_mode.single_download(user_esp,zipped_title_url,course_path,logger_path)

            download_course_mat = input_field('Would you like to download the course material:'
                                        + '\n [Y]es to download or [N]o to skip: \n\t', isGUI, 'options', ['Yes', 'No'])

            if download_course_mat.upper()=='Y':
                
                material_url = extract_material_url_and_download.extract_course_material_url(src)

                if material_url:

                    extract_material_url_and_download.extract_course_material(material_url,course_path)
                else:
                    display_text('This course does not have materials attached !!!', window, information_field)

        except ValueError as ve:
            display_text('\nIncorrect log-in details...Retry with correct log-in details\n' 
                + 'Or it might be the url link to the course site\n' 
                + 'if not any of the above, report to github repo\n', window, information_field)

    except requests.exceptions.ConnectionError as ce:

        display_text('\nYou are not connected to internet....Connect and retry\n', window, information_field)

    except Exception as error:

        display_text(f'\nThere is an unknown error : "{error}"....Report issue github repo \n', window, information_field)
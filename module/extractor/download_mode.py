
from module.extractor import extract_video


def single_download(esp_num,zipped_title_url,course_path,logger_path):

    download_episode = [zipped_title_url[int(esp_num)-1]]

    for title, url in download_episode:

        url =str(url).strip('"')

        download = extract_video.extract_video(url,title,course_path)

        if download == True:

            extract_video.update_logger(logger_path, title)


def range_download(user_range:str ,zipped_title_url,course_path,logger_path):

    user_range = user_range.split(',')

    esp_start,esp_end = int(user_range[0]),int(user_range[1])

    download_range = zipped_title_url[esp_start-1 : esp_end+1]

    for title, url in download_range:

        url =str(url).strip('"')

        download = extract_video.extract_video(url,title,course_path)

        if download == True:

            extract_video.update_logger(logger_path, title)


def download_all(zipped_title_url,course_path,logger_path):

    for title, url in zipped_title_url:

        url =str(url).strip('"')

        download = extract_video.extract_video(url,title,course_path)

        if download == True:

            extract_video.update_logger(logger_path, title)

def download_list_gui(to_download, course_path, logger_path, window):
    for element in to_download:
        cur_element = to_download[element]
        url = str(cur_element['url']).strip('"')

        download = extract_video.extract_video(url, cur_element['title'], course_path, True, cur_element, window)

        if download == True:

            extract_video.update_logger(logger_path, cur_element['title'])
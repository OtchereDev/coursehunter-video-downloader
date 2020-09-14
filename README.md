# COURSEHUNTER DOWNLOADER (CH-DOWNLOAD)

# Download videos (course) from coursehunter.net

### How to install needed packages ( Python 3.\* required):

```sh
~ git clone https://github.com/OtchereDev/coursehunter-video-downloader.git
~ cd coursehunter-video-downloader
~ pip install -r requirements.txt
```

### Download premium courses (required paid subscription)

```sh
# from downloaded directory
~ python main.py
```

### User Inputs:

```sh

Email: email for login

Password: password for login

Course_links : url to the course (eg. https://coursehunter.net/course_name)

Which type of download would you like to make: A  to download all course lesson
                                               R  to download a range of course lesson eg. 10,15
                                               S to download a single lesson eg. 5

Would you like to download the course material: Y to download course material 
                                                N or Enter skip downloading it

```

## Author:

- [Oliver Otchere](https://github.com/OtchereDev)

### Inspiration:

- This is a python port of [ch-download](https://github.com/alekseylovchikov/ch-download) by [Alekseylovchikov](https://github.com/alekseylovchikov) but has support for current restructuring of the website

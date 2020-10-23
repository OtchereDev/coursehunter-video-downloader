
from robobrowser import RoboBrowser

import warnings

warnings.simplefilter('ignore', UserWarning)



def sign_in_and_extractHTML(user_email: str,password: str, course_link:str):

    br = RoboBrowser()

    br.open('https://coursehunter.net/sign-in')

    form = br.get_form(class_='auth')

    form['e_mail']= user_email.strip()

    form['password'] = password.strip()

    br.submit_form(form)

    br.open(course_link.strip())

    src = br.parsed

    return src



def draw_out_script(src):

    search = str(src.find_all('script')[2:3])

    return search



def clean_out(original_text:str):

    original_text = '''{}'''.format(original_text)

    merge_together = original_text.replace('\n','')

    merge_together = merge_together.replace(' ','')

    begin = merge_together.index('1)')

    leftover_aft_firstcut = merge_together[begin:-1]

    last = leftover_aft_firstcut.index('poster') - 2

    final_leftover = leftover_aft_firstcut[:last]

    break_with_title = final_leftover.split('{"title"')

    return break_with_title



def title_url(break_with_title: list):

    
    links=[]

    title=[]

    

    for dict_ in break_with_title:

        dict_ = dict_.strip()
        if dict_[0] ==':':
            dict_ =dict_.lstrip(':"')
        if dict_[-1:] ==',':
            dict_  = dict_.rstrip('},')


        parts_of_dict = dict_.split(',"')

        for k in parts_of_dict:
            if k[0:5]=='file"':
                main_link = k.split(':',maxsplit=1)[-1]
                links.append(main_link) 

            if k[1]==')' or k[2]==')' or k[3]==')' :
                main_title = k .split('|')
                title.append(main_title[0])

    t_l=[]

    for index,i in enumerate(title):
        t_l.append((i,links[index]))

    return t_l

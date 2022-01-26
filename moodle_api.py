#!/usr/bin/env python3
# for moodle 3.9

from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pyvirtualdisplay import Display

""" Firefox settings """
display = Display(visible=0, size=(800, 600))
display.start()
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, log_path="/tmp/geckodriver.log")

""" env """
moodle_url = 'https://ict-i.el.kyutech.ac.jp'

def login(id, passwd):
    try:
        driver.get(moodle_url + '/login/index.php')
        driver.set_page_load_timeout(30)

        elem = driver.find_element_by_id('username')
        elem.clear()
        elem.send_keys(id)

        elem = driver.find_element_by_id('password')
        elem.clear()
        elem.send_keys(passwd)

        elem = driver.find_element_by_id('loginbtn')
        elem.click()
        
    except WebDriverException:
        print('[Err] WebDriverException@login')

    # login check
    html = driver.page_source
    if 'ダッシュボード'  or 'Dashboard' or '个人主页' or '강의 현황' in html:
        print('[+] moodle login success !')
    else:
        print('[Err] moodle login failed...')


def get_upcoming_tasks():
    try:
        driver.get(moodle_url + '/calendar/view.php?view=upcoming')
        driver.set_page_load_timeout(30)
    except WebDriverException:
        print('[Err] WebDriverException@get_upcoming_tasks')
        return None

    tasks = {}
    events = driver.find_elements_by_class_name('event')# list
    print(events)
    for index, event in enumerate(events):
        task = event.get_attribute('data-event-title')
        date = event.find_elements_by_xpath('./div[1]/div[1]/span[1]')
        date = date[0].text
        i = {
            'name': task,
            'date': date,
            'delta': get_delta(date)
        }
        tasks[str(index)] = i
    return tasks


def get_delta(date):
    """ Returns the timedelta between the submit time and now"""
    now = datetime.now()
    when = datetime.strptime(date, '%d/%m/%Y, %H:%M')
    return when - now


def from_dict_to_text(tasks_dict):
    """ Help method to represent the tasks as text """
    if tasks_dict is None:
        return None

    tasks = []
    for _, task in tasks_dict.items():
        name = task['name']
        date = task['date']
        delta = task['delta']
        tasks.append(f'*{name}* by *{date}*.\n'
                     f'*{delta}* have left!\n')
    if len(tasks) == 0:
        message = None
    else:
        message = '\n'.join(tasks)
    return message


def from_dict_to_set(tasks_dict):
    """ Help method to represent the tasks as set of names """
    if tasks_dict is None:
        return None

    tasks = set()
    for _, task in tasks_dict.items():
        tasks.add(task['name'])

    return tasks


def get_upcoming_tasks_as_text():
    """ Same as get_upcoming_tasks() but as text """
    return from_dict_to_text(get_upcoming_tasks())


def get_upcoming_tasks_as_set_of_names():
    """ Same as get_upcoming_tasks() but as set of names"""
    return from_dict_to_set(get_upcoming_tasks())


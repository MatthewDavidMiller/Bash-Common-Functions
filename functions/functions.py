# Credits
# https://www.w3schools.com/python/gloss_python_global_variables.asp
# Eric Wilson, https://stackoverflow.com/questions/6711567/how-to-use-python-regex-to-replace-using-captured-group
# Hari Menon, https://stackoverflow.com/questions/19243020/in-python-get-the-output-of-system-command-as-a-string

import subprocess
import os
import re


def lock_root():
    subprocess.call(['passwd', '--lock', 'root'])


def get_username():
    global user_name
    user_name = subprocess.call(['logname'])


def get_interface_name():
    global interface
    ip_route = subprocess.getoutput([r'ip route get 8.8.8.8'])
    interface_regex = re.compile('.*' + r'dev' + '\s' + '(\S*).*', flags=re.S)
    interface = interface_regex.sub(r'\1', ip_route)
    print(r'Interface name is ' + interface)

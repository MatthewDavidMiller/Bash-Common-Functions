# Credits
# https://www.geeksforgeeks.org/create-an-empty-file-using-python/
# https://www.geeksforgeeks.org/create-a-directory-in-python/
# https://pythonguides.com/python-copy-file/

import subprocess
import re
import os
import shutil


def log_rotate_configure(user_name):

    subprocess.call(['apt-get', 'install', '-y', 'logrotate'])

    with open('/etc/logrotate.conf', "w") as opened_file:
        pass

    os.mkdir(r'/home/' + user_name + r'/config_backups')

    shutil.copyfile(r'/etc/logrotate.conf', r'/home/' +
                    user_name + r'/config_backups/logrotate.conf.backup')

    daily_regex = str('(^\s*[#]*\s*' + r'daily' + '\s*$)|(^\s*[#]*\s*' +
                      r'weekly' + '\s*$)|(^\s*[#]*\s*' + r'monthly' + '\s*$)')

    daily_replace = str(
        r'daily')

    minsize_regex = str('^\s*[#]*\s*' + r'minsize' + '.*$')

    minsize_replace = str(r'minsize 100M')

    rotate_regex = str('^\s*[#]*\s*' + r'rotate' + '\s*[0-9]*$')

    rotate_replace = str(r'rotate 4')

    compress_regex = str('^\s*[#]*\s*' + r'compress' + '\s*$')

    compress_replace = str(r'compress')

    create_regex = str('^\s*[#]*\s*' + r'create' + '\s*$')

    create_replace = str(r'create')

    with open('/etc/logrotate.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/logrotate.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(daily_regex, daily_replace, line,))

            if daily_replace == line.strip():
                break
        else:
            opened_file.write(daily_replace + '\n')

    with open('/etc/logrotate.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/logrotate.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(minsize_regex, minsize_replace, line,))

            if minsize_replace == line.strip():
                break
        else:
            opened_file.write(minsize_replace + '\n')

    with open('/etc/logrotate.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/logrotate.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(rotate_regex, rotate_replace, line,))

            if rotate_replace == line.strip():
                break
        else:
            opened_file.write(rotate_replace + '\n')

    with open('/etc/logrotate.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/logrotate.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(compress_regex, compress_replace, line,))

            if compress_replace == line.strip():
                break
        else:
            opened_file.write(compress_replace + '\n')

    with open('/etc/logrotate.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/logrotate.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(create_regex, create_replace, line,))

            if create_replace == line.strip():
                break
        else:
            opened_file.write(create_replace + '\n')

# Credits to https://www.w3schools.com/python/gloss_python_function_arguments.asp
# Credits to https://www.w3schools.com/python/python_variables.asp
# Credits to aIKid, https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python
# Credits to https://www.techbeamers.com/python-multiline-string/
# Credits to https://www.w3schools.com/python/python_functions.asp
# Credits to https://pythonguides.com/python-write-variable-to-file/
# Credits to Ned Batchelder, https://stackoverflow.com/questions/6930982/how-to-use-a-variable-inside-a-regular-expression

import re


def apt_configure_auto_updates(release_name):

    update_regex = '.*' + r'Unattended-Upgrade::Origins-Pattern' + '.*\n.*' + \
        r'origin=' + '.*\n.*' + r'origin=' + '.*\n.*' + r'origin=' + '.*\n.*'

    update_replace = r'Unattended-Upgrade::Origins-Pattern {' + '\n' + r'"origin=Debian,n=' + re.escape(release_name) + r',l = Debian";' + '\n' + r'"origin=Debian,n=' + \
        re.escape(release_name) + r',l = Debian-Security";' '\n' r'"origin=Debian,n=' + \
        re.escape(release_name) + r'-updates";' + '\n' + r'};' + '\n'

    # Enable autoupdates
    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(update_regex, update_replace, line))

            if (update_replace) == line.strip():
                break
            else:
                opened_file.write(update_replace)

# Credits to https://www.w3schools.com/python/gloss_python_function_arguments.asp
# Credits to https://www.w3schools.com/python/python_variables.asp
# Credits to aIKid, https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python
# Credits to https://www.techbeamers.com/python-multiline-string/
# Credits to https://www.w3schools.com/python/python_functions.asp
# Credits to https://pythonguides.com/python-write-variable-to-file/
# Credits to Ned Batchelder, https://stackoverflow.com/questions/6930982/how-to-use-a-variable-inside-a-regular-expression
# Credits to https://docs.python.org/3/library/re.html
# Credits to https://regex101.com/

import re


def apt_configure_auto_updates(release_name, origin_name):

    update_regex = str(r'Unattended-Upgrade::Origins-Pattern {' + '.*' + r'};')

    update_replace = str(r'Unattended-Upgrade::Origins-Pattern {' + '\n' + r'"origin=' + origin_name + r',n=' + release_name + r',l = Debian";' + '\n' +
                         r'"origin=' + origin_name + r',n=' + release_name + r',l = Debian-Security";' '\n' r'"origin=' + origin_name + r',n=' +
                         release_name + r'-updates";' + '\n' + r'};')

    reboot_regex = str('.*' + r'Unattended-Upgrade::Automatic-Reboot' + '.*')

    reboot_replace = str(
        r'Unattended-Upgrade::Automatic-Reboot "true";')

    reboot_time_regex = str(
        '.*' + r'Unattended-Upgrade::Automatic-Reboot-Time' + '.*')

    reboot_time_replace = str(
        r'Unattended-Upgrade::Automatic-Reboot-Time "04:00";')

    # Enable autoupdates
    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(update_regex, update_replace, line, flags=re.S))

            if update_replace == line.strip():
                break
        else:
            opened_file.write(update_replace + '\n')

    # Allow reboots
    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(reboot_regex, reboot_replace, line))

            if reboot_replace == line.strip():
                break
        else:
            opened_file.write(reboot_replace + '\n')

    # Set reboot time
    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/apt/apt.conf.d/50unattended-upgrades', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(reboot_time_regex, reboot_time_replace, line))

            if reboot_time_replace == line.strip():
                break
        else:
            opened_file.write(reboot_time_replace + '\n')

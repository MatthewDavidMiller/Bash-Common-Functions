# Credits
# https://www.w3schools.com/python/gloss_python_global_variables.asp
# Eric Wilson, https://stackoverflow.com/questions/6711567/how-to-use-python-regex-to-replace-using-captured-group
# Hari Menon, https://stackoverflow.com/questions/19243020/in-python-get-the-output-of-system-command-as-a-string
# https://www.tutorialspoint.com/python/os_symlink.htm
# https://www.tutorialspoint.com/python/os_chown.htm
# https://www.geeksforgeeks.org/pwd-module-in-python/
# https://stackoverflow.com/questions/33386553/python-chown-folder-by-username
# https://www.geeksforgeeks.org/python-os-getlogin-method/

import subprocess
import os
import re
import pwd


def lock_root():
    subprocess.call(['passwd', '--lock', 'root'])


def get_username():
    global user_name
    user_name = os.getlogin()


def get_interface_name():
    global interface
    ip_route = subprocess.getoutput([r'ip route get 8.8.8.8'])
    interface_regex = re.compile('.*' + r'dev' + '\s' + '(\S*).*', flags=re.S)
    interface = interface_regex.sub(r'\1', ip_route)
    print(r'Interface name is ' + interface)


def fix_apt_packages():
    subprocess.call(['dpkg', r'--configure', '-a'])


def install_packages(packages):
    subprocess.call([r'apt-get', r'update'])
    subprocess.call([r'apt-get', r'upgrade', '-y'])
    subprocess.call([r'apt-get', 'install', '-y', packages])


def get_ipv6_link_local_address():
    global ipv6_link_local_address
    ip_address = subprocess.getoutput([r'ip address'])
    ipv6_link_local_address_regex = re.compile(
        '.*' + r'inet6' + '\s*(fe80:*[a-z,0-9]*:*[a-z,0-9]*:*[a-z,0-9]*:*[a-z,0-9]*).*', flags=re.S)
    ipv6_link_local_address = ipv6_link_local_address_regex.sub(
        r'\1', ip_address)
    print(r'ipv6 link local address is ' + ipv6_link_local_address)


def set_timezone():
    sym_source = r'/usr/share/zoneinfo/America/New_York'
    sym_dest = r'/etc/localtime'
    os.symlink(sym_source, sym_dest)


def set_language():
    set_language_regex = str('.*' + r'LANG=' + '.*')

    set_language_replace = str(r'LANG=en_US.UTF-8')

    with open('/etc/locale.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/locale.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(set_language_regex, set_language_replace, line))
            if set_language_replace == line.strip():
                break
        else:
            opened_file.write(set_language_replace + '\n')


def set_hostname(device_hostname):
    device_hostname_regex = str('.*')

    device_hostname_replace = str(device_hostname)

    with open('/etc/hostname', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/hostname', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(device_hostname_regex, device_hostname_replace, line, flags=re.S))
            if device_hostname_replace == line.strip():
                break
        else:
            opened_file.write(device_hostname_replace + '\n')


def setup_hosts_file(device_hostname):
    line_1_regex = '.*' + r'127.0.0.1 localhost' + '.*'

    line_1_replace = r'127.0.0.1 localhost'

    line_2_regex = '.*' + r'::1' + '.*'

    line_2_replace = r'::1 localhost'

    line_3_regex = '.*' + r'127.0.0.1 ' + device_hostname + '.*'

    line_3_replace = r'127.0.0.1 ' + device_hostname + \
        r'.localdomain ' + device_hostname

    with open('/etc/hosts', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/hosts', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(line_1_regex, line_1_replace, line))
            if line_1_replace == line.strip():
                break
        else:
            opened_file.write(line_1_replace + '\n')

    with open('/etc/hosts', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/hosts', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(line_2_regex, line_2_replace, line))
            if line_2_replace == line.strip():
                break
        else:
            opened_file.write(line_2_replace + '\n')

    with open('/etc/hosts', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/hosts', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(line_3_regex, line_3_replace, line))
            if line_3_replace == line.strip():
                break
        else:
            opened_file.write(line_3_replace + '\n')


def create_user(user_name):
    subprocess.call(['useradd', '-m', user_name])
    print(r'Set the password for ' + user_name)
    subprocess.call(['passwd', user_name])
    os.mkdir(r'/home/' + user_name)
    uid = pwd.getpwnam(user_name).pw_uid
    gid = pwd.getpwnam(user_name).pw_gid
    os.chown(r'/home/' + uid, gid)


def allow_user_group_sudo(name):
    wheel_regex = '.*' + name + r' ALL=(ALL) ALL'
    wheel_replace = name + r' ALL=(ALL) ALL'

    with open('/etc/sudoers', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/sudoers', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(wheel_regex, wheel_replace, line))
            if wheel_replace == line.strip():
                break
        else:
            opened_file.write(wheel_replace + '\n')


def add_user_to_group(user_name, group):
    subprocess.call(['usermod', '-G', group, user_name])


def set_shell_bash(user_name):
    subprocess.call(['chsh', '-s', r'/bin/bash'])
    subprocess.call(['chsh', '-s', r'/bin/bash', user_name])


def get_linux_headers():
    global linux_headers
    linux_headers = r'linux-headers-' + subprocess.getoutput(['uname', '-r'])


def add_backports_repository(release_name):
    backports_repository_text = r'deb https://mirrors.wikimedia.org/debian/ ' + release_name + r'-backports main' + \
        '\n' + r'deb-src https://mirrors.wikimedia.org/debian/ ' + \
        release_name + r'-backports main'

    with open('/etc/apt/sources.list', "w") as opened_file:
        opened_file.write(backports_repository_text + '\n')


def configure_ddclient(domain_name):
    print(r'Enter dynamic dns username: ')
    user_name = input()
    print(r'Enter dynamic dns password: ')
    password = input()

    dyndns2_regex = '.*' + r'protocol=' + '.*'
    dyndns2_replace = r'protocol=dyndns2'
    useweb_regex = '.*' + r'use=' + '.*'
    useweb_replace = r'use=web'
    server_regex = '.*' + r'server=' + '.*'
    server_replace = r'server=domains.google.com'
    ssl_regex = '.*' + r'ssl=' + '.*'
    ssl_replace = r'ssl=yes'
    login_regex = '.*' + r'login=' + '.*'
    login_replace = r'login=' + user_name
    password_regex = '.*' + r'password=' + '.*'
    password_replace = r'password=' + password
    domain_regex = '.*' + domain_name + '.*'
    domain_replace = domain_name

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(dyndns2_regex, dyndns2_replace, line))
            if dyndns2_replace == line.strip():
                break
        else:
            opened_file.write(dyndns2_replace + '\n')

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(useweb_regex, useweb_replace, line))
            if useweb_replace == line.strip():
                break
        else:
            opened_file.write(useweb_replace + '\n')

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(server_regex, server_replace, line))
            if server_replace == line.strip():
                break
        else:
            opened_file.write(server_replace + '\n')

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(ssl_regex, ssl_replace, line))
            if ssl_replace == line.strip():
                break
        else:
            opened_file.write(ssl_replace + '\n')

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(login_regex, login_replace, line))
            if login_replace == line.strip():
                break
        else:
            opened_file.write(login_replace + '\n')

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(password_regex, password_replace, line))
            if password_replace == line.strip():
                break
        else:
            opened_file.write(password_replace + '\n')

    with open('/etc/ddclient.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ddclient.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(domain_regex, domain_replace, line))
            if domain_replace == line.strip():
                break
        else:
            opened_file.write(domain_replace + '\n')


def list_partitions():
    subprocess.call([r'lsblk', r'-f'])


def apt_clear_cache():
    subprocess.call([r'apt-get', r'clean'])


def set_password():
    print(r'Set root password: ')
    subprocess.call([r'passwd', r'root'])

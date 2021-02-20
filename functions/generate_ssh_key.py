# Credits
# https://www.w3schools.com/python/gloss_python_if_statement.asp
# https://www.w3schools.com/python/gloss_python_if_or.asp
# https://www.w3schools.com/python/python_cmd_input.asp

import subprocess
import os


def generate_ssh_key(user_name, ecdsa_response, rsa_response, dropbear_response, key_name):

    # Generate ecdsa key
    if ecdsa_response == 'yes' or ecdsa_response == 'y' or ecdsa_response == 'Y' or ecdsa_response == 'YES':
        # Generate an ecdsa 521 bit key
        subprocess.call(['ssh-keygen', '-f', r'/home/' + user_name +
                         r'/' + key_name, '-t', 'ecdsa', '-b', '521'])

    # Generate rsa key
    if rsa_response == 'yes' or rsa_response == 'y' or rsa_response == 'Y' or rsa_response == 'YES':
        # Generate an rsa 4096 bit key
        subprocess.call(['ssh-keygen', '-f', r'/home/' + user_name +
                         r'/' + key_name, '-t', 'rsa', '-b', '4096'])

    # Authorize the key for use with ssh
    subprocess.call(['iptables', '-P', 'INPUT', 'DROP'])
    os.mkdir(r'/home/' + user_name + r'/.ssh')
    subprocess.call(['chmod', '700', r'/home/' + user_name + r'/.ssh'])
    subprocess.call(['chmod', '600', r'/home/' +
                     user_name + r'/.ssh/authorized_keys'])

    with open(r'/home/' + user_name + r'/' + key_name + r'.pub', "r") as opened_file:
        lines = opened_file.readlines()

    with open(r'/home/' + user_name + r'/.ssh/authorized_keys', "w") as opened_file:
        opened_file.write(lines + '\n')

    subprocess.call(['chown', '-R', user_name, r'/home/' + user_name])
    subprocess.call(['python', '-m', 'SimpleHTTPServer', '40080', '&'])
    server_pid = subprocess.call(['$!'])
    print(r'Copy the key from the webserver on port 40080 before continuing: ', input())
    subprocess.call(['kill', server_pid])

    # Dropbear setup
    if dropbear_response == 'yes' or dropbear_response == 'y' or dropbear_response == 'Y' or dropbear_response == 'YES':
        with open(r'/home/' + user_name + r'/' + key_name + r'.pub', "r") as opened_file:
            lines = opened_file.readlines()

        with open(r'/home/' + user_name + r'/etc/dropbear/authorized_keys', "w") as opened_file:
            opened_file.write(lines + '\n')

        subprocess.call(['chmod', '0700', r'/etc/dropbear'])
        subprocess.call(['chmod', '0600', r'/etc/dropbear/authorized_keys'])

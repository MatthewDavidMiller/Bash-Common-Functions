# Credits
# https://www.w3schools.com/python/gloss_python_if_statement.asp
# https://www.w3schools.com/python/gloss_python_if_or.asp
# https://www.w3schools.com/python/python_cmd_input.asp

import subprocess
import os


def generate_ssh_key(user_name, key_name):
    # Generate key
    subprocess.call([r'ssh-keygen', r'-f', r'/home/' + user_name + r'/' + key_name, r'-t', r'ed25519'])

    # Authorize the key for use with ssh
    os.makedirs(r'/home/' + user_name + r'/.ssh', exist_ok=True)
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
    print(r'Copy the key from the webserver on port 40080 before continuing: ')
    input()
    subprocess.call(['kill', server_pid])

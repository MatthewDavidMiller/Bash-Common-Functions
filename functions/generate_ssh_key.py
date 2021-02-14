# Credits
# https://www.w3schools.com/python/gloss_python_if_statement.asp
# https://www.w3schools.com/python/gloss_python_if_or.asp

import subprocess


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

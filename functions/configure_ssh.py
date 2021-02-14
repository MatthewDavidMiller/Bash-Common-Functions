# Credits to https://docs.python.org/3/howto/regex.html
# Credits to https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# Credits to https://www.w3schools.com/python/python_functions.asp
# Credits to https://www.w3schools.com/python/python_regex.asp
# Credits to phynfo, https://stackoverflow.com/questions/6186938/how-to-use-regexp-on-file-line-by-line-in-python
# Credits to David Miller, https://stackoverflow.com/questions/4427542/how-to-do-sed-like-text-replace-with-python
# Credits to https://www.w3schools.com/python/python_lists.asp
# Credits to Jim DeLaHunt, https://stackoverflow.com/questions/12871066/what-exactly-is-a-raw-string-regex-and-how-can-you-use-it
# Credits to Thierry Lathuille, https://stackoverflow.com/questions/45114679/how-to-append-a-name-to-a-file-if-it-isnt-already-present
import re


def configure_ssh():

    password_authentication_regex = str(
        '.*' + r'PasswordAuthentication' + '.*')

    password_authentication_replace = str(r'PasswordAuthentication no')

    empty_password_regex = str('.*' + r'PermitEmptyPasswords' + '.*')

    empty_password_replace = str(r'PermitEmptyPasswords no')

    disable_pam_regex = str('.*' + r'UsePAM' + '.*')

    disable_pam_replace = str(r'UsePAM no')

    disable_root_ssh_regex = str('.*' + r'PermitRootLogin' '.*')

    disable_root_ssh_replace = str(r'PermitRootLogin no')

    set_key_folder_regex = str('.*' + r'AuthorizedKeysFile' + '\s*' +
                               r'.ssh/authorized_keys' + '\s*' + r'.ssh/authorized_keys2')

    set_key_folder_replace = str(r'AuthorizedKeysFile .ssh/authorized_keys')

    enable_pub_key_authentication_regex = str(
        '.*' + r'PubkeyAuthentication' + '.*')

    enable_pub_key_authentication_replace = str(r'PubkeyAuthentication yes')

    # Turn off password authentication
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(password_authentication_regex, password_authentication_replace, line))
            if password_authentication_replace == line.strip():
                break
        else:
            opened_file.write(password_authentication_replace + '\n')

# Do not allow empty passwords
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(empty_password_regex,
                                     empty_password_replace, line))
            if empty_password_replace == line.strip():
                break
        else:
            opened_file.write(empty_password_replace + '\n')

# Turn off PAM
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(disable_pam_regex, disable_pam_replace, line))
            if disable_pam_replace == line.strip():
                break
        else:
            opened_file.write(disable_pam_replace + '\n')

# Turn off root ssh access
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(disable_root_ssh_regex,
                                     disable_root_ssh_replace, line))
            if disable_root_ssh_replace == line.strip():
                break
        else:
            opened_file.write(disable_root_ssh_replace + '\n')

# Enable public key authentication
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(set_key_folder_regex,
                                     set_key_folder_replace, line))
            if set_key_folder_replace == line.strip():
                break
        else:
            opened_file.write(set_key_folder_replace + '\n')

    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(enable_pub_key_authentication_regex,
                                     enable_pub_key_authentication_replace, line))
            if enable_pub_key_authentication_replace == line.strip():
                break
        else:
            opened_file.write(enable_pub_key_authentication_replace + '\n')

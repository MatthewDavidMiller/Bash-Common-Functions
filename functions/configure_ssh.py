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
    # Turn off password authentication
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(".*PasswordAuthentication.*",
                                     "PasswordAuthentication no", line))
            if 'PasswordAuthentication no' == line.strip():
                break
        else:
            opened_file.write('PasswordAuthentication no' + '\n')

# Do not allow empty passwords
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(".*PermitEmptyPasswords.*",
                                     "PermitEmptyPasswords no", line))
            if 'PermitEmptyPasswords no' == line.strip():
                break
        else:
            opened_file.write('PermitEmptyPasswords no' + '\n')

# Turn off PAM
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(".*UsePAM.*", "UsePAM no", line))
            if 'UsePAM no' == line.strip():
                break
        else:
            opened_file.write('UsePAM no' + '\n')

# Turn off root ssh access
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(".*PermitRootLogin.*",
                                     "PermitRootLogin no", line))
            if 'PermitRootLogin no' == line.strip():
                break
        else:
            opened_file.write('PermitRootLogin no' + '\n')

# Enable public key authentication
    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(".*AuthorizedKeysFile\s*\.ssh/authorized_keys\s*\.ssh/authorized_keys2",
                                     'AuthorizedKeysFile .ssh/authorized_keys', line))
            if 'AuthorizedKeysFile .ssh/authorized_keys' == line.strip():
                break
        else:
            opened_file.write('AuthorizedKeysFile .ssh/authorized_keys' + '\n')

    with open('/etc/ssh/sshd_config', "r") as opened_file:
        lines = opened_file.readlines()
    with open('/etc/ssh/sshd_config', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(".*PubkeyAuthentication.*",
                                     'PubkeyAuthentication yes', line))
            if 'PubkeyAuthentication yes' == line.strip():
                break
        else:
            opened_file.write('PubkeyAuthentication yes' + '\n')


configure_ssh()

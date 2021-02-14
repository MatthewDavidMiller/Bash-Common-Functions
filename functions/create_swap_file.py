import subprocess
import re


def create_swap_file(swap_file_size):

    swap_fstab_regex = str('.*' + r'/swapfile' + '.*')

    swap_fstab_replace = str(r'/swapfile none swap defaults 0 0')

    # Create swapfile
    subprocess.run(['dd', 'if=/dev/zero', 'of=/swapfile', 'bs=1M',
                    'count=' + swap_file_size, 'status=progress'])
    # Set file permissions
    # chmod 600
    subprocess.run(['chmod', 'u=rw,g-rwx,o-rwx', '/swapfile'])
    # Format file to swap
    subprocess.run(['mkswap', '/swapfile'])
    # Activate the swap file
    subprocess.run(['swapon', '/swapfile'])

    # Add swap to fstab
    with open('/etc/fstab', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/fstab', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(swap_fstab_regex, swap_fstab_replace, line))

            if swap_fstab_replace == line.strip():
                break
        else:
            opened_file.write(swap_fstab_replace + '\n')

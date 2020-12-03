#!/bin/bash

function configure_ssh() {
    # Turn off password authentication
    grep -q -E ".*PasswordAuthentication" '/etc/ssh/sshd_config' && sed -i -E "s,.*PasswordAuthentication.*,PasswordAuthentication no," '/etc/ssh/sshd_config' || printf '%s\n' 'PasswordAuthentication no' >>'/etc/ssh/sshd_config'

    # Do not allow empty passwords
    grep -q -E ".*PermitEmptyPasswords" '/etc/ssh/sshd_config' && sed -i -E "s,.*PermitEmptyPasswords.*,PermitEmptyPasswords no," '/etc/ssh/sshd_config' || printf '%s\n' 'PermitEmptyPasswords no' >>'/etc/ssh/sshd_config'

    # Turn off PAM
    grep -q -E ".*UsePAM" '/etc/ssh/sshd_config' && sed -i -E "s,.*UsePAM.*,UsePAM no," '/etc/ssh/sshd_config' || printf '%s\n' 'UsePAM no' >>'/etc/ssh/sshd_config'

    # Turn off root ssh access
    grep -q -E ".*PermitRootLogin" '/etc/ssh/sshd_config' && sed -i -E "s,.*PermitRootLogin.*,PermitRootLogin no," '/etc/ssh/sshd_config' || printf '%s\n' 'PermitRootLogin no' >>'/etc/ssh/sshd_config'

    # Enable public key authentication
    grep -q -E ".*AuthorizedKeysFile" '/etc/ssh/sshd_config' && sed -i -E "s,.*AuthorizedKeysFile\s*.ssh\/authorized_keys\s*.ssh\/authorized_keys2,AuthorizedKeysFile .ssh\/authorized_keys," '/etc/ssh/sshd_config' || printf '%s\n' 'AuthorizedKeysFile .ssh/authorized_keys' >>'/etc/ssh/sshd_config'
    grep -q -E ".*PubkeyAuthentication" '/etc/ssh/sshd_config' && sed -i -E "s,.*PubkeyAuthentication.*,PubkeyAuthentication yes," '/etc/ssh/sshd_config' || printf '%s\n' 'PubkeyAuthentication yes' >>'/etc/ssh/sshd_config'
}

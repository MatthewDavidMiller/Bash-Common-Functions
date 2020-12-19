#!/bin/bash

function lock_root() {
    passwd --lock root
}

function get_username() {
    user_name=$(logname)
}

function get_interface_name() {
    interface="$(ip route get 8.8.8.8 | sed -nr 's/.*dev ([^\ ]+).*/\1/p')"
    echo "Interface name is ${interface}"
}

function fix_apt_packages() {
    dpkg --configure -a
}

function install_packages() {
    apt-get update
    apt-get upgrade -y
    apt-get install -y $packages
}

function get_ipv6_link_local_address() {
    ipv6_link_local_address="$(ip address | grep '.*inet6 fe80' | sed -nr 's/.*inet6 ([^\ ]+)\/64.*/\1/p')"
    echo "ipv6 link local address is ${ipv6_link_local_address}"
}

function set_timezone() {
    ln -sf '/usr/share/zoneinfo/America/New_York' '/etc/localtime'
}

function set_language() {
    grep -q -E ".*LANG=" '/etc/locale.conf' && sed -i -E "s,.*LANG=.*,LANG=en_US\.UTF-8," '/etc/locale.conf' || printf '%s\n' 'LANG=en_US.UTF-8' >>'/etc/locale.conf'
}

function set_hostname() {
    # Parameters
    local device_hostname=${1}

    rm -f '/etc/hostname'
    printf '%s\n' "${device_hostname}" >>'/etc/hostname'
}

function setup_hosts_file() {
    # Parameters
    local device_hostname=${1}

    grep -q -E ".*127\.0\.0\.1 localhost" '/etc/hosts' && sed -i -E "s,.*127\.0\.0\.1 localhost.*,127\.0\.0\.1 localhost," '/etc/hosts' || printf '%s\n' '127.0.0.1 localhost' >>'/etc/hosts'
    grep -q -E ".*::1 localhost" '/etc/hosts' && sed -i -E "s,.*::1.*,::1 localhost," '/etc/hosts' || printf '%s\n' '::1 localhost' >>'/etc/hosts'
    grep -q -E ".*127\.0\.0\.1 ${device_hostname}\.localdomain ${device_hostname}" '/etc/hosts' && sed -i -E "s,.*127\.0\.0\.1 ${device_hostname}.*,127\.0\.0\.1 ${device_hostname}\.localdomain ${device_hostname}," '/etc/hosts' || printf '%s\n' "127.0.0.1 ${device_hostname}.localdomain ${device_hostname}" >>'/etc/hosts'
}

function create_user() {
    # Parameters
    local user_name=${1}

    useradd -m "${user_name}"
    echo "Set the password for ${user_name}"
    passwd "${user_name}"
    mkdir -p "/home/${user_name}"
    chown "${user_name}" "/home/${user_name}"
}

function allow_wheel_sudo() {
    local wheel
    local wheel_new
    wheel='#%wheel ALL=(ALL) ALL'
    wheel_new='%wheel ALL=(ALL) ALL'

    grep -q -E ".*${wheel_new}" '/etc/sudoers' && sed -i -E "s,.*${wheel}.*,${wheel_new}," '/etc/sudoers' || printf '%s\n' "${wheel_new}" >>'/etc/sudoers'
}

function add_user_to_wheel_group() {
    # Parameters
    local user_name=${1}

    usermod -G wheel "${user_name}"
}

function add_user_to_sudo_group() {
    # Parameters
    local user_name=${1}

    usermod -G sudo "${user_name}"
}

function set_shell_bash() {
    # Parameters
    local user_name=${1}

    chsh -s /bin/bash
    chsh -s /bin/bash "${user_name}"
}

function get_linux_headers() {
    linux_headers="linux-headers-$(uname -r)"
}

function add_backports_repository() {
    # Parameters
    local release_name=${1}

    cat <<EOF >>'/etc/apt/sources.list'
deb https://mirrors.wikimedia.org/debian/ ${release_name}-backports main
deb-src https://mirrors.wikimedia.org/debian/ ${release_name}-backports main
EOF
}

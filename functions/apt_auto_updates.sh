#!/bin/bash

function apt_configure_auto_updates() {
    # Parameters
    local release_name=${1}

    sed -i -E -z "s,.*Unattended-Upgrade::Origins-Pattern.*\n.*\n.*\n.*\n.*,Unattended-Upgrade::Origins-Pattern {\n\"origin=Debian\,n=${release_name}\,l=Debian\";\n\"origin=Debian\,n=${release_name}\,l=Debian-Security\";\n\"origin=Debian\,n=${release_name}-updates\";\n};," '/etc/apt/apt.conf.d/50unattended-upgrades'
    grep -q -E ".*Unattended-Upgrade::Origins-Pattern.*" '/etc/apt/apt.conf.d/50unattended-upgrades' || cat <<EOF >>"/etc/apt/apt.conf.d/50unattended-upgrades"
Unattended-Upgrade::Origins-Pattern {
        "origin=Debian,n=${release_name},l=Debian";
        "origin=Debian,n=${release_name},l=Debian-Security";
        "origin=Debian,n=${release_name}-updates";
};
EOF

    sed -i -E "s,.*Unattended-Upgrade::Automatic-Reboot.*,Unattended-Upgrade::Automatic-Reboot \"true\";," '/etc/apt/apt.conf.d/50unattended-upgrades'
    grep -q -E ".*Unattended-Upgrade::Automatic-Reboot" '/etc/apt/apt.conf.d/50unattended-upgrades' || printf '%s\n' 'Unattended-Upgrade::Automatic-Reboot "true";' >>'/etc/apt/apt.conf.d/50unattended-upgrades'

    sed -i -E "s,.*Unattended-Upgrade::Automatic-Reboot-Time.*,Unattended-Upgrade::Automatic-Reboot-Time \"04:00\";," '/etc/apt/apt.conf.d/50unattended-upgrades'
    grep -q -E ".*Unattended-Upgrade::Automatic-Reboot-Time" '/etc/apt/apt.conf.d/50unattended-upgrades' || printf '%s\n' 'Unattended-Upgrade::Automatic-Reboot-Time "04:00";' >>'/etc/apt/apt.conf.d/50unattended-upgrades'
}

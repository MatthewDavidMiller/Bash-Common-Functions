#!/bin/bash

function log_rotate_configure() {
    # Parameters
    user_name=${1}

    apt-get install -y logrotate
    touch -a '/etc/logrotate.conf'
    mkdir -p "/home/$user_name/config_backups"
    cp '/etc/logrotate.conf' "/home/$user_name/config_backups/logrotate.conf.backup"
    grep -q -E "(^\s*[#]*\s*daily\s*$)|(^\s*[#]*\s*weekly\s*$)|(^\s*[#]*\s*monthly\s*$)" '/etc/logrotate.conf' && sed -i -E "s,(^\s*[#]*\s*daily\s*$)|(^\s*[#]*\s*weekly\s*$)|(^\s*[#]*\s*monthly\s*$),daily," '/etc/logrotate.conf' || printf '%s\n' 'daily' >>'/etc/logrotate.conf'
    grep -q -E "^\s*[#]*\s*minsize.*$" '/etc/logrotate.conf' && sed -i -E "s,^\s*[#]*\s*minsize.*$,minsize 100M," '/etc/logrotate.conf' || printf '%s\n' 'minsize 100M' >>'/etc/logrotate.conf'
    grep -q -E "^\s*[#]*\s*rotate\s*[0-9]*$" '/etc/logrotate.conf' && sed -i -E "s,^\s*[#]*\s*rotate\s*[0-9]*$,rotate 4," '/etc/logrotate.conf' || printf '%s\n' 'rotate 4' >>'/etc/logrotate.conf'
    grep -q -E "^\s*[#]*\s*compress\s*$" '/etc/logrotate.conf' && sed -i -E "s,^\s*[#]*\s*compress\s*$,compress," '/etc/logrotate.conf' || printf '%s\n' 'compress' >>'/etc/logrotate.conf'
    grep -q -E "^\s*[#]*\s*create\s*$" '/etc/logrotate.conf' && sed -i -E "s,^\s*[#]*\s*create\s*$,create," '/etc/logrotate.conf' || printf '%s\n' 'create' >>'/etc/logrotate.conf'
}

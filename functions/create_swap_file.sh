#!/bin/bash

function create_swap_file() {
    # Parameters
    local swap_file_size=${1}

    # Create swapfile
    dd if=/dev/zero of=/swapfile bs=1M count="${swap_file_size}" status=progress
    # Set file permissions
    # chmod 600
    chmod u=rw,g-rwx,o-rwx '/swapfile'
    # Format file to swap
    mkswap /swapfile
    # Activate the swap file
    swapon /swapfile
    # Add to fstab
    grep -q -E ".*\/swapfile" '/etc/fstab' && sed -i -E "s,.*\/swapfile.*,\/swapfile none swap defaults 0 0," '/etc/fstab' || printf '%s\n' "/swapfile none swap defaults 0 0" >>'/etc/fstab'
}

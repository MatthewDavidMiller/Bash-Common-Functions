#!/bin/bash

function configure_network() {
    # Parameters
    local ip_address=${1}
    local network_address=${2}
    local subnet_mask=${3}
    local gateway_address=${4}
    local dns_address=${5}
    local interface=${6}
    local ipv6_link_local_address=${7}

    # Configure ipv4 network
    # Add auto $interface if it is not in the file
    grep -q -E ".*auto ${interface}" '/etc/network/interfaces' || printf '%s\n' "auto ${interface}" >>'/etc/network/interfaces'

    # Replace iface $interface inet dhcp with iface $interface inet static
    sed -i -E -z "s,.*iface ${interface} inet dhcp.*,iface ${interface} inet static\naddress ${ip_address}\nnetwork ${network_address}\nnetmask ${subnet_mask}\ngateway ${gateway_address}\ndns-nameservers ${dns_address}," '/etc/network/interfaces'

    grep -q -E ".*iface ${interface} inet static.*" '/etc/network/interfaces' || cat <<EOF >>'/etc/network/interfaces'
iface ${interface} inet static
    address ${ip_address}
    network ${network_address}
    netmask ${subnet_mask}
    gateway ${gateway_address}
    dns-nameservers ${dns_address}
EOF

    grep -q -E ".*iface ${interface} inet6 static.*" '/etc/network/interfaces' || cat <<EOF >>'/etc/network/interfaces'

iface ${interface} inet6 static
    address ${ipv6_link_local_address}
    netmask 64
    scope link
EOF

    # Restart network interface
    ifdown "${interface}" && ifup "${interface}"
}

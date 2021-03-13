# Credits
# Gjordis, https://stackoverflow.com/questions/15107714/wait-process-until-all-subprocess-finish

import re
import subprocess


def configure_network(ip_address, network_address, subnet_mask, gateway_address, dns_address, interface, ipv6_link_local_address):

    auto_interface_regex = str('.*' + r'auto ' + interface + '.*')

    auto_interface_replace = str(r'auto ' + interface)

    interface_static_regex = str(
        '.*' + r'iface ' + interface + r' inet dhcp' '.*')

    interface_static_replace = str(r'iface ' + interface + r' inet static' + '\n' + r'address ' + ip_address + '\n' + r'network ' +
                                   network_address + '\n' + r'netmask ' + subnet_mask + '\n' r'gateway ' + gateway_address + '\n' r'dns-nameservers ' + dns_address)

    interface_ipv6_static_regex = str(
        '.*' + r'iface ' + interface + r' inet dhcp' '.*')

    interface_ipv6_static_replace = str(r'iface ' + interface + r' inet6 static' + '\n' +
                                        r'address ' + ipv6_link_local_address + '\n' + r'netmask 64' + '\n' + r'scope link')

    # Configure ipv4 network
    # Add auto interface if it is not in the file
    with open('/etc/network/interfaces', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/network/interfaces', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(auto_interface_regex,
                                     auto_interface_replace, line))

            if auto_interface_replace == line.strip():
                break
        else:
            opened_file.write(auto_interface_replace + '\n')

    # Replace iface interface inet dhcp with iface interface inet static
    with open('/etc/network/interfaces', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/network/interfaces', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(interface_static_regex,
                                     interface_static_replace, line))

            if interface_static_replace == line.strip():
                break
        else:
            opened_file.write(interface_static_replace + '\n')

    with open('/etc/network/interfaces', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/network/interfaces', "w") as opened_file:
        for line in lines:
            opened_file.write(re.sub(interface_ipv6_static_regex,
                                     interface_ipv6_static_replace, line))

            if interface_ipv6_static_replace == line.strip():
                break
        else:
            opened_file.write(interface_ipv6_static_replace + '\n')

    # Restart network interface
    subprocess.call(['ifdown', interface])
    subprocess.call(['ifup', interface])

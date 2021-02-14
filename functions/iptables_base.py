import subprocess
import re


def iptables_setup_base():

    # Allow established connections
    subprocess.call(['iptables', '-A', 'INPUT', '-m', 'conntrack',
                     '--ctstate', 'ESTABLISHED,RELATED', '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-m', 'conntrack',
                     '--ctstate', 'ESTABLISHED,RELATED', '-j', 'ACCEPT'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_set_defaults():

    # Drop inbound by default
    subprocess.call(['iptables', '-P', 'INPUT', 'DROP'])
    subprocess.call(['ip6tables', '-P', 'INPUT', 'DROP'])

    # Allow outbound by default
    subprocess.call(['iptables', '-P', 'OUTPUT', 'ACCEPT'])
    subprocess.call(['ip6tables', '-P', 'OUTPUT', 'ACCEPT'])

    # Drop forwarding by default
    subprocess.call(['iptables', '-P', 'FORWARD', 'DROP'])
    subprocess.call(['ip6tables', '-P', 'FORWARD', 'DROP'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_forwarding():

    allow_forwarding_ipv4_regex = str('.*' + r'net.ipv4.ip_forward=' + '.*')

    allow_forwarding_ipv4_replace = str(r'net.ipv4.ip_forward=1')

    allow_forwarding_ipv6_regex = str(
        '.*' + r'net.ipv6.conf.all.forwarding=' + '.*')

    allow_forwarding_ipv6_replace = str(r'net.ipv6.conf.all.forwarding=1')

    # Allow Forwarding
    with open('/etc/sysctl.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/sysctl.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(allow_forwarding_ipv4_regex, allow_forwarding_ipv4_replace, line))

            if allow_forwarding_ipv4_replace == line.strip():
                break
        else:
            opened_file.write(allow_forwarding_ipv4_replace + '\n')

    with open('/etc/sysctl.conf', "r") as opened_file:
        lines = opened_file.readlines()

    with open('/etc/sysctl.conf', "w") as opened_file:
        for line in lines:
            opened_file.write(
                re.sub(allow_forwarding_ipv6_regex, allow_forwarding_ipv6_replace, line, flags=re.S))

            if allow_forwarding_ipv6_replace == line.strip():
                break
        else:
            opened_file.write(allow_forwarding_ipv6_replace + '\n')

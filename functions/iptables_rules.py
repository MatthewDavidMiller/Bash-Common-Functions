# Credits
# https://stackabuse.com/executing-shell-commands-with-python/
# Skurmedel, https://stackoverflow.com/questions/4856583/how-do-i-pipe-a-subprocess-call-to-a-text-file

import subprocess


def iptables_allow_ssh(source, interface, ipv6_link_local):

    # Allow ssh from a source and interface
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                     '22', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                     '22', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Log new connection ips and add them to a list called SSH
    subprocess.call(
        ['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--set', '--name', 'SSH'])
    subprocess.call(
        ['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--set', '--name', 'SSH'])

    # Log ssh connections from an ip to 6 connections in 60 seconds.
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--update',
                     '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'LOG', '--log-level', 'info', '--log-prefix', 'Limit SSH'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--update',
                     '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'LOG', '--log-level', 'info', '--log-prefix', 'Limit SSH'])

    # Limit ssh connections from an ip to 6 connections in 60 seconds.
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW',
                     '-m', 'recent', '--update', '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'DROP'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW',
                     '-m', 'recent', '--update', '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'DROP'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_dns(source, interface, ipv6_link_local):

    # Allow dns from a source and interface
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                     '53', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'udp', '--dport',
                     '53', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                     '53', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'udp', '--dport',
                     '53', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_http(source, interface, ipv6_link_local):

    # Allow http from a source and interface
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                     '80', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'tcp' '--dport',
                     '80', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_https(source, interface, ipv6_link_local):

    # Allow https from a source and interface
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                     '443', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'tcp' '--dport',
                     '443', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_icmp(source, interface, ipv6_link_local):

    # Allow icmp from a source and interface
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'icmp',
                     '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-p', 'icmpv6',
                     '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_loopback():

    subprocess.call(['iptables', '-A', 'INPUT', '-s',
                     '127.0.0.0/8', '-i', 'lo', '-j', 'ACCEPT'])
    subprocess.call(['ip6tables', '-A', 'INPUT', '-s',
                     '::1', '-i', 'lo', '-j', 'ACCEPT'])

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)


def iptables_allow_vpn_port(interface, vpn_port):

    # Allow vpn port to a destination
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'udp',
                     '--dport', vpn_port, '-i', interface, '-j', 'ACCEPT'])
    # ip6tables -A INPUT -p udp --dport ${vpn_port} -i "${interface}" -j ACCEPT

    # Log new connection ips and add them to a list called Wireguard
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'udp', '--dport', vpn_port, '-m',
                     'state', '--state', 'NEW', '-m', 'recent', '--set', '--name', 'Wireguard'])
    # ip6tables -A INPUT -p udp --dport ${vpn_port} -m state --state NEW -m recent --set --name Wireguard

    # Log vpn connections from an ip to 3 connections in 60 seconds.
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'udp', '--dport', vpn_port, '-m', 'state', '--state', 'NEW', '-m', 'recent', '--update',
                     '--seconds', '60', '--hitcount', '3', '--rttl', '--name', 'Wireguard', '-j', 'LOG', '--log-level', 'info', '--log-prefix', 'Limit Wireguard'])
    # ip6tables -A INPUT -p udp --dport ${vpn_port} -m state --state NEW -m recent --update --seconds 60 --hitcount 3 --rttl --name Wireguard -j LOG --log-level info --log-prefix "Limit Wireguard"

    # Limit vpn connections from an ip to 3 connections in 60 seconds.
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'udp', '--dport', vpn_port, '-m', 'state', '--state', 'NEW', '-m',
                     'recent', '--update', '--seconds', '60', '--hitcount', '3', '--rttl', '--name', 'Wireguard', '-j', 'DROP'])
    # ip6tables -A INPUT -p udp --dport ${vpn_port} -m state --state NEW -m recent --update --seconds 60 --hitcount 3 --rttl --name Wireguard -j DROP

    # Save rules
    with open('/etc/iptables/rules.v4', "w") as opened_file:
        subprocess.call(['iptables-save'], stdout=opened_file)

    with open('/etc/iptables/rules.v6', "w") as opened_file:
        subprocess.call(['ip6tables-save'], stdout=opened_file)

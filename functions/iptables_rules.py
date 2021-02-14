# Credits to https://stackabuse.com/executing-shell-commands-with-python/

import subprocess


def iptables_allow_ssh(source, interface, ipv6_link_local):

    # Allow ssh from a source and interface
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                    '22', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                    '22', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Log new connection ips and add them to a list called SSH
    subprocess.run(
        ['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--set', '--name', 'SSH'])
    subprocess.run(
        ['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--set', '--name', 'SSH'])

    # Log ssh connections from an ip to 6 connections in 60 seconds.
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--update',
                    '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'LOG', '--log-level', 'info', '--log-prefix', 'Limit SSH'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW', '-m', 'recent', '--update',
                    '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'LOG', '--log-level', 'info', '--log-prefix', 'Limit SSH'])

    # Limit ssh connections from an ip to 6 connections in 60 seconds.
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW',
                    '-m', 'recent', '--update', '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'DROP'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-m', 'state', '--state', 'NEW',
                    '-m', 'recent', '--update', '--seconds', '60', '--hitcount', '6', '--rttl', '--name', 'SSH', '-j', 'DROP'])

    # Save rules
    subprocess.run(['iptables-save']) > '/etc/iptables/rules.v4'
    subprocess.run(['ip6tables-save']) > '/etc/iptables/rules.v6'


def iptables_allow_dns(source, interface, ipv6_link_local):

    # Allow dns from a source and interface
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                    '53', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'udp', '--dport',
                    '53', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                    '53', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'udp', '--dport',
                    '53', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    subprocess.run(['iptables-save']) > '/etc/iptables/rules.v4'
    subprocess.run(['ip6tables-save']) > '/etc/iptables/rules.v6'


def iptables_allow_http(source, interface, ipv6_link_local):

    # Allow http from a source and interface
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                    '80', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'tcp' '--dport',
                    '80', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    subprocess.run(['iptables-save']) > '/etc/iptables/rules.v4'
    subprocess.run(['ip6tables-save']) > '/etc/iptables/rules.v6'


def iptables_allow_https(source, interface, ipv6_link_local):

    # Allow https from a source and interface
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport',
                    '443', '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'tcp' '--dport',
                    '443', '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    subprocess.run(['iptables-save']) > '/etc/iptables/rules.v4'
    subprocess.run(['ip6tables-save']) > '/etc/iptables/rules.v6'


def iptables_allow_icmp(source, interface, ipv6_link_local):

    # Allow icmp from a source and interface
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'icmp',
                    '-s', source, '-i', interface, '-j', 'ACCEPT'])
    subprocess.run(['ip6tables', '-A', 'INPUT', '-p', 'icmpv6',
                    '-s', ipv6_link_local, '-i', interface, '-j', 'ACCEPT'])

    # Save rules
    subprocess.run(['iptables-save']) > '/etc/iptables/rules.v4'
    subprocess.run(['ip6tables-save']) > '/etc/iptables/rules.v6'

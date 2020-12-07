#!/bin/bash

function iptables_setup_base() {
    # Allow established connections
    iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    ip6tables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

    # Save rules
    iptables-save >/etc/iptables/rules.v4
    ip6tables-save >/etc/iptables/rules.v6
}

function iptables_set_defaults() {
    # Drop inbound by default
    iptables -P INPUT DROP
    ip6tables -P INPUT DROP

    # Allow outbound by default
    iptables -P OUTPUT ACCEPT
    ip6tables -P OUTPUT ACCEPT

    # Drop forwarding by default
    iptables -P FORWARD DROP
    ip6tables -P FORWARD DROP

    # Save rules
    iptables-save >/etc/iptables/rules.v4
    ip6tables-save >/etc/iptables/rules.v6
}

function iptables_allow_forwarding() {
    grep -q -E ".*net\.ipv4\.ip_forward=" '/etc/sysctl.conf' && sed -i -E "s,.*net\.ipv4\.ip_forward=.*,net.ipv4.ip_forward=1," '/etc/sysctl.conf' || printf '%s\n' 'net.ipv4.ip_forward=1' >>'/etc/sysctl.conf'
    grep -q -E ".*net\.ipv6\.conf\.all\.forwarding=" '/etc/sysctl.conf' && sed -i -E "s,.*net\.ipv6\.conf\.all\.forwarding=.*,net.ipv6.conf.all.forwarding=1," '/etc/sysctl.conf' || printf '%s\n' 'net.ipv6.conf.all.forwarding=1' >>'/etc/sysctl.conf'
}

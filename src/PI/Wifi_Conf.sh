#!/bin/bash

if [ "$1" == "hotspot" ]; then
    # Hotspot Configuration
    sudo cp /etc/dhcpcd.conf.hotspot /etc/dhcpcd.conf
    sudo cp /etc/dnsmasq.conf.hotspot         /etc/dnsmasq.conf
    sudo cp /etc/hostapd/hostapd.conf.hotspot /etc/hostapd/hostapd.conf
    sudo cp /etc/default/hostapd.hotspot      /etc/default/hostapd
    sudo cp /etc/sysctl.conf.hotspot          /etc/sysctl.conf
    sudo cp /etc/network/interfaces.hotspot   /etc/network/interfaces

    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE # Add
    sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
    iptables-restore < /etc/iptables.ipv4.nat


elif [ "$1" == "normalwifi" ]; then
    # Normal Wi-Fi Configuration
    sudo cp /etc/dhcpcd.conf.wifi /etc/dhcpcd.conf
    sudo cp /etc/hostapd/hostapd.conf.wifi   /etc/hostapd/hostapd.conf
    sudo cp /etc/dnsmasq.conf.wifi           /etc/dnsmasq.conf
    sudo cp /etc/default/hostapd.wifi        /etc/default/hostapd
    sudo cp /etc/sysctl.conf.wifi            /etc/sysctl.conf
    sudo cp /etc/network/interfaces.wifi     /etc/network/interfaces

    sudo iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE # Delete
    
else
    echo "Invalid parameter. Use 'hotspot' or 'normalwifi'."
fi

#!/bin/bash

sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.wifi 
sudo echo "interface=wlan0" >> /etc/dnsmasq.conf
sudo echo "dhcp-range=192.168.0.11,192.168.0.30,255.255.255.0,24h" >> /etc/dnsmasq.conf
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.hotspot

sudo echo "interface=wlan0" >> /etc/hostapd/hostapd.conf
sudo echo "bridge=br0" >> /etc/hostapd/hostapd.conf
sudo echo "hw_mode=g" >> /etc/hostapd/hostapd.conf
sudo echo "channel=7" >> /etc/hostapd/hostapd.conf
sudo echo "wmm_enabled=0" >> /etc/hostapd/hostapd.conf
sudo echo "macaddr_acl=0" >> /etc/hostapd/hostapd.conf
sudo echo "auth_algs=1" >> /etc/hostapd/hostapd.conf
sudo echo "ignore_broadcast_ssid=0" >> /etc/hostapd/hostapd.conf
sudo echo "wpa=2" >> /etc/hostapd/hostapd.conf
sudo echo "wpa_key_mgmt=WPA-PSK" >> /etc/hostapd/hostapd.conf
sudo echo "wpa_pairwise=TKIP" >> /etc/hostapd/hostapd.conf
sudo echo "rsn_pairwise=CCMP" >> /etc/hostapd/hostapd.conf
sudo echo "ssid=momentumWCR" >> /etc/hostapd/hostapd.conf
sudo echo "wpa_passphrase=momentum_2024" >> /etc/hostapd/hostapd.conf
sudo mv /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.hotspot
sudo echo "" >> /etc/hostapd/hostapd.conf.wifi

sudo mv /etc/default/hostapd /etc/default/hostapd.wifi
sudo echo "DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"" >> /etc/default/hostapd
sudo mv /etc/default/hostapd /etc/default/hostapd.hotspot

sudo mv /etc/sysctl.conf /etc/sysctl.conf.wifi
sudo echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf.hotspot

sudo mv /etc/network/interfaces /etc/network/interfaces.wifi
sudo echo "auto br0" >> /etc/network/interfaces.hotspot
sudo echo "iface br0 inet manual" >> /etc/network/interfaces.hotspot
sudo echo "bridge_ports eth0 wlan0" >> /etc/network/interfaces.hotspot







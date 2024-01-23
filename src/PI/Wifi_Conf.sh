#!/bin/bash

if [ "$1" == "hotspot" ]; then
    # Hotspot Configuration
    sudo service NetworkManager start
    sleep 2
    sudo nmcli device wifi hotspot ssid Momentum-wcr password momentum_2024 ifname wlan0

elif [ "$1" == "normalwifi" ]; then
    # Normal Wi-Fi Configuration
    sudo service NetworkManager stop
    sudo service dhcpcd restart
    
else
    echo "Invalid parameter. Use 'hotspot' or 'normalwifi'."
fi

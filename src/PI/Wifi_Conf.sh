#!/bin/bash

if [ "$1" == "hotspot" ]; then
    # Hotspot Configuration
    echo "Configuring Raspberry Pi as Hotspot..."

    # Stop services
    sudo systemctl stop hostapd
    sudo systemctl stop dnsmasq

    # Edit network interfaces file
    sudo cp /etc/network/interfaces /etc/network/interfaces.backup
    sudo echo -e "auto lo\niface lo inet loopback\niface eth0 inet dhcp" | sudo tee /etc/network/interfaces

    # Start services
    sudo systemctl start hostapd
    sudo systemctl start dnsmasq

    echo "Hotspot configuration complete. Rebooting..."
    sudo reboot

elif [ "$1" == "normalwifi" ]; then
    # Normal Wi-Fi Configuration
    echo "Configuring Raspberry Pi as Normal Wi-Fi..."

    # Stop services
    sudo systemctl stop hostapd
    sudo systemctl stop dnsmasq

    # Restore original network interfaces file
    sudo cp /etc/network/interfaces.backup /etc/network/interfaces

    # Start services
    sudo systemctl start hostapd
    sudo systemctl start dnsmasq

    echo "Normal Wi-Fi configuration complete. Rebooting..."
    sudo reboot

else
    echo "Invalid parameter. Use 'hotspot' or 'normalwifi'."
fi

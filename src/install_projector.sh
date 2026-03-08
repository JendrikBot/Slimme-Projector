echo "system update" 
sudo apt update -y

echo "installing VLC..."
sudo apt install -y vlc

echo "Configurating HDMI"
sudo sed -i '/hdmi_force_hotplug/d' /boot/config.txt
sudo sed -i '/hdmi_group/d' /boot/config.txt
sudo sed =i 'hdmi_mode/d' /boot/config.txt

echo "hdmi_force_hotplug=1" | sudo tee -a /boot/config.txt
echo "hdmi_group=1" | sudo tee -a /boot/config.txt
echo "hdmi_mode=16 | sudo tee -a /boot/config.txt

echo "setup complete. Reboot required"

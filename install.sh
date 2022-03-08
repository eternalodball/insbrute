#!/bin/bash

echo -e "\e[1m"

#python

echo "[+] Installing pip ..."
echo ""
sudo apt-get install python3-pip -y

#chromium

echo ""
echo "[+] Do you want to install chromium browser (yes/no)"
echo ""
read -p ">> " option

if [[ "$option" == "yes" ]]
then
echo ""
echo "[+] installing chromium ..."
echo ""
sudo apt-get install chromium -y

elif [[ $option == "no" ]]
then
echo ""
echo "[+] Not installing chromium ..."

else
echo ""  
echo "[!] No such option"
echo ""
fi

# Selenium

echo ""
echo "[+] Installing selenium ..."

pip3 install selenium


#chromedriver

echo ""
echo "[+] Do you want to install chromedriver (yes/no)"
echo ""
read -p ">> " option

if [[ "$option" == "yes" ]]
then
echo ""
echo "[+] installing chromedriver ..."
pip3 install chromedriver-py

elif [[ $option == "no" ]]
then
echo ""
echo "[+] Not installing chromedriver ..."

else
echo ""  
echo "[!] No such option"
fi

echo ""
echo "[+] Dependencies installed ! , Happy hacking ;)"
echo ""

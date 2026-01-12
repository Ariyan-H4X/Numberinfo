# NUMBER INFO

A Python-based terminal tool that fetches mobile number information using an API.  
Works smoothly on Termux, Kali Linux, and all Linux terminals.

------------------------------------------------------------

DISCLAIMER
This program is only for educational purposes.  
Do not use this tool for any illegal or unethical activities.

------------------------------------------------------------

CREDIT
Ariyan  
Telegram: https://t.me/ar1yanff

------------------------------------------------------------

FEATURES
- Supports Termux, Kali Linux, Ubuntu, Debian, Mint
- User enters a 10-digit mobile number
- Calls API and shows formatted results
- Clean terminal output with banner
- Easy to install and use

------------------------------------------------------------

PROJECT FILES
Ariyan.py  
requirements.txt  
README.md  

------------------------------------------------------------

SETUP & RUN GUIDE (ALL IN ONE)

=====================
TERMUX (Android)
=====================

Update & Upgrade:
    pkg update -y && pkg upgrade -y

Install Python:
    pkg install python -y

Install Requirements:
    pip install -r requirements.txt

Run Tool:
    python Ariyan.py

------------------------------------------------------------

=====================
KALI LINUX
=====================

Update System:
    sudo apt update && sudo apt upgrade -y

Install Python & Pip:
    sudo apt install python3 python3-pip -y

Install Requirements:
    pip3 install -r requirements.txt

Run Tool:
    python3 Ariyan.py

------------------------------------------------------------

=====================
OTHER LINUX (Ubuntu / Debian / Mint)
=====================

Update System:
    sudo apt update

Install Python:
    sudo apt install python3 python3-pip -y

Install Requirements:
    pip3 install -r requirements.txt

Run Tool:
    python3 Ariyan.py

------------------------------------------------------------

HOW TO USE
1. Run the script
2. Enter a valid 10-digit mobile number
3. Wait for API response
4. View the result directly in terminal

------------------------------------------------------------

SAMPLE OUTPUT

============================================================
                      NUMBER INFO
============================================================
Description : This program is only for educational purposes
Credit      : Ariyan (https://t.me/ar1yanff)
============================================================

Enter 10-digit mobile number: 8101817567

[+] Fetching information...

--- Result 1 ---
ID            : 1001685248
Mobile        : 8101817567
Name          : Bhaskar Roy
Father Name   : shrihari roy
Address       : West Bengal
Alt Mobile    : 7872874448
Circle        : JIO WB
ID Number     : 845656269853
Email         : None

------------------------------------------------------------

TESTED ON
- Termux
- Kali Linux
- Ubuntu
- Debian

------------------------------------------------------------

NOTES
- Internet connection required
- Only 10-digit numbers are accepted
- Output depends on API availability

------------------------------------------------------------

END
Made with ❤️ by Ariyan

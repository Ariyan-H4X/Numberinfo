#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import json

# ===== PROGRAM INFO =====
PROGRAM_NAME = "NUMBER INFO"
DESCRIPTION = "This program is only for educational purposes don't use it for illigal works."
CREDIT = "Ariyan"
CREDIT_LINK = "https://t.me/ar1yanff"

API_KEY = "azam"
API_URL = "https://anishexploits.site/api/api.php"

def banner():
    print("=" * 60)
    print(f"{PROGRAM_NAME:^60}")
    print("=" * 60)
    print(f"Description : {DESCRIPTION}")
    print(f"Credit      : {CREDIT} ({CREDIT_LINK})")
    print("=" * 60)
    print()

def validate_number(number):
    return number.isdigit() and len(number) == 10

def fetch_number_info(number):
    params = {
        "key": API_KEY,
        "num": number
    }
    try:
        response = requests.get(API_URL, params=params, timeout=20)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("[!] Network Error:", e)
        sys.exit(1)
    except json.JSONDecodeError:
        print("[!] Invalid JSON response from API")
        sys.exit(1)

def show_result(data):
    if not data.get("success"):
        print("[!] No data found or API error")
        return

    results = data.get("result", [])
    if not results:
        print("[!] Empty result")
        return

    for i, item in enumerate(results, 1):
        print(f"\n--- Result {i} ---")
        print(f"ID            : {item.get('id')}")
        print(f"Mobile        : {item.get('mobile')}")
        print(f"Name          : {item.get('name')}")
        print(f"Father Name   : {item.get('father_name')}")
        print(f"Address       : {item.get('address')}")
        print(f"Alt Mobile    : {item.get('alt_mobile')}")
        print(f"Circle        : {item.get('circle')}")
        print(f"ID Number     : {item.get('id_number')}")
        print(f"Email         : {item.get('email')}")

def main():
    banner()
    number = input("Enter 10-digit mobile number: ").strip()

    if not validate_number(number):
        print("[!] Invalid number. Please enter exactly 10 digits.")
        sys.exit(1)

    print("\n[+] Fetching information...\n")
    data = fetch_number_info(number)
    show_result(data)

if __name__ == "__main__":
    main()
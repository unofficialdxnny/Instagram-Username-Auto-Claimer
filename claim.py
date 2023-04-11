import requests
import threading
from pystyle import *
import os

banner = '''

 _                        
(_)             _         
 _ ____   ___ _| |_ _____ 
| |  _ \ /___|_   _|____ |
| | | | |___ | | |_/ ___ |
|_|_| |_(___/   \__)_____|
                          

'''
os.system('cls')

print(Colorate.Color(Colors.purple, banner, True))


base_url = "https://www.instagram.com/"

def claim_username(username):
    url = f"{base_url}accounts/create_ajax/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "X-CSRFToken": "",
        "Referer": f"{base_url}accounts/emailsignup/"
    }
    data = {
        "email": "",
        "password": "",
        "username": username,
        "first_name": "",
        "opt_into_one_tap": False
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code, response.text)

usernames = ["example1", "example2", "example3"]

for username in usernames:
    t = threading.Thread(target=claim_username, args=(username,))
    t.start()

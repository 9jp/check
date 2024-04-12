import requests
from colorama import Fore, Style

def check_link(link):
    try:
        response = requests.head(link)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

link = input("Enter the link to check: ")
if check_link(link):
    print(f"{Fore.GREEN}Link is accessible.{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}Link is not accessible.{Style.RESET_ALL}")

import requests

def check_username(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f"The username '{username}' is available on Twitter!")
    else:
        print(f"The username '{username}' is already taken on Twitter.")

username = input("Enter a Twitter username to check for availability: ")
check_username(username)

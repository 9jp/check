import requests
from bs4 import BeautifulSoup

def check_twitter_username(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        if "Sorry, that page doesn’t exist!" in soup.title.text:
            print(f"The username '{username}' is available on Twitter!")
        else:
            print(f"The username '{username}' is already taken on Twitter.")
    else:
        print("Error connecting to Twitter. Please try again later.")

def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        if "Page Not Found • Instagram" in soup.title.text:
            print(f"The username '{username}' is available on Instagram!")
        else:
            print(f"The username '{username}' is already taken on Instagram.")
    else:
        print("Error connecting to Instagram. Please try again later.")

def check_snapchat_username(username):
    url = f"https://www.snapchat.com/add/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        if "Sorry! We couldn't find that page." in soup.text:
            print(f"The username '{username}' is available on Snapchat!")
        else:
            print(f"The username '{username}' is already taken on Snapchat.")
    else:
        print("Error connecting to Snapchat. Please try again later.")

print("Select an option to check for username availability:")
print("1. Check username on Twitter")
print("2. Check username on Instagram")
print("3. Check username on Snapchat")
print("4. Check username on all three platforms")

choice = input("Enter your choice (1/2/3/4): ")
username = input("Enter a username to check for availability: ")

if choice == "1":
    check_twitter_username(username)
elif choice == "2":
    check_instagram_username(username)
elif choice == "3":
    check_snapchat_username(username)
elif choice == "4":
    check_twitter_username(username)
    check_instagram_username(username)
    check_snapchat_username(username)
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")

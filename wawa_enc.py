import requests
import time

# File paths for tokens
tokens_file = "/sdcard/Test/toka.txt"

# Function to get stalkers
def get_stalkers(token):
    print("🔍 Searching for Profile Stalkers...")
    
    # Get recent post reactions
    url_reacts = f"https://graph.facebook.com/me/feed?fields=id,likes.limit(100)&access_token={token}"
    response_reacts = requests.get(url_reacts).json()

    # Get friends list
    url_friends = f"https://graph.facebook.com/me/friends?access_token={token}"
    response_friends = requests.get(url_friends).json()
    friend_list = [friend['id'] for friend in response_friends.get("data", [])]

    stalkers = []

    # Check who reacted but isn’t a friend
    for post in response_reacts.get("data", []):
        if "likes" in post:
            for user in post["likes"]["data"]:
                if user["id"] not in friend_list:  # Not a friend? Possible stalker!
                    stalkers.append(user["name"])

    if stalkers:
        print("\n👀 Possible Profile Stalkers Found:")
        for stalker in stalkers:
            print(f"🔸 {stalker}")
    else:
        print("❌ No stalkers detected.")

# Function to process all tokens and run stalker finder
def process_stalkers():
    try:
        with open(tokens_file, "r") as tf:
            tokens = tf.read().strip().split("\n")

            for token in tokens:
                print(f"\n📌 Checking Account with Token: {token[:10]}...")
                get_stalkers(token)
                time.sleep(2)  # Delay to avoid spam detection

    except FileNotFoundError:
        print("❌ Error: Token file not found!")

# Menu system
while True:
    print("\n[ MENU ]")
    print("1️⃣ Enable Profile Guard")
    print("2️⃣ Disable Profile Guard")
    print("3️⃣ Auto-Reacts")
    print("4️⃣ Auto-Stalker Finder 👀")
    print("0️⃣ Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "4":
        process_stalkers()
    elif choice == "0":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice! Please enter a valid number.")

import requests
import time

# File paths
tokens_file = "/sdcard/Test/toka.txt"
ids_file = "/sdcard/Test/tokaid.txt"

# Mobile API endpoint for bio update
FB_MOBILE_API = "https://graph.facebook.com/me"

# Function to update bio using Mobile API
def update_bio(token, bio_text):
    url = FB_MOBILE_API
    headers = {
        "Authorization": f"OAuth {token}",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)"
    }
    payload = {
        "bio": bio_text,
        "access_token": token
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200 and "error" not in response.text:
        print(f"✅ Bio Updated → {bio_text}")
    else:
        print(f"❌ Failed → {response.text}")

# Get bio input from user
bio_text = input("Enter the new bio: ")

# Process all tokens from file
def process_bio():
    try:
        with open(tokens_file, "r") as tf:
            tokens = tf.read().strip().split("\n")

            for token in tokens:
                update_bio(token.strip(), bio_text)
                time.sleep(2)  # Delay to prevent spam detection

    except FileNotFoundError:
        print("❌ Error: Token file not found!")

# Run the function
process_bio()

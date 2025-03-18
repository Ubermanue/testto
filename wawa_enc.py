import requests
import time

# File paths
tokens_file = "/sdcard/Test/toka.txt"
ids_file = "/sdcard/Test/tokaid.txt"

# Function to update bio
def update_bio(token, user_id, bio_text):
    url = f"https://graph.facebook.com/{user_id}"
    payload = {
        "bio": bio_text,
        "access_token": token
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200 and "error" not in response.text:
        print(f"✅ Bio Updated: {user_id} → {bio_text}")
    else:
        print(f"❌ Failed: {user_id} → {response.text}")

# Get bio input from user
bio_text = input("Enter the new bio: ")

# Process all tokens and user IDs
def process_bio():
    try:
        with open(tokens_file, "r") as tf, open(ids_file, "r") as idf:
            tokens = tf.read().strip().split("\n")
            user_ids = idf.read().strip().split("\n")

            if len(tokens) != len(user_ids):
                print("❌ Error: Token and ID count mismatch!")
            else:
                for token, user_id in zip(tokens, user_ids):
                    update_bio(token.strip(), user_id.strip(), bio_text)
                    time.sleep(2)  # Delay to prevent spam detection

    except FileNotFoundError:
        print("❌ Error: One or both files not found!")

# Run the function
process_bio()

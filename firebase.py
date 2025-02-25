# import firebase_admin
# from firebase_admin import credentials, db

# # Load Firebase credentials
# cred = credentials.Certificate("fire.json")  # Replace with your JSON file
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://ai-news-d465d-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Your Firebase URL
# })

# # Define the data to upload
# data= {
#     "article1": {
#         "headline": "News 1",
#         "author": "John Doe"
#     },
#     "article2": {
#         "headline": "News 2",
#         "author": "Jane Smith"
#     }
# }

# # Push data to Firebase
# ref = db.reference("/news")  # You can change the path
# ref.set(data)

# print("✅ Data uploaded successfully!")



import json
import os
import firebase_admin
from firebase_admin import credentials, db

# Load Firebase credentials from GitHub Secrets
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
if not firebase_credentials:
    raise ValueError("❌ FIREBASE_CREDENTIALS secret is missing!")

# Save credentials to a temporary file
cred_path = "firebase_temp.json"
with open(cred_path, "w", encoding="utf-8") as f:
    f.write(firebase_credentials)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ai-news-d465d-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Update your DB URL
})

# Function to rename keys in JSON
def rename_keys(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            return {f"article{i}": value for i, (key, value) in enumerate(data.items(), start=1)}
        return data  # Return as is if not a dictionary
    except json.JSONDecodeError as e:
        raise ValueError(f"❌ Invalid JSON format: {e}")

# Path to JSON file
json_file = "latest_news.json"  # Ensure this exists before running

# Process the JSON data
modified_data = rename_keys(json_file)

# Upload data to Firebase
ref = db.reference("/news")
ref.set(modified_data)

# Cleanup temporary file
os.remove(cred_path)

print("✅ Data uploaded successfully!")

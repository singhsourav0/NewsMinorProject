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

# Load Firebase credentials
cred = credentials.Certificate("fire.json")  # Replace with your Firebase credentials file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ai-news-d465d-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Your Firebase DB URL
})

# Function to replace URL keys with "article1", "article2", etc.
def rename_keys(json_file):
    """Replaces URL keys with 'article1', 'article2', etc."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):  # Ensure it's a dictionary
        new_data = {}
        for i, (key, value) in enumerate(data.items(), start=1):
            new_data[f"article{i}"] = value  # Rename keys as article1, article2, etc.

        return new_data

    return data  # Return unchanged if it's not a dictionary

# Path to JSON file
json_file = "latest_news.json"  # Replace with your actual JSON file

# Process the JSON data
modified_data = rename_keys(json_file)

# Upload modified data to Firebase
ref = db.reference("/news")  # Change path as needed
ref.set(modified_data)

print("✅ Data uploaded successfully with formatted keys!")

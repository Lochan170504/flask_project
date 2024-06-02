from google.cloud import translate_v2 as translate
import json

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\xampp\htdocs\flask_project\scholarship_data.json"

# Authenticate to Google Cloud
# Replace 'YOUR_PROJECT_ID' with your GCP project ID
translate_client = translate.Client()

# Read the JSON file
with open('scholarship_data.json', 'r') as file:
    data = json.load(file)

# Translate the text
for item in data:
    text_to_translate = item['text']
    translations = translate_client.translate(text_to_translate, target_language='kn')  # Translate to Kannada
    item['translated_text'] = translations['translatedText']

# Write the translations back to the JSON file
with open('translated_filekannada.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

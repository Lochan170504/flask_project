from google.cloud import translate
import json

# Initialize Google Cloud Translation client
client = translate.TranslationServiceClient()

# Load JSON file
with open('original.json', 'r', encoding='utf-8') as f:
    original_data = json.load(f)

# Function to translate text
def translate_text(text, target_language):
    response = client.translate_text(
        contents=[text],
        target_language_code=target_language,
    )
    return response.translations[0].translated_text

# Function to traverse and translate JSON structure
def translate_json(json_data, target_language):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            json_data[key] = translate_json(value, target_language)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            json_data[i] = translate_json(item, target_language)
    elif isinstance(json_data, str):
        json_data = translate_text(json_data, target_language)
    return json_data

# Translate JSON to multiple languages
languages = ['fr', 'es', 'de']  # Example: French, Spanish, German
for lang in languages:
    translated_data = translate_json(original_data, lang)
    with open(f'translated_{lang}.json', 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)

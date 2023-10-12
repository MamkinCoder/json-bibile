import json
import os

# Paths to the JSON files
file_paths = [
    "asv.json",
    "crtb.json",
    "kjv.json",
    "nrt.json",
    "rst.json"
]

# Function to load translations from each file
def load_translations(file_paths):
    translations = {}
    for path in file_paths:
        with open(path, 'r') as file:
            translation_name = os.path.basename(path).split('.')[0].upper()
            translations[translation_name] = json.load(file)
    return translations

# Load translations
translations = load_translations(file_paths)

# Function to compare translations
def compare_translations(translations):
    all_verses = set()
    translation_verses = {}

    for name, data in translations.items():
        verses = {(item['book'], item['chapter'], item['verse']) for item in data}
        all_verses |= verses
        translation_verses[name] = verses

    discrepancies = {}
    for name, verses in translation_verses.items():
        missing = sorted(all_verses - verses)
        additional = sorted(verses - all_verses)
        discrepancies[name] = {'missing': missing, 'additional': additional}

    return discrepancies

# Function to write discrepancies to a file in a friendly format
def write_discrepancies_to_file(discrepancies, filename):
    with open(filename, 'w') as file:
        for translation, details in discrepancies.items():
            file.write(f"Translation: {translation}\n")

            missing = details['missing']
            if missing:
                file.write("  Missing Verses:\n")
                for verse in missing:
                    book, chapter, verse_number = verse
                    file.write(f"    - {book} {chapter}:{verse_number}\n")
            else:
                file.write("  No Missing Verses.\n")

            additional = details['additional']
            if additional:
                file.write("  Additional Verses:\n")
                for verse in additional:
                    book, chapter, verse_number = verse
                    file.write(f"    - {book} {chapter}:{verse_number}\n")
            else:
                file.write("  No Additional Verses.\n")

            file.write("-" * 50 + "\n")

# Get discrepancies and write to a file
discrepancies = compare_translations(translations)
write_discrepancies_to_file(discrepancies, 'discrepancies.txt')

# Print a message to indicate that the discrepancies have been written to the file
print("Discrepancies have been written to discrepancies.txt")

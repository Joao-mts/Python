import re
from unidecode import unidecode

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)  # remove non-alphabetic characters
    text = text.lower()  # convert to lowercase
    text = remove_emoji(text)  # remove emojis
    text = unidecode(text)  # remove accents
    return text

def remove_emoji(string):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", string)


with open(r'C:/Users/john/Documents/ESTUDO/Project/chat_data_no_emoji.txt' , 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()
    cleaned_text = clean_text(text)

# Salvando o texto limpo em um novo arquivo
with open(r'C:/Users/john/Documents/ESTUDO/Project/chat_data_cleaned.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_text)

import re

raw_text = "Hello, world. Is this-- a test?"

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed)
print("Length of the Text: ",len(preprocessed))
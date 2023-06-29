#text to speech
from gtts import gTTS
import random
import string
import os

# Function to generate random text
def generate_random_text(length):
    letters = string.ascii_letters + string.digits + string.punctuation + " "
    return ''.join(random.choice(letters) for _ in range(length))

# Function to convert text to speech
def text_to_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)
    print("Speech saved to:", output_file)

# Generate random text
random_text = generate_random_text(50)

# Output file name
output_file = "output.mp3"

# Convert random text to speech
text_to_speech(random_text, output_file)

# Play the speech using a media player
os.system("start " + output_file)  # Works on Windows with default media player


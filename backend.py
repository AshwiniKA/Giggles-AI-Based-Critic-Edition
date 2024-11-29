import google.generativeai as genai  # Assuming you have this installed and available
from gtts import gTTS  # Google Text-to-Speech library
import os  # For file path handling
import pygame.mixer  # For playing audio with pygame

# Initialize the GenerativeModel (replace with actual initialization)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_content(prompt,update_output):
    """
    Generates content using the GenerativeModel and returns the result.
    """
    # Call the model's generate_content method with the user input
    response = model.generate_content("Can you give a short funny review of the movie / show "+prompt)

    # return translated_content

      # Return the response text by calling the update_output callback
    update_output(response.text)
    #Return the response text
    return response.text


def save_audio(text, language_code='en'):
    """
    Converts the text to an audio file (MP3) using gTTS and saves it to disk.
    """
    if not text:
        return "No content to convert to audio."

    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang=language_code)

    # Save the audio file (MP3)
    audio_file = "generated_audio.mp3"
    tts.save(audio_file)

    return f"Audio saved as {audio_file}"

def play_audio():
    """
    Play the generated audio file using pygame.mixer.
    """
    audio_file = "generated_audio.mp3"
    if os.path.exists(audio_file):
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
    else:
        print("No audio file found to play.")

def stop_audio():
    """
    Stop the audio playback using pygame.mixer.
    """
    pygame.mixer.music.stop()



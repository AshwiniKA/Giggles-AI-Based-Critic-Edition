# Giggles-AI-Based-Critic-Edition

### Content Generation and Audio Playback App
This project allows users to input a movie/show name, generate content based on that input, display the content, and convert it into an audio file. The application uses Tkinter for the UI, gTTS (Google Text-to-Speech) for text-to-speech conversion, and pygame for audio playback.

### Features
1. Content Generation: Enter a movie/show name, and the app generates related content.
2. Text-to-Speech: Converts generated text into an audio file using gTTS (Google Text-to-Speech).
3. Audio Playback: Plays the generated audio using pygame.
4. Stop Audio: Provides functionality to stop the audio playback.

### Requirements
To run the application, you need to install the following Python libraries:

1. Tkinter (for UI)
2. gTTS (for text-to-speech)
3. pygame (for audio playback)

### Install dependencies
1. pip install gTTS pygame
2. Ensure you have Python installed. This app works with Python 3.x.

### File Structure
ui.py: Handles the graphical user interface (GUI) and user interactions.
backend.py: Contains logic for content generation, text-to-speech conversion, and audio playback.
main.py: Entry point for running the application, which sets up the UI and backend connection.

### How to Run
Make sure your Python environment is set up and the required libraries are installed.
Ensure adding Gemini API key where 'Your Key' is mentioned
Run the app by executing main.py: python main.py
The app will open a GUI window where you can enter a movie/show name. Click Generate Content to see the result. The generated text will also be converted to an audio file that you can play or stop using the provided buttons.

### App Workflow
1. User Input: You enter the name of a movie or show.
2. Content Generation: The app generates related content (this part can be replaced with your own content generation logic).
3. Audio Conversion: The generated text is converted to an audio file using Google Text-to-Speech.
4. Playback Controls: You can play or stop the generated audio using buttons in the UI.

## Example
1. Provide Show or Movie Name: "Barbie"
2. Generate Content: The app generates a short funny review for the movie
3. Play Audio: The content is converted to speech and can be played using the Play Audio button.
<img width="778" alt="Screenshot 2024-11-28 at 5 43 41 PM" src="https://github.com/user-attachments/assets/6f781f82-2e65-4d4f-9c10-6ce88c87fddc">
<img width="776" alt="Screenshot 2024-11-28 at 5 43 55 PM" src="https://github.com/user-attachments/assets/33bd05a5-0fa5-480e-8839-6cba0e313a03">

   

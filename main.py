
import google.generativeai as genai
from gtts import gTTS
import tkinter as tk
from ui import create_ui
from backend import generate_content
import os

genai.configure(api_key="YOUR_KEY")




def main():
    # Create the Tkinter window and UI
    root = tk.Tk()
    root.title("Giggles : AI Based Critic Edition")
    root.geometry("700x450")
    
    # Create the UI and pass the model interface
    create_ui(root, generate_content)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Tell me about clouds")
# print(response.text)
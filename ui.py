import tkinter as tk
from tkinter import scrolledtext
import threading
import os  # For file path handling
import pygame.mixer  # For playing audio with pygame
from backend import generate_content, save_audio, play_audio, stop_audio  # Import backend functions



def create_ui(root, generate_content_callback):
    """
    Creates the user interface for the application.
    """
      # Set the background color of the main window to blue
    root.configure(bg="blue")

    # Initialize pygame mixer for audio playback
    pygame.mixer.init()

    # Add a label with a more concise prompt
    prompt_label = tk.Label(root, text="Provide Show or Movie Name")
    prompt_label.pack(pady=10)

    # Add a text entry widget for user input
    prompt_entry = tk.Entry(root, width=50, bg="white", fg="black")
    prompt_entry.pack(pady=10)


    # Add a button to trigger content generation
    feedback_label = tk.Label(root, text="", fg="red", bg="blue")
    feedback_label.pack(pady=5)

    def on_generate_button_click():
        prompt = prompt_entry.get().strip()
        if not prompt:
            feedback_label.config(text="Please enter a valid prompt.")
            return
        feedback_label.config(text="")  # Clear any error messages
        generate_button.config(state=tk.DISABLED)  # Disable button during processing
        feedback_label.config(text="Generating content...")  # Show feedback message
        run_generation_in_thread(prompt, update_output)
    generate_button = tk.Button(root, text="Generate Content", command=on_generate_button_click)
    generate_button.pack(pady=10)

    # Add a scrolled text widget to display the model's response
    output_text = scrolledtext.ScrolledText(root, width=70, height=10, wrap=tk.WORD)
    output_text.pack(pady=10)

    # Pass the output text box to backend so it can update the result
    def update_output(response_text):
        output_text.delete(1.0, tk.END)  # Clear previous content


        output_text.insert(tk.END, response_text)  # Insert new content
        generate_button.config(state=tk.NORMAL)  # Re-enable the button
        feedback_label.config(text="")  # Clear feedback message

        # Once content is generated, save it as audio
        save_audio(response_text, 'en')

    def run_generation_in_thread(prompt, update_output):
        """
        Runs the content generation in a separate thread to avoid blocking the UI.
        """
        threading.Thread(target=generate_content_callback, args=(prompt, update_output), daemon=True).start()



    # Add Play Audio Button
    play_button = tk.Button(root, text="Play Audio", command=play_audio, bg="lightblue", fg="black")
    play_button.pack(pady=10)

    # Add Stop Audio Button
    stop_button = tk.Button(root, text="Stop Audio", command=stop_audio, bg="lightblue", fg="black")
    stop_button.pack(pady=10)

    return update_output

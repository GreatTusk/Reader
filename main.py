import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to read text out loud
def read_text():
    text = text_var.get()
    engine.say(text)
    engine.runAndWait()


# Function to capture key presses and update the text variable
def log_key(event):
    current_text = text_var.get()
    # Handle backspace (delete last character)
    if event.keysym == 'BackSpace':
        current_text = current_text[:-1]
    else:
        # Append the pressed key to the current text
        current_text += event.char
    text_var.set(current_text)

    # Reset the reading timer
    if hasattr(log_key, 'after_id'):
        root.after_cancel(log_key.after_id)
    engine.stop()
    log_key.after_id = root.after(300, read_text)


# Create the main window
root = tk.Tk()
root.title("Lector de pantalla")

# Variable to store the captured text
text_var = tk.StringVar()

# Create a label to display the instructions
label = tk.Label(root, text="Empieza a escribir para que el texto sea leído:")
label.pack(pady=10)

# Create a label to display the captured text (optional)
display_label = tk.Label(root, textvariable=text_var)
display_label.pack(pady=10)

# Bind the log_key function to key press events
root.bind('<Key>', log_key)

# Run the application
root.mainloop()
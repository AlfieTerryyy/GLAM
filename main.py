import tkinter as tk
from tkinter import simpledialog, messagebox

def check_password():
    entered_password = password_entry.get()
    if entered_password == "2911107243":  # Replace with your desired password
        root.deiconify()  # Show the main window
        password_popup.destroy()  # Close the password popup
    else:
        password_entry.delete(0, tk.END)  # Clear the entry field
        password_entry.focus_set()  # Set focus back to the entry field
        messagebox.showerror("Incorrect Password", "Please enter the correct password.")

def apply_letter_mapping(user_input):
    letter_mapping = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w',
        'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
        'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
        'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
        'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a',
    }

    result = ""
    for char in user_input.lower():
        if char.isalpha():
            result += letter_mapping.get(char, char)
        else:
            result += char
    return result

def process_user_input():
    user_input = input_entry.get()
    output_text = apply_letter_mapping(user_input)
    output_label.config(text=f"Output: {output_text}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Lock with Letter Mapping")

# Hide the main window initially
root.withdraw()

# Create a password popup window
password_popup = tk.Toplevel(root)
password_popup.title("Enter Password")

# Create an entry field for the password
password_entry = tk.Entry(password_popup, show="*")
password_entry.pack()

# Create a button to check the password
check_button = tk.Button(password_popup, text="Enter", command=check_password)
check_button.pack()

# Set focus to the password entry field
password_entry.focus_set()

# Create an entry field for user input
input_entry = tk.Entry(root)
input_entry.pack()

# Create a button to process user input
process_button = tk.Button(root, text="Process Input", command=process_user_input)
process_button.pack()

# Create a label to display the processed output
output_label = tk.Label(root, text="")
output_label.pack()

# Start the Tkinter event loop
root.mainloop()

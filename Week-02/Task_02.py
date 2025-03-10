import tkinter as tk
from tkinter import messagebox
import random
import string

generated_passwords = []  # List to store the last 5 passwords

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Enable, update password field, then disable again
        entry_password.config(state=tk.NORMAL)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        entry_password.config(state=tk.DISABLED)
        
        # Save the last 5 passwords
        generated_passwords.append(password)
        if len(generated_passwords) > 5:
            generated_passwords.pop(0)
        
        # Update the password history display
        update_password_history()
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def update_password_history():
    history_text.config(state=tk.NORMAL)
    history_text.delete("1.0", tk.END)
    for idx, pwd in enumerate(reversed(generated_passwords), start=1):
        history_text.insert(tk.END, f"{idx}. {pwd}\n")
    history_text.config(state=tk.DISABLED)

# Creating main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# UI Elements
label_title = tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold"))
label_title.pack(pady=5)

label_length = tk.Label(root, text="Enter Password Length:")
label_length.pack()

entry_length = tk.Entry(root, width=5)
entry_length.pack()

button_generate = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white", font=("Arial", 10, "bold"))
button_generate.pack(pady=5)

entry_password = tk.Entry(root, width=30, font=("Arial", 12), justify='center', state=tk.DISABLED)
entry_password.pack(pady=5)

button_copy = tk.Button(root, text="Copy Password", command=copy_password, bg="green", fg="white", font=("Arial", 10, "bold"))
button_copy.pack(pady=5)

label_history = tk.Label(root, text="Last 5 Passwords:", font=("Arial", 10, "bold"))
label_history.pack()

history_text = tk.Text(root, height=5, width=30, font=("Arial", 10), state=tk.DISABLED)
history_text.pack(pady=5)

root.mainloop()
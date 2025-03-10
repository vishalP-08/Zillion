import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")  # Adjusted for compact layout
root.resizable(False, False)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, pady=5, padx=5, sticky="nsew")

# Buttons layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 18), width=6, height=2, 
                           command=lambda t=text: on_click(t))
        button.grid(row=r, column=c, padx=0, pady=0, sticky="nsew")  # Removed spacing between buttons

# Configure row and column weights for uniform button resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
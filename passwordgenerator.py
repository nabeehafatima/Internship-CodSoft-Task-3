import tkinter as tk
from tkinter import StringVar, IntVar
from random import choice, shuffle

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_var = StringVar()
        self.length_var = IntVar(value=12)
        self.use_lowercase_var = IntVar(value=1)
        self.use_uppercase_var = IntVar(value=1)
        self.use_digits_var = IntVar(value=1)
        self.use_symbols_var = IntVar(value=1)

        self.create_widgets()

    def create_widgets(self):
        # Label for length
        length_label = tk.Label(self.root, text="Password Length:")
        length_label.pack(pady=5)

        # Entry for length
        length_entry = tk.Entry(self.root, textvariable=self.length_var, width=5, justify='center')
        length_entry.pack(pady=5)

        # Checkbuttons for complexity
        use_lowercase_check = tk.Checkbutton(self.root, text="Lowercase", variable=self.use_lowercase_var)
        use_lowercase_check.pack()

        use_uppercase_check = tk.Checkbutton(self.root, text="Uppercase", variable=self.use_uppercase_var)
        use_uppercase_check.pack()

        use_digits_check = tk.Checkbutton(self.root, text="Digits", variable=self.use_digits_var)
        use_digits_check.pack()

        use_symbols_check = tk.Checkbutton(self.root, text="Symbols", variable=self.use_symbols_var)
        use_symbols_check.pack()

        # Label for generated password
        password_label = tk.Label(self.root, text="Generated Password:")
        password_label.pack(pady=10)

        # Entry for generated password
        password_entry = tk.Entry(self.root, textvariable=self.password_var, state='readonly', width=30, font=('Helvetica', 12, 'bold'))
        password_entry.pack(pady=10)

        # Button
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

    def generate_password(self):
        # Define character sets based on user preferences
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz' if self.use_lowercase_var.get() else ''
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if self.use_uppercase_var.get() else ''
        digits = '0123456789' if self.use_digits_var.get() else ''
        symbols = '!@#$%^&*()_-+=<>?' if self.use_symbols_var.get() else ''

        # Combine the character sets
        all_characters = lowercase_letters + uppercase_letters + digits + symbols

        # Check if at least one character set is selected
        if not all_characters:
            self.password_var.set("Select at least one character set")
            return

        # Generate a password with a random combination of characters
        password_list = [choice(all_characters) for _ in range(self.length_var.get())]
        shuffle(password_list)

        # Set the generated password in the Entry widget
        self.password_var.set(''.join(password_list))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

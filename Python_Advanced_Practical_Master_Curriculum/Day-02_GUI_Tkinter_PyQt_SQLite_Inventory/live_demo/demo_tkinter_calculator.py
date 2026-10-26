# demo_tkinter_calculator.py
# Clean, modern GUI Calculator built using Tkinter

import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GLA HPC Calculator")
        self.root.geometry("340x440")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2E")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._create_widgets()

    def _create_widgets(self):
        # Display Screen
        screen_frame = tk.Frame(self.root, bg="#1E1E2E")
        screen_frame.pack(expand=True, fill="both", padx=10, pady=10)

        entry = tk.Entry(
            screen_frame, 
            textvariable=self.display_var, 
            font=("Segoe UI", 26, "bold"), 
            bg="#181825", 
            fg="#CDD6F4", 
            bd=0, 
            justify="right",
            state="readonly"
        )
        entry.pack(expand=True, fill="both", ipady=12)

        # Buttons Grid
        btn_frame = tk.Frame(self.root, bg="#1E1E2E")
        btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ('C', 0, 0, '#F38BA8'), ('(', 0, 1, '#89B4FA'), (')', 0, 2, '#89B4FA'), ('/', 0, 3, '#FAB387'),
            ('7', 1, 0, '#313244'), ('8', 1, 1, '#313244'), ('9', 1, 2, '#313244'), ('*', 1, 3, '#FAB387'),
            ('4', 2, 0, '#313244'), ('5', 2, 1, '#313244'), ('6', 2, 2, '#313244'), ('-', 2, 3, '#FAB387'),
            ('1', 3, 0, '#313244'), ('2', 3, 1, '#313244'), ('3', 3, 2, '#313244'), ('+', 3, 3, '#FAB387'),
            ('0', 4, 0, '#313244'), ('.', 4, 1, '#313244'), ('DEL', 4, 2, '#A6ADC8'), ('=', 4, 3, '#A6E3A1')
        ]

        for text, r, c, bg_col in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 14, "bold"),
                bg=bg_col,
                fg="#11111B" if bg_col in ['#F38BA8', '#A6E3A1', '#FAB387', '#89B4FA'] else "#CDD6F4",
                bd=0,
                relief="flat",
                command=lambda t=text: self._on_button_click(t)
            )
            btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

    def _on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Mathematical Expression")
                self.expression = ""
                self.display_var.set("0")
        else:
            if self.display_var.get() == "0" and char not in ['.', '/', '*', '+', '-']:
                self.expression = char
            else:
                self.expression += char
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    print("[*] Starting Tkinter Calculator GUI...")
    root.mainloop()

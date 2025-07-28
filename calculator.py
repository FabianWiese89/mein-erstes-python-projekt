import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taschenrechner")
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        self.expression = tk.StringVar()

        entry = ttk.Entry(self, textvariable=self.expression, font=("Arial", 16), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0),
        ]

        for (text, row, col) in buttons:
            action = lambda t=text: self._on_button_click(t)
            ttk.Button(self, text=text, command=action, width=5).grid(row=row, column=col, padx=2, pady=2)

        # adjust column weights
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def _on_button_click(self, char):
        if char == 'C':
            self.expression.set('')
        elif char == '=':
            try:
                result = str(eval(self.expression.get()))
                self.expression.set(result)
            except Exception:
                self.expression.set('Fehler')
        else:
            self.expression.set(self.expression.get() + char)

if __name__ == '__main__':
    Calculator().mainloop()

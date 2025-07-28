import tkinter as tk
import math

ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith('_')}

class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Wissenschaftlicher Taschenrechner')
        self.root.configure(bg='black')

        self.display = tk.Entry(self.root, font=('Helvetica', 20), bd=0, bg='#353535', fg='white', justify='right', insertbackground='white')
        self.display.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'log',
            '1', '2', '3', '-', 'sin',
            '0', '.', '=', '+', 'cos',
            '(', ')', 'pi', '^', 'tan'
        ]
        row = 1
        col = 0
        for b in buttons:
            action = lambda x=b: self.on_click(x)
            button = tk.Button(self.root, text=b, command=action, font=('Helvetica', 16), bg='black', fg='white', width=4, height=2, bd=1, relief='raised')
            button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            self.root.columnconfigure(i, weight=1)
        for i in range(row+1):
            self.root.rowconfigure(i, weight=1)

    def on_click(self, char):
        if char == '=':
            expr = self.display.get()
            try:
                result = eval(expr, {'__builtins__': {}}, ALLOWED_NAMES)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, 'Error')
        elif char == 'pi':
            self.display.insert(tk.END, str(math.pi))
        elif char == 'sqrt':
            self.display.insert(tk.END, 'sqrt(')
        elif char in ('sin', 'cos', 'tan', 'log'):
            self.display.insert(tk.END, char + '(')
        elif char == '^':
            self.display.insert(tk.END, '**')
        else:
            self.display.insert(tk.END, char)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    CalculatorGUI().run()

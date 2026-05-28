import tkinter as tk
from tkinter import messagebox
import math

# WINDOW #
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x700")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# ---------------- VARIABLES ---------------- #
expression = ""
input_text = tk.StringVar()

# ---------------- DISPLAY ---------------- #
entry = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    justify="right"
)
entry.pack(pady=20, ipadx=10, ipady=10)

# ---------- BASIC FUNCTIONS ------------ #
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# ---------------- CALCULATION ---------------- #
def calculate():
    global expression

    try:
        result = eval(expression, {"__builtins__": None}, {
            "math": math,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log10,
            "sqrt": math.sqrt,
            "π": math.pi
        })

        if isinstance(result, float) and abs(result) < 1e-10:
            result = 0

        input_text.set(result)
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

# ---------------- DEGREE  ---------------- #
def degree_to_radian():
    global expression
    try:
        expr = expression.replace("π", str(math.pi))
        value = eval(expr, {"__builtins__": None}, {"math": math})

        result = math.radians(float(value))

        if abs(result) < 1e-10:
            result = 0

        input_text.set(result)
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()



# ---------------- FRAME ---------------- #
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# ---------------- NUMBER BUTTONS ---------------- #
buttons = [
    ('7',0,0),('8',0,1),('9',0,2),('/',0,3),
    ('4',1,0),('5',1,1),('6',1,2),('*',1,3),
    ('1',2,0),('2',2,1),('3',2,2),('-',2,3),
    ('0',3,0),('.',3,1),('=',3,2),('+',3,3),
]

for (text,r,c) in buttons:
    if text == "=":
        cmd = calculate
        color = "#ff9500"
    else:
        cmd = lambda x=text: button_click(x)
        color = "#333333"

    tk.Button(frame, text=text, width=8, height=3,
              command=cmd, bg=color, fg="white",
              bd=0).grid(row=r, column=c, padx=5, pady=5)

# ---------------- SCIENTIFIC BUTTONS ---------------- #
scientific = [
    ("sin(", lambda: button_click("sin(")),
    ("cos(", lambda: button_click("cos(")),
    ("tan(", lambda: button_click("tan(")),
    ("log(", lambda: button_click("log(")),
    ("√(", lambda: button_click("sqrt(")),
    ("π", lambda: button_click("π")),
    ("(", lambda: button_click("(")),
    (")", lambda: button_click(")")),
]

r = 4
c = 0

for text, cmd in scientific:
    tk.Button(frame, text=text, width=8, height=3,
              command=cmd,
              bg="#444444", fg="white",
              bd=0).grid(row=r, column=c, padx=5, pady=5)

    c += 1
    if c > 3:
        c = 0
        r += 1

# ---------------- CONTROL BUTTONS ---------------- #
tk.Button(frame, text="C", width=17, height=3,
          bg="#d32f2f", fg="white",
          command=clear).grid(row=6, column=0, columnspan=2)

tk.Button(frame, text="⌫", width=17, height=3,
          bg="#1976d2", fg="white",
          command=backspace).grid(row=6, column=2, columnspan=2)

# ---------------- DEGREE BUTTON ---------------- #
tk.Button(frame, text="Deg→Rad", width=17, height=3,
          bg="#555555", fg="white",
          command=degree_to_radian).grid(row=7, column=0, columnspan=2)

root.mainloop()
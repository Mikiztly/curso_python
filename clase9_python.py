""" import tkinter as tk
from tkinter import ttk
from tkinter import messagebox """

""" def saludar():
    mensaje = caja.get()
    saludo.config(text=mensaje)

#messagebox.showinfo(title="Información", message="Esto solo es información")
#messagebox.showwarning(title="Advertencia", message="Esto solo es una advertencia")
messagebox.showerror(title="Error", message="Te mandaste una macana")

ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.config(width=300, height=300)

label = ttk.Label(text="Ingrese el saludo")
label.place(x=10, y=10)

caja = ttk.Entry()
caja.place(x=10, y=40)

boton = ttk.Button(text="Saludo", command=saludar)
boton.place(x=10, y=70, width=100, height=25)

lista_desplegable = ttk.Combobox(values=["Papas", "Manzanas","Peras","Uvas"])
lista_desplegable.place(x=10,y=100)

checkbox = ttk.Checkbutton(text="Checkbox")
checkbox.place(x=10, y=130)

saludo = ttk.Label(text="")
saludo.place(x=10, y=200)

ventana.mainloop() """

import tkinter as tk
from tkinter import messagebox

'''
Ubuntu:
sudo apt install python3-tk

Para crear el instalador:

pyinstaller --noconsole --onefile clase9.py
pyinstaller --noconsole clase9.py
pyinstaller --onefile clase9.py
'''

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora")
        self.config(width=280, height=420)
        self.resizable(False, False)
        
        self.result_var = tk.StringVar()
        
        self.display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.display.place(x=20,y=20, width=240, height=60)
        
        botones = [
            ('7', 20, 100), ('8', 80, 100), ('9', 140, 100), ('/', 200, 100),
            ('4', 20, 160), ('5', 80, 160), ('6', 140, 160), ('*', 200, 160),
            ('1', 20, 220), ('2', 80, 220), ('3', 140, 220), ('-', 200, 220),
            ('0', 20, 280), ('.', 80, 280), ('=', 140, 280), ('+', 200, 280),
        ]
        
        for (text,x,y) in botones:
            self.create_button(text,x,y)
            
        self.create_button("C", 20, 340, width=240)
        
    def create_button(self, text,x,y, width=60, height=60):
        button = tk.Button(self, text=text, font=("Arial", 18), width=4, height=2,command=lambda: self.on_button_click(text))
        button.place(x=x, y=y, width=width, height=height)
        
    
    def on_button_click(self, text):
        current = self.result_var.get()
        
        if text == "C":
            self.result_var.set("")
        elif text == "=":
            try:
                result = str(eval(current))
                self.result_var.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Operacion inválida", "¡No puedes dividir un numero por cero!")
            except Exception as e:
                messagebox.showerror("Error insesperado", f"Ocurrio un error inesperado: {str(e)}")
                self.result_var.set("0")
        else:
            self.result_var.set(current + text)
            
if __name__=="__main__":
    app = Calculadora()
    app.mainloop()
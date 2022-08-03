import tkinter
from tkinter import ttk

"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que 
contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.
"""
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)



selected = tkinter.StringVar()
botonRadius1= ttk.Radiobutton(window, text='Rojo', value='1', variable=selected)
botonRadius2 = ttk.Radiobutton(window, text='Verde', value='2',variable=selected)
botonRadius3 = ttk.Radiobutton(window, text='Azul', value='3', variable=selected)

botonRadius1.grid(column=0, row=1, padx=5, pady=5)
botonRadius2.grid(column=0, row=2, padx=5, pady=5)
botonRadius3.grid(column=0, row=3, padx=5, pady=5)

def reiniciar(event):
    return not selected


botonReinicio = ttk.Button(window, text='Reiniciar')
botonReinicio.grid(column=0, row=4, padx=10, pady=10)
botonReinicio.bind('<Button-1>', reiniciar)


window.mainloop()

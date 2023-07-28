from tkinter import *
from tkinter import ttk


def hitung(*args):
	try: 
		nilai=float(celcius.get())
		fahrenheit.set((9/5 * nilai )+32)
	except ValueError:
		pass

root = Tk()
root.title("Ubah Celcius Menjadi Fahrenheit")

jendela = ttk.Frame(root, padding = "10 10 20 20")
jendela.grid(column=0, row=0, sticky=(N,W,E,S))
jendela.columnconfigure(0, weight=1)
jendela.rowconfigure(0, weight=1)

celcius = StringVar()
fahrenheit = StringVar()

celcius_entry = ttk.Entry(jendela, width=7, textvariable=celcius)
celcius_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(jendela, textvariable=fahrenheit).grid(column=2,row=2, sticky=(W,E))
ttk.Button(jendela, text="Hitung", command= hitung).grid(column=3, row=3, sticky=W)

ttk.Label(jendela, text="Celcius").grid(column=3, row=1, sticky=W)
ttk.Label(jendela, text="sama dengan").grid(column=1, row=2, sticky=E)
ttk.Label(jendela, text="Fahrenheit").grid(column=3, row=2, sticky=W)

for child in jendela. winfo_children():
	child.grid_configure(padx=5, pady=5)

celcius_entry.focus()
root.bind('<Return>', hitung)

root.mainloop()




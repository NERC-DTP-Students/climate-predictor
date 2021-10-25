from tkinter import *
from tkinter import ttk

def make_value_entry(root,caption,rowno,default_initial, default_rate, unit):
    label = ttk.Label(root, width = 10, text = caption)
    label.grid(row = rowno, column = 0)
    entry = ttk.Entry(root, width = 10, textvariable = default_initial)
    entry.grid(row = rowno, column = 1)
    label = ttk.Label(root, width = 10, text = unit)
    label.grid(row = rowno, column = 2)
    entry = ttk.Entry(root, width = 10, textvariable = default_rate)
    entry.grid(row = rowno, column = 3)
    label = ttk.Label(root, width = 10, text = unit+' per yr')
    label.grid(row = rowno, column = 4)


#def make_slider_entry():

root = Tk()
root.title('Climate Predictor')

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

albedo_initial = StringVar(value = 0.3)
albedo_rate = StringVar(value = 0)
albedo = make_value_entry(root,'Albedo',1, albedo_initial, albedo_rate, '%')
duration = make_value_entry(root,'Duration', 2, albedo_initial, albedo_rate, '%')
root.mainloop()


'''
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

'''
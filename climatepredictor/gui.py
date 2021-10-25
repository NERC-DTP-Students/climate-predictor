from tkinter import *
from tkinter import ttk

def make_value_entry(root,caption,rowno,colno,default_initial, default_rate, unit):
    
    new_frame = ttk.Frame(root, padding="12 12 12 12")
    new_frame.grid(column=colno, row=rowno, sticky=(N, W, E, S),columnspan=5)
    label = ttk.Label(new_frame, width = 10, text = caption)
    label.grid(row = 0, column = 0)
    entry = ttk.Entry(new_frame, width = 10, textvariable = default_initial)
    entry.grid(row = 0, column = 1)
    label = ttk.Label(new_frame, width =10, text = unit)
    label.grid(row = 0, column = 2)
    entry = ttk.Entry(new_frame, width = 10, textvariable = default_rate)
    entry.grid(row = 0, column = 3)
    label = ttk.Label(new_frame, width = 10, text = unit+' per yr')
    label.grid(row = 0, column = 4)


#def make_slider_entry():

root = Tk()
#set style
root.tk.call('source','climatepredictor/sun-valley.tcl')
root.tk.call('set_theme','dark')
root.title('Climate Predictor')

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#make frame for changing variables
varframe=ttk.Frame(root, padding="12 12 12 12")
varframe.grid(column=0, row=0, sticky=(N, W, E, S))
varframe.columnconfigure(0, weight=1)
varframe.rowconfigure(0, weight=1)

#make frame for plot options
plotframe=ttk.Frame(root, padding="12 12 12 12")
plotframe.grid(column=0, row=1, sticky=(N, W, E, S))
plotframe.columnconfigure(0, weight=1)
plotframe.rowconfigure(0, weight=1)

#customise variable frame
ttk.Label(varframe, text='Variable Options',width=30).grid(column=1,row=0, sticky='')
#label_frame=ttk.Frame(varframe,padding="12 12 12 12")
#label_frame.grid(row=1,column=0,columnspan=2,rowspan=1,sticky='')

ttk.Label(varframe, text='Variable',width=10).grid(column=0,row=1, sticky='')
ttk.Label(varframe, text='Initial amount',width=15).grid(column=1,row=1, sticky='')
ttk.Label(varframe, text='Change',width=10).grid(column=2,row=1, sticky='')


#customise plot frame
ttk.Label(plotframe, text='Plot Options',width=30).grid(column=1,row=0, sticky='')


albedo_initial = StringVar(value = 0.3)
albedo_rate = StringVar(value = 0)
albedo = make_value_entry(varframe,'Albedo',2,0, albedo_initial, albedo_rate, '%')
duration = make_value_entry(varframe,'Duration', 3,0, albedo_initial, albedo_rate, '%')



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
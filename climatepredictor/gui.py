from tkinter import *
from tkinter import ttk

def make_value_entry(root,caption,rowno,colno,default_initial, default_rate, unit):
    
    new_frame = ttk.Frame(root, padding="12 12 12 12")
    new_frame.grid(column=colno, row=rowno, sticky=(N, W, E, S),columnspan=4,rowspan=1)
    new_frame.columnconfigure(0, weight=1)
    new_frame.rowconfigure(0, weight=1)
    label = ttk.Label(new_frame, width = 10, text = caption)
    label.grid(row = 0, column = 0)
    entry = ttk.Entry(new_frame, width = 10, textvariable = default_initial)
    entry.grid(row = 0, column = 1)
    label = ttk.Label(new_frame, width =5, text = unit)
    label.grid(row = 0, column = 2)
    entry = ttk.Entry(new_frame, width = 5, textvariable = default_rate)
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
plotframe.grid(column=0, row=10, sticky=(N, W, E, S))
plotframe.columnconfigure(0, weight=1)
plotframe.rowconfigure(0, weight=1)

#customise variable frame
ttk.Label(varframe, text='Variable Options',width=30).grid(column=1,row=0, sticky=(N, W, E, S))

#create widget for labels
label_frame=ttk.Frame(varframe,padding="12 12 12 12")
label_frame.grid(row=1,column=0,columnspan=4,rowspan=1,sticky=(N,W,E,S))
label_frame.columnconfigure(0, weight=1)
label_frame.rowconfigure(0, weight=1)
ttk.Label(label_frame, text='Variable',width=10).grid(column=0,row=1, sticky=(N, W, E, S))
ttk.Label(label_frame, text='Initial amount',width=15).grid(column=1,row=1, sticky=(N, W, E, S))
ttk.Label(label_frame, text='Change',width=15).grid(column=5,row=1, sticky=(N, W, E, S))


#customise plot frame
ttk.Label(plotframe, text='Plot Options',width=30).grid(column=1,row=0, sticky=(N, W, E, S))

#default values
#change this to accurate values later
albedo_initial = float(0.3)
albedo_rate = float(0)
cloud_initial=float(10)
cloud_rate=float(0)
alpha1_initial=0.3
alpha1_rate=0.1
alpha2_initial=0.4
alpha2_rate=0.1
epsilon1_initial=0.3
epsilon1_rate=0.1
epsilon2_initial=0.4
epsilon2_rate=0.1

make_value_entry(varframe,u'CO\u2082 conc.',2,0, albedo_initial, albedo_rate, 'ppm')
make_value_entry(varframe,'Cloud cover', 3,0, cloud_initial, cloud_rate, '%')



advanced_frame=ttk.Frame(varframe,padding="12 12 12 12")
advanced_frame.grid(column=0,row=7,sticky=(N,W,E,S),columnspan=4,rowspan=5)
make_value_entry(advanced_frame,u'\u03B1\u2081',0,0,alpha1_initial,alpha1_rate,'')
make_value_entry(advanced_frame,u'\u03B1\u2082',1,0,alpha2_initial,alpha2_rate,'')
make_value_entry(advanced_frame,u'\u03B5\u2081',2,0,epsilon1_initial,epsilon1_rate,'')
make_value_entry(advanced_frame,u'\u03B5\u2082',3,0,epsilon2_initial,epsilon2_rate,'')
ttk.Label(advanced_frame,text=u'S\u2080/present day solar flux').grid(column=0,row=4, sticky=(N, W, E, S))
solar_flux=float()
ttk.Entry(advanced_frame,textvariable=solar_flux).grid(column=1,row=4, sticky=(N, W, E, S))
advanced_frame.grid_remove()

def reveal():
    hide_button=ttk.Button(varframe,text='Hide',command=hide).grid(row=6,column=1)
    return advanced_frame.grid(), hide_button

def hide():
    return advanced_frame.grid_remove()

button=ttk.Button(varframe,text='Advanced Options',command=reveal)
button.grid(row=6, column=0)

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
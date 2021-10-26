from tkinter import *
from tkinter import ttk

def make_value_entry(root,caption,rowno,colno,default_initial, default_rate, unit):
    
    new_frame = ttk.Frame(root, padding="12 12 12 12")
    new_frame.grid(column=colno, row=rowno, sticky=(N, W, E, S),columnspan=4)
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
root.geometry('1000x200')
root.resizable(False,False)
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

#add input parameters
albedo_initial = StringVar(value = 0.3)
albedo_rate = StringVar(value = 0)
albedo = make_value_entry(varframe,'Albedo',2,0, albedo_initial, albedo_rate, '')
cloud_cover = make_value_entry(varframe,'Cloud cover', 3,0, albedo_initial, albedo_rate, '%')

#add time widget with slider
slider_frame = ttk.Frame(root)
slider_frame.grid(column = 0, row = 0)
slider_frame.rowconfigure(0,weight=2)
slider_frame.rowconfigure(1,weight=2)
slider_label = ttk.Label(slider_frame, text='Time:')
slider_label.grid(column=0,row=0,sticky='nw')
interval_initial = IntVar(value = 1)
label = ttk.Label(slider_frame, width = 13, text = 'Change Interval:')
label.grid(row = 1, column = 0, sticky='ew')
entry = ttk.Entry(slider_frame, width = 4, textvariable = interval_initial)
entry.grid(row = 1, column = 1, sticky='ew')
label = ttk.Label(slider_frame, width = 10, text = 'years')
label.grid(row = 1, column = 2, sticky='ew')
label = ttk.Label(slider_frame, width = 8, text = 'Duration:')
label.grid(row = 1, column = 3, sticky='ew')
current_value = StringVar(value=0)
value_entry = ttk.Entry(slider_frame, width = 4, textvariable = current_value)
value_entry.grid(row = 1, column = 4, sticky='ew')
label = ttk.Label(slider_frame, width = 6, text = 'years')
label.grid(row = 1, column = 5, sticky='ew')
slider = Scale(slider_frame, 
                    from_ = 0, 
                    to=100,
                    length = 300, 
                    orient = 'horizontal',
                    command = lambda s:current_value.set('%0.0f' % float(s)), 
                    variable = current_value,
                    tickinterval = 25,
                    showvalue = False
                    )
slider.grid(row=1,column=6,sticky='we')

#add advanced frame dropdown
advanced_frame=ttk.Frame(varframe,padding="12 12 12 12")
advanced_frame.grid(column=0,row=3,sticky=(N,W,E,S))
ttk.Label(advanced_frame,text='Hey').grid(column=0,row=0,sticky='')
advanced_frame.grid_remove()

def reveal():
    return advanced_frame.grid()
button=ttk.Button(plotframe,text='Click',command=reveal)
button.grid(row=5)

root.mainloop()

print(current_value.get())
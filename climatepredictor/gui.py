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
root.geometry('1000x200')
root.resizable(False,False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
#root.rowconfigure(0, weight=1)
#root.rowconfigure(1, weight=1)

#albedo_initial = StringVar(value = 0.3)
#albedo_rate = StringVar(value = 0)
#albedo = make_value_entry(root,'Albedo',1, albedo_initial, albedo_rate, '%')
#duration = make_value_entry(root,'Duration', 2, albedo_initial, albedo_rate, '%')
'''def get_current_value():
    return '{: .0f}'.format(current_value.get())
def slider_changed(event):
    value_entry.configure(textvariable=get_current_value())'''

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
#value_label = ttk.Label(slider_frame,text=get_current_value())
#value_label.grid(row=1,column=7,columnspan=2,sticky='n')
#current_value_label = ttk.Label(slider_frame, text=' yrs')
#current_value_label.grid(row=1, column = 8,columnspan=2,sticky='ew')#,ipadx=10,ipady=10)

root.mainloop()

print(current_value.get())
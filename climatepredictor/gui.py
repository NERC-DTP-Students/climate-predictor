from tkinter import *
from tkinter import ttk

#functions for creating entry types

#function for making entry for user friendly options
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

#make simple entry with one label
def make_simple_entry(root,label,variable,rowno,colno):
    new_label=ttk.Label(root,text=label,width=10)
    new_label.grid(row=rowno,column=colno)
    new_entry=ttk.Entry(root,width=10,textvariable=variable)
    new_entry.grid(row=rowno,column=colno+1)

#function for making a Radiobutton
def make_radio_button(frame,name,variable_in,value_in,rowno):
    radio_button=ttk.Radiobutton(frame,text=name,variable=variable_in, value=value_in)
    radio_button.grid(column=0,row=rowno)

#function for making a Checkbutton
def make_check_button(frame,name,variable_in,initial_state,rowno):
    check_button=ttk.Checkbutton(frame,text=name,variable=variable_in,onvalue='On',offvalue='Off')
    check_button.grid(column=0,row=rowno)
    check_button.state(['!alternate']) #clear alternate state
    if initial_state=='On':
        check_button.state(['selected'])
    else:
        check_button.state(['!selected'])


root = Tk()
#set style
root.tk.call('source','climatepredictor/sun-valley.tcl')
root.tk.call('set_theme','dark')
root.title('Climate Predictor')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#create mainframe
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#make frame for changing variables - row 0 of mainframe
varframe=ttk.Frame(root, padding="12 12 12 12")
varframe.grid(column=0, row=0, sticky=(N, W, E, S))
varframe.columnconfigure(0, weight=1)
varframe.rowconfigure(0, weight=1)

#make frame for plot options - row 1 of mainframe
plotframe=ttk.Frame(root, padding="12 12 12 12")
plotframe.grid(column=0, row=1, sticky=(N, W, E, S))
plotframe.columnconfigure(0, weight=1)
plotframe.rowconfigure(0, weight=1)

######################## Customise Variable Frame ################################################################
#default values
#change this to accurate values later
co2_initial = DoubleVar(root,value = 278.0)#preindustrial
co2_rate =  DoubleVar(root,value = 0.0)
cloud_initial=  DoubleVar(root,value = 10.0)
cloud_rate= DoubleVar(root,value = 0.0)
alpha1_initial= DoubleVar(root,value = 0.3)
alpha1_rate= DoubleVar(root,value = 0.0)
alpha2_initial= DoubleVar(root,value = 0.4)
alpha2_rate= DoubleVar(root,value = 0.0)
epsilon1_initial= DoubleVar(root,value = 0.3)
epsilon1_rate= DoubleVar(root,value = 0.0)
epsilon2_initial= DoubleVar(root,value = 0.4)
epsilon2_rate= DoubleVar(root,value = 0.0)


ttk.Label(varframe, text='Variable Options',width=30).grid(column=1,row=0, sticky=(N, W, E, S))

#create frame for labels - row=1, column=0 in variable frame
#spans the same number of rows as the make_new_entry thing so it lines up
label_frame=ttk.Frame(varframe,padding="12 12 12 12")
label_frame.grid(row=1,column=0,columnspan=4,rowspan=1,sticky=(N,W,E,S))
label_frame.columnconfigure(0, weight=1)
label_frame.rowconfigure(0, weight=1)

variable_label=ttk.Label(label_frame, text='Variable',width=10)
variable_label.grid(column=0,row=1, sticky=(N, W, E, S))
intial_amount_label=ttk.Label(label_frame, text='Initial amount',width=15)
intial_amount_label.grid(column=1,row=1, sticky=(N, W, E, S))
change_label=ttk.Label(label_frame, text='Change',width=15)
change_label.grid(column=2,row=1, sticky=(N, W, E, S))

#add our entry options rows 2,3 in variable frame
make_value_entry(varframe,u'CO\u2082 conc.',2,0, co2_initial, co2_rate, 'ppm')
make_value_entry(varframe,'Cloud cover', 3,0, cloud_initial, cloud_rate, '%')

#add advanced frame dropdown in variable frame row 4
advanced_frame=ttk.Frame(varframe,padding="12 12 12 12")
advanced_frame.grid(column=0,row=5,sticky=(N,W,E,S),rowspan=1)
make_value_entry(advanced_frame,u'\u03B1\u2081',0,0,alpha1_initial,alpha1_rate,'')
make_value_entry(advanced_frame,u'\u03B1\u2082',1,0,alpha2_initial,alpha2_rate,'')
make_value_entry(advanced_frame,u'\u03B5\u2081',2,0,epsilon1_initial,epsilon1_rate,'')
make_value_entry(advanced_frame,u'\u03B5\u2082',3,0,epsilon2_initial,epsilon2_rate,'')
solar_label=ttk.Label(advanced_frame,text=u'S\u2080/present day solar flux')
solar_label.grid(column=0,row=4, sticky=(N, W, E, S))
solar_flux=float()
solar_entry=ttk.Entry(advanced_frame,textvariable=solar_flux)
solar_entry.grid(column=1,row=4, sticky=(N, W, E, S))
advanced_frame.grid_remove()

#functions for button for advanced frame
def reveal():
    
    return advanced_frame.grid(), hide_button

def hide():
    
    return advanced_frame.grid_remove(),hide_button.grid_remove()


button=ttk.Button(varframe,text='Advanced Options',command=reveal)
button.grid(row=4, column=0)
hide_button=ttk.Button(varframe,text='Hide',command=hide)
hide_button.grid(row=4,column=1)

#add land use widget here, row 6 in variable frame
from climatepredictor.slider_setup_2 import Slider
slider_frame=ttk.Frame(varframe,padding="12 12 12 12")
slider_frame.grid(row=6,column=0)


# initial positions on the slider (calculated from initial percentages)
init_positions = [25,50,75]
# create the slider
slider = Slider(slider_frame, width = 400, height = 60, min_val = 0, max_val = 100, init_lis = init_positions, show_value = True)
slider.grid(row=0,column=0)
# Entry boxes for the different values
# use make_simple_entry(root,label,variable,rowno,colno):
forest_value = make_simple_entry(slider_frame,'Forest',slider.forest_perc,1,0)
ice_value = make_simple_entry(slider_frame,'Ice',slider.ice_perc,2,0)
water_value = make_simple_entry(slider_frame,'Water',slider.water_perc,3,0)
desert_value = make_simple_entry(slider_frame,'Desert',slider.desert_perc,4,0)

#add time widget with slider - row 8 in variable frame
if(cloud_rate.get() != 0.0):
    print(cloud_rate.get())
slider_frame = ttk.Frame(varframe)
slider_frame.grid(column = 0, row = 8,columnspan=4,rowspan=1)
slider_frame.rowconfigure(0,weight=2)
slider_frame.rowconfigure(1,weight=2)
slider_label = ttk.Label(slider_frame, text='Time:')
slider_label.grid(column=0,row=0,sticky='')
interval_initial = IntVar(value = 1)
label = ttk.Label(slider_frame, width = 13, text = 'Change Interval:')
label.grid(row = 1, column = 0, sticky='')
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



############################################ Customise plotting frame ###########################################
#title frame
plot_options_label=ttk.Label(plotframe, text='Plot Options',width=30)
plot_options_label.grid(column=1,row=0, sticky=(N, W, E, S))

def plotting(): #add sol's function here
    pass

# 4 frames
xaxis_frame=ttk.Frame(plotframe,padding="12 12 12 12")
xaxis_frame.grid(row=1,column=0,sticky=(N,W,E,S))
yaxis_frame=ttk.Frame(plotframe,padding="12 12 12 12")
yaxis_frame.grid(row=1,column=1,sticky=(N,W,E,S))
xaxis_advanced=ttk.Frame(plotframe,padding="12 12 12 12")
xaxis_advanced.grid(row=2,column=0,sticky=(N,W,E,S))
save_frame=ttk.Frame(plotframe,padding="12 12 12 12")
save_frame.grid(row=2,column=1,sticky=(N,W,E,S))

# customise x axis frame
xaxis_label=ttk.Label(xaxis_frame,text='X Axis')
xaxis_label.grid(column=0,row=0)
make_radio_button(xaxis_frame,'Time','xaxis','time',1)
make_radio_button(xaxis_frame,'Cloud clover','xaxis','cloud cover',2)
make_radio_button(xaxis_frame,u'CO\u2082','xaxis','co2',3)

# customise y axis frame
yaxis_label=ttk.Label(yaxis_frame,text='Y Axis')
yaxis_label.grid(column=0,row=0)
make_check_button(yaxis_frame,u'T\u2081','plot_T1','Off',1)
make_check_button(yaxis_frame,u'T\u2082','plot_T2','Off',2)
make_check_button(yaxis_frame,u'T\u209B','plot_Ts','On',3)

#X axis advanced options -initiall a button
make_radio_button(xaxis_advanced,u'\u03B1\u2081','xaxis','alpha1',1)
make_radio_button(xaxis_advanced,u'\u03B1\u2082','xaxis','alpha2',2)
make_radio_button(xaxis_advanced,u'\u03B5\u2081','xaxis','epsilon1',3)
make_radio_button(xaxis_advanced,u'\u03B5\u2082','xaxis','epsilon2',3)
xaxis_advanced.grid_remove()

#functions for button for advanced frame
def reveal_plot():
    
    return xaxis_advanced.grid(), hide_button2.grid(), button2.grid_remove()

def hide_plot():
    
    return xaxis_advanced.grid_remove(), hide_button2.grid_remove(), button2.grid()

hide_button2=ttk.Button(plotframe,text='Hide',command=hide_plot)
hide_button2.grid(row=2,column=1)
hide_button2.grid_remove()
button2=ttk.Button(plotframe,text='Advanced X Axis Options',command=reveal_plot)
button2.grid(row=3, column=0)

# add save button
def save_plot(): #create this function
    pass

button_save=ttk.Button(save_frame,text='Save Plot',command=save_plot)
button_save.grid(row=0, column=0)
root.mainloop()



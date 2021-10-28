from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from slider_experiments import forest_change

from config import * #import variables from config file
import time_slider_range
from save import saving

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import matplotlib.pyplot as plt
from plot import make_plot
from energymodel import solve_over_time, calculate_albedo



#function for making entry for user friendly options
def make_value_entry(root,caption,rowno,default_initial, default_rate, unit):
    label = ttk.Label(root, width = 10, text = caption)
    label.grid(row = rowno, column = 0,sticky=(N, S, E, W))
    entry = ttk.Entry(root, width = 10, textvariable = default_initial)
    entry.grid(row = rowno, column = 1,sticky=(N, S, E, W))
    entry.bind('<KeyRelease>', execute_main)
    label = ttk.Label(root, width =10, text = unit)
    label.grid(row = rowno, column = 2,sticky=(N, S, E, W))
    entry = ttk.Entry(root, width = 10, textvariable = default_rate)
    entry.grid(row = rowno, column = 3,sticky=(N, S, E, W))
    entry.bind('<KeyRelease>', execute_main)
    label = ttk.Label(root, width = 20, text = unit+' per time interval')
    label.grid(row = rowno, column = 4,sticky=(N, S, E, W))

#make simple entry with one label
def make_simple_entry(root,label,variable,rowno,colno):
    new_label=ttk.Label(root,text=label,width=10)
    new_label.grid(row=rowno,column=colno,sticky=(N, S, E, W))
    new_entry=ttk.Entry(root,width=10,textvariable=variable)
    new_entry.grid(row=rowno,column=colno+1,sticky=(N, S, E, W))
    new_entry.bind('<KeyRelease>', execute_main)

# what happens when the entries are changed
def check_initial_total():
    current_tot = forest.get() + ice.get() + water.get()
    if current_tot > 100:
        """
        
        
        
        call a function to display a box saying the values add up to more than 100%
        
        
        
        """
    else:
        desert.set(100-current_tot)
    return

def check_final_total():
    current_tot = forest_final.get() + ice_final.get() + water_final.get()
    if current_tot > 100:
        """
        
        
        
        call a function to display a box saying the values add up to more than 100%
        
        
        
        """
    else:
        desert_final.set(100-current_tot)
    return

def entry_change(event = None, index = 0):
        # add function to deal with errors if the box is empty
        if index == 0:
            try:
                pos = forest.get()
            except TclError:
                pos = 0
        if index == 1:
            try:
                pos = ice.get()
            except TclError:
                pos = 0
        if index == 2:
            try:
                pos = water.get()
            except TclError:
                pos = 0
        if index == 3:
            try:
                pos = desert.get()
            except TclError:
                pos = 0
        if index < 4:
            slider.moveBar(posit = pos/100, idx = index, entry=True)
            check_initial_total()

        if index == 4:
            try:
                pos = forest_final.get()
            except TclError:
                pos = 0
        if index == 5:
            try:
                pos = ice_final.get()
            except TclError:
                pos = 0
        if index == 6:
            try:
                pos = water_final.get()
            except TclError:
                pos = 0
        if index == 7:
            try:
                pos = desert_final.get()
            except TclError:
                pos = 0
        if index > 3:
            slider_final.moveBar(posit = pos/100, idx = index-4, entry=True)
            check_final_total()        
        return

#def forest_change(event):
#        # add function to deal with errors if the box is empty
#        try:
#            f_pos = forest.get()
#        except TclError:
#            f_pos = 0
#        slider.moveBar(posit = f_pos/100, idx = 0, entry=True)
#        check_total()
#        return

#def ice_change(event):
#        # add function to deal with errors if the box is empty
#        try:
#            ice_pos = ice.get()
#        except TclError:
#            ice_pos = 0
#        slider.moveBar(posit = ice_pos/100, idx = 1, entry=True)
#        check_total()
#        return

#def water_change(event):
        # add function to deal with errors if the box is empty
#        try:
#            water_pos = water.get()
#        except TclError:
#            water_pos = 0
#        slider.moveBar(posit = water_pos/100, idx = 2, entry=True)
#        check_total()
#        return

#def desert_change(event):
#        desert_pos = desert_perc.get()
#        slider.moveBar(posit = desert_pos/100, idx = 3, entry=True)
#        return


#slider entries
def make_slider_entry(root,label,variable,rowno,colno, type):
    new_label=ttk.Label(root,text=label,width=10)
    new_label.grid(row=rowno,column=colno,sticky=(N, S, E, W))
    new_entry=ttk.Entry(root,width=10,textvariable=variable)
    new_entry.grid(row=rowno,column=colno+1,sticky=(N, S, E, W))
    new_entry.bind('<KeyRelease>', execute_main, add= '+')

    new_entry.bind('<KeyRelease>', lambda event: entry_change(event, index = type), add= '+')


#    if type == 0:
#        new_entry.bind('<KeyRelease>', forest_change, add= '+')
#    elif type ==1:
#        new_entry.bind('<KeyRelease>', ice_change, add= '+')
#    elif type == 2:
#        new_entry.bind('<KeyRelease>', water_change, add= '+')
#    else:
#        new_entry.bind('<KeyRelease>', desert_change, add= '+')

#function for making a Radiobutton
def make_radio_button(frame,name,variable_in,value_in,rowno,initial_state):
    radio_button=ttk.Radiobutton(frame,text=name,variable=variable_in, value=value_in, command = lambda : execute_main(None))
    radio_button.grid(column=0,row=rowno,sticky=(N, S, E, W))
    if initial_state=='On':
        radio_button.state(['selected'])
    else:
        radio_button.state(['!selected'])
    #radio_button.bind('<Button-1>', execute_main)

#function for making a Checkbutton
def make_check_button(frame,name,variable_in,initial_state,rowno):
    check_button=ttk.Checkbutton(frame,text=name,variable=variable_in,onvalue='On',offvalue='Off', command = lambda : execute_main(None))
    check_button.grid(column=0,row=rowno,sticky=(N, S, E, W))
    check_button.state(['!alternate']) #clear alternate state
    if initial_state=='On':
        check_button.state(['selected'])
    else:
        check_button.state(['!selected'])
    #check_button.bind('<Button-1>', execute_main)

#close plots when GUI is closed
def on_closing():
    plt.close('all')
    root.destroy()


#update variables and make plot when key is pressed
def execute_main(pressed):
    global co2_initial_update
    global co2_rate_update
    global cloud_initial_update
    global cloud_rate_update
    global albedo_initial_update
    global albedo_rate_update
    global epsilon1_initial_update
    global epsilon1_rate_update
    global epsilon2_initial_update
    global epsilon2_rate_update
    global solar_flux_update
    global forest_update
    global ice_update
    global water_update
    global desert_update
    global time_interval_update
    global time_duration_update
    global xaxis_update
    global Ts_update
    global T1_update
    global T2_update
    global forest_final_update
    global ice_final_update
    global water_final_update
    global desert_final_update

    cloud_initial_update = cloud_initial.get()
    cloud_rate_update = cloud_rate.get()
    albedo_initial_update = albedo_initial.get()
    albedo_rate_update = albedo_rate.get()
    epsilon1_initial_update = epsilon1_initial.get()
    epsilon1_rate_update = epsilon1_rate.get()
    epsilon2_initial_update = epsilon2_initial.get()
    epsilon2_rate_update = epsilon2_rate.get()
    solar_flux_update = solar_flux.get()
    forest_update = forest.get()
    ice_update = ice.get()
    water_update = water.get()
    desert_update = desert.get()
    time_interval_update = int(float(time_interval.get()))
    time_duration_update = int(float(time_duration.get()))
    xaxis_update = xaxis.get()
    Ts_update = Ts_switch.get()
    T1_update = T1_switch.get()
    T2_update = T2_switch.get()
    forest_final_update = forest_final.get()
    ice_final_update = ice_final.get()
    water_final_update = water_final.get()
    desert_final_update = desert_final.get()
    
    if forest_update + water_update + ice_update + desert_update > 100:
        messagebox.showwarning("WARNING","Environment fractions add up to more than 100%")
    
    if forest_final_update + water_final_update + ice_final_update + desert_final_update > 100:
        messagebox.showwarning("WARNING","Environment fractions add up to more than 100%")

    show_plot()

#solve equations with updated inputs and embed plot into GUI
def show_plot():
    #NEED to replace these variables with connections to GUI inputs!

    delta_Solar = 0
    calcs_per_timestep = 10
    # water_final_update = water_update
    # ice_final_update = ice_update
    # forest_final_update = forest_update
    # desert_final_update = desert_update
    
    if albedo_initial_update == 0 and albedo_rate_update == 0:
        albedo, albedo_rate = calculate_albedo(water_update, water_final_update, ice_update, ice_final_update, forest_update, forest_final_update, desert_update, desert_final_update, cloud_initial_update, cloud_rate_update, time_interval_update, time_duration_update)
    else: 
        albedo = albedo_initial_update
        albedo_rate = albedo_rate_update
    
    print(xaxis_update)
    solution = solve_over_time(solar_flux_update,albedo,epsilon1_initial_update,epsilon2_initial_update,time_interval_update,time_duration_update,albedo_rate,epsilon1_rate_update,epsilon2_rate_update,delta_Solar,calcs_per_timestep)
    fig = make_plot(solution, Ts_update, T1_update, T2_update, xaxis_update)
    gui_plot = FigureCanvasTkAgg(fig, outputframe)
    gui_plot.get_tk_widget().grid(row = 1, column = 0, sticky=(N, S, E, W))

print(xaxis_update)  

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
#set style
root.tk.call('source','climatepredictor/sun-valley.tcl')
root.tk.call('set_theme','dark')
root.title('Climate Predictor')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#create mainframe
m=29 #number of rows in mainframe
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe.columnconfigure(0, weight=1)
for i in range(m):
    mainframe.rowconfigure(i, weight=1)

#make frame for changing variables - row 0-n of mainframe
n=29 #rowspan of varframe in main frame
varframe=ttk.Frame(mainframe, padding="12 12 12 12")
varframe.grid(column=0, row=0, sticky=(N, S, E, W),rowspan=n)
varframe.columnconfigure(0, weight=1)
varframe.columnconfigure(1, weight=1)
#configure all rows to have same weight
for i in range(n):
    varframe.rowconfigure(i, weight=1)

#make frame for plot options - row 1 of mainframe
r=10 #rowspan of plot frame
outputframe=ttk.Frame(mainframe, padding="12 12 12 12")
outputframe.grid(column=2, row=0, sticky=(N, S, E, W),rowspan=r)
outputframe.columnconfigure(2, weight=1)
outputframe.columnconfigure(3, weight=1)
for i in range(m):
    outputframe.rowconfigure(i, weight=1)

#make frame for plot options - row n+1 to m  mainframe
p=10 #rowspan of plot frame
plotframe=ttk.Frame(mainframe, padding="12 12 12 12")
plotframe.grid(column=2, row=r+1, sticky=(N, S, E, W),rowspan=p)
plotframe.columnconfigure(2, weight=1)
plotframe.columnconfigure(3, weight=1)
for i in range(p):
    plotframe.rowconfigure(i, weight=1)


######################## Customise Variable Frame ################################################################
#default values
#change this to accurate values later
cloud_initial = DoubleVar(root,value = cloud_initial_update)
cloud_rate = DoubleVar(root,value = cloud_rate_update)
albedo_initial = DoubleVar(root,value = albedo_initial_update)
albedo_rate = DoubleVar(root,value = albedo_rate_update)
epsilon1_initial = DoubleVar(root,value = epsilon1_initial_update)
epsilon1_rate = DoubleVar(root,value = epsilon1_rate_update)
epsilon2_initial = DoubleVar(root,value = epsilon2_initial_update)
epsilon2_rate = DoubleVar(root,value = epsilon2_rate_update)
solar_flux = DoubleVar(root,value = solar_flux_update)
time_interval = IntVar(value = time_interval_update)
time_duration = StringVar(value= time_duration_update)

variable_title=ttk.Label(varframe, text='Variable Options',width=30,font='bold')
variable_title.grid(column=0,row=0, sticky=(N, S, E, W))

#create frame for labels - row=1, column=0 in variable frame
#spans the same number of rows as the make_new_entry thing so it lines up
q=2 #rowspan of frame
label_frame=ttk.Frame(varframe,padding="12 12 12 12")
label_frame.grid(row=1,column=0,columnspan=2,rowspan=q,sticky=(N, S, E, W))
label_frame.columnconfigure(0, weight=1)
label_frame.columnconfigure(1, weight=1)
for i in range(q):
    label_frame.rowconfigure(i, weight=1)

def add_labels(root,rowno):
    variable_label=ttk.Label(root, text='Variable',width=5)
    variable_label.grid(column=0,row=rowno, sticky=(N, S, E, W))
    intial_amount_label=ttk.Label(root, text='Initial amount',width=10)
    intial_amount_label.grid(column=1,row=rowno, sticky=(N, S, E, W))
    change_label=ttk.Label(root, text='Change',width=10)
    change_label.grid(column=3,row=rowno, sticky=(N, S, E, W))

#add our cloud cover entry options and title in rows 1, 2 in variable frame
# make_value_entry(root,caption,rowno,default_initial, default_rate, unit):
add_labels(label_frame,0)
make_value_entry(label_frame,'Cloud cover', 1, cloud_initial, cloud_rate, '%')

#functions for button for advanced frame
def reveal():
    
    return button.grid_remove(), advanced_frame.grid(column=0,row=2+q,sticky=(N, S, E, W),rowspan=k,columnspan=2), hide_button.grid(row=1+q,column=1),slider_frame.grid_remove(),slider_frame_final.grid_remove()

def hide():
    
    return button.grid(), advanced_frame.grid_remove(),hide_button.grid_remove(), slider_frame.grid(row=2+q+k,column=0,columnspan=2,rowspan=rowspanf,sticky=(N, S, E, W)), slider_frame_final.grid(column = 0, row = 8+q+k,columnspan=2,rowspan=2,sticky=(N, S, E, W))

#add buttons for advanced options in row 1+q
button=ttk.Button(varframe,text='Advanced Options',command=reveal)
button.grid(row=1+q, column=0)
hide_button=ttk.Button(varframe,text='Hide Advanced Options',command=hide)
hide_button.grid(row=1+q,column=0)
hide_button.grid_remove()

#add advanced frame dropdown in variable frame row 5
k=5 #rowspan
advanced_frame=ttk.Frame(varframe,padding="12 12 12 12")
advanced_frame.grid(column=0,row=2+q,sticky=(N, S, E, W),rowspan=k,columnspan=2)
for i in range(5):
    advanced_frame.columnconfigure(i, weight=1)
for i in range(k):
    advanced_frame.rowconfigure(i, weight=1)

make_value_entry(advanced_frame,'Albedo',1,albedo_initial,albedo_rate,'')
make_value_entry(advanced_frame,u'\u03B5\u2081',2,epsilon1_initial,epsilon1_rate,'')
make_value_entry(advanced_frame,u'\u03B5\u2082',3,epsilon2_initial,epsilon2_rate,'')
solar_label=ttk.Label(advanced_frame,text=u'S\u2080/present day solar flux')
solar_label.grid(column=1,row=5, sticky=(N, S, E, W))
solar_entry=ttk.Entry(advanced_frame,textvariable=solar_flux,width=5)
solar_entry.grid(column=3,row=5, sticky=(N, S, E, W))
solar_entry.bind('<KeyRelease>', execute_main)
advanced_frame.grid_remove()


#add initial land use widget here, row 2+q+k in variable frame
from slider_setup_2 import Slider
rowspanf=8
slider_frame=ttk.Frame(varframe,padding="12 12 12 12")
slider_frame.grid(row=2+q+k,column=0,columnspan=2,rowspan=rowspanf,sticky=(N, S, E, W))
slider_frame.columnconfigure(0, weight=1)
slider_frame.columnconfigure(1, weight=1)
for i in range(rowspanf):
    slider_frame.rowconfigure(i, weight=1)
slider_title=ttk.Label(slider_frame,text='Land Uses - Initial',)
slider_title.grid(row=0,column=0,sticky=(N, S, E, W))
slider_note=ttk.Label(slider_frame,text='Enter values in descending order')
slider_note.grid(row=0,column=1,sticky=(N, S, E, W))
# initial positions on the slider (calculated from initial percentages)
init_positions = [25,50,75]
# create the slider
slider = Slider(slider_frame, width = 400, height = 60, min_val = 0, max_val = 100, init_lis = init_positions, show_value = True)
slider.grid(row=2,column=0,columnspan=2)
# Entry boxes for the different values
# use make_simple_entry(root,label,variable,rowno,colno):
forest = slider.forest_perc
ice = slider.ice_perc
water = slider.water_perc
desert = slider.desert_perc
forest_value = make_slider_entry(slider_frame,'Forest',slider.forest_perc,4,0, type = 0)
ice_value = make_slider_entry(slider_frame,'Ice',slider.ice_perc,5,0, type = 1)
water_value = make_slider_entry(slider_frame,'Water',slider.water_perc,6,0, type = 2)
desert_value = make_slider_entry(slider_frame,'Desert',slider.desert_perc,7,0, type = 3)

#final land use widget here
rowspanf=8
slider_frame_final=ttk.Frame(varframe,padding="12 12 12 12")
slider_frame_final.grid(row=10+q+k,column=0,columnspan=2,rowspan=rowspanf,sticky=(N, S, E, W)) #span just one row as had to put in later
slider_frame_final.columnconfigure(0, weight=1)
slider_frame_final.columnconfigure(1, weight=1)
for i in range(rowspanf):
    slider_frame_final.rowconfigure(i, weight=1)
slider_title_final=ttk.Label(slider_frame_final,text='Land Uses - final')
slider_title_final.grid(row=0,column=0,sticky=(N, S, E, W))
slider_note_final=ttk.Label(slider_frame_final,text='Enter values in descending order')
slider_note_final.grid(row=0,column=1,sticky=(N, S, E, W))
# initial positions on the slider (calculated from initial percentages)
init_positions_final = [25,50,75]
# create the slider
slider_final = Slider(slider_frame_final, width = 400, height = 60, min_val = 0, max_val = 100, init_lis = init_positions_final, show_value = True)
slider_final.grid(row=2,column=0,columnspan=2)
# Entry boxes for the different values
# use make_simple_entry(root,label,variable,rowno,colno):
forest_final = slider_final.forest_perc
ice_final = slider_final.ice_perc
water_final = slider_final.water_perc
desert_final = slider_final.desert_perc
forest_value_final = make_slider_entry(slider_frame_final,'Forest',slider_final.forest_perc,4,0, type = 4)
ice_value_final = make_slider_entry(slider_frame_final,'Ice',slider_final.ice_perc,5,0, type = 5)
water_value_final = make_slider_entry(slider_frame_final,'Water',slider_final.water_perc,6,0, type = 6)
desert_value_final = make_slider_entry(slider_frame_final,'Desert',slider_final.desert_perc,7,0, type = 7)

#add time widget with slider - row 23 in variable frame
slider_frame2 = ttk.Frame(varframe)
slider_frame2.grid(column = 0, row = 26,columnspan=2,rowspan=2,sticky=(N, S, E, W))
slider_frame2.columnconfigure(0,weight=1)
slider_frame2.columnconfigure(1,weight=1)
slider_frame2.rowconfigure(0,weight=1)
slider_frame2.rowconfigure(1,weight=1)
slider_label = ttk.Label(slider_frame2, text='Time:')
slider_label.grid(column=0,row=0,sticky=(N, S, E, W))
label = ttk.Label(slider_frame2, width = 13, text = 'Change Interval:')
label.grid(row = 1, column = 0, sticky=(N, S, E, W))
entry = ttk.Entry(slider_frame2, width = 4, textvariable = time_interval)
entry.grid(row = 1, column = 1, sticky=(N, S, E, W))
entry.bind('<KeyRelease>', execute_main)
label = ttk.Label(slider_frame2, width = 10, text = 'years')
label.grid(row = 1, column = 2, sticky=(N, S, E, W))
label = ttk.Label(slider_frame2, width = 8, text = 'Duration:')
label.grid(row = 1, column = 3, sticky=(N, S, E, W))
value_entry = ttk.Entry(slider_frame2, width = 4, textvariable = time_duration)
value_entry.grid(row = 1, column = 4, sticky=(N, S, E, W))
value_entry.bind('<KeyRelease>', execute_main)
label = ttk.Label(slider_frame2, width = 6, text = 'years')
label.grid(row = 1, column = 5, sticky=(N, S, E, W))

'''slider2 = Scale(slider_frame2, 
                    from_ = 0, 
                    to=100,
                    length = 300, 
                    orient = 'horizontal',
                    command = lambda s:time_duration.set('%0.0f' % float(s)), 
                    variable = time_duration,
                    tickinterval = 25,
                    showvalue = False
                    )
slider2.grid(row=1,column=6,sticky=(N, S, E, W))'''



############################################ Customise plotting frame ###########################################
#title frame
plot_options_label=ttk.Label(plotframe, text='Plot Options',width=30,font='bold')
plot_options_label.grid(column=0,row=0, sticky=(N, S, E, W))


# 4 frames
rowspanf=4
xaxis_frame=ttk.Frame(plotframe,padding="12 12 12 12")
xaxis_frame.grid(row=1,column=0,columnspan=1,sticky=(N, S, E, W),rowspan=4)
xaxis_frame.columnconfigure(0, weight=1)
for i in range(rowspanf):
    xaxis_frame.rowconfigure(i, weight=1)
rowspanf=4    
yaxis_frame=ttk.Frame(plotframe,padding="12 12 12 12")
yaxis_frame.grid(row=1,column=1,sticky=(N, S, E, W),columnspan=1,rowspan=rowspanf)
yaxis_frame.columnconfigure(0, weight=1)
for i in range(rowspanf):
    yaxis_frame.rowconfigure(i, weight=1)

rowspanf=3
xaxis_advanced=ttk.Frame(plotframe,padding="12 12 12 12")
xaxis_advanced.grid(row=1,column=0,sticky=(N, S, E, W),columnspan=1,rowspan=rowspanf)
xaxis_advanced.columnconfigure(0, weight=1)
for i in range(rowspanf):
    xaxis_advanced.rowconfigure(i, weight=1)

# customise x axis frame
xaxis = StringVar()
xaxis_label=ttk.Label(xaxis_frame,text='X Axis')
xaxis_label.grid(column=0,row=0,sticky=(N, S, E, W))
make_radio_button(xaxis_frame,'Time',xaxis,'time',0,'On')
make_radio_button(xaxis_frame,'Cloud cover',xaxis,'cloud cover',1,'Off')
make_radio_button(xaxis_frame,u'CO\u2082',xaxis,'co2',2,'Off')

# customise y axis frame
Ts_switch = StringVar()
T1_switch = StringVar()
T2_switch = StringVar()
yaxis_label=ttk.Label(yaxis_frame,text='Y Axis')
yaxis_label.grid(column=0,row=0,sticky=(N, S, E, W))
make_check_button(yaxis_frame,u'T\u209B',Ts_switch,'On',1)
make_check_button(yaxis_frame,u'T\u2081',T1_switch,'On',2)
make_check_button(yaxis_frame,u'T\u2092',T2_switch,'On',3)

#X axis advanced options -initiall a button

make_radio_button(xaxis_advanced,'Albedo', xaxis,'albedo',0,'Off')
make_radio_button(xaxis_advanced,u'\u03B5\u2081',xaxis,'epsilon1',1,'Off')
make_radio_button(xaxis_advanced,u'\u03B5\u2082',xaxis,'epsilon2',2,'Off')
xaxis_advanced.grid_remove()



######################################## Output Plot Frame ######################################
#ttk.Label(outputframe, text='Output',width=30).grid(column=0,row=0, sticky=(N, S, E, W))
show_plot()

#functions for button for advanced axis frame
def reveal_plot():
    
    return xaxis_advanced.grid(row=1,column=0,sticky=(N, S, E, W),columnspan=1,rowspan=3), hide_button2.grid(row=5,column=0,sticky=(N, S, E, W)), button2.grid_remove(), xaxis_frame.grid_remove()

def hide_plot():
    
    return xaxis_advanced.grid_remove(), hide_button2.grid_remove(), button2.grid(row=5, column=0,sticky=(N, S, E, W)), xaxis_frame.grid(row=1,column=0,columnspan=1,sticky=(N, S, E, W),rowspan=4)

hide_button2=ttk.Button(plotframe,text='Hide Advanced X Axis Options',command=hide_plot)
hide_button2.grid(row=5,column=0,sticky=(N, S, E, W))
hide_button2.grid_remove()
button2=ttk.Button(plotframe,text='Show Advanced X Axis Options',command=reveal_plot)
button2.grid(row=5, column=0,sticky=(N, S, E, W))
button3=ttk.Button(plotframe, text='Plot',command=show_plot)
button3.grid(row=9, column=0,sticky=(N,S,E,W))

# add save button
def save_plot(): #add this!
    pass
button_save=ttk.Button(plotframe,text='Save Plot',command=save_plot)
button_save.grid(row=9, column=1,sticky=(N, S, E, W))

root.after(10, execute_main)
root.mainloop()


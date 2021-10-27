from tkinter import *
from tkinter import ttk

import time_slider_range

#functions for creating entry types

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
    label = ttk.Label(root, width = 10, text = unit+' per yr')
    label.grid(row = rowno, column = 4,sticky=(N, S, E, W))

#make simple entry with one label
def make_simple_entry(root,label,variable,rowno,colno):
    new_label=ttk.Label(root,text=label,width=10)
    new_label.grid(row=rowno,column=colno,sticky=(N, S, E, W))
    new_entry=ttk.Entry(root,width=10,textvariable=variable)
    new_entry.grid(row=rowno,column=colno+1,sticky=(N, S, E, W))
    new_entry.bind('<KeyRelease>', execute_main)

#function for making a Radiobutton
def make_radio_button(frame,name,variable_in,value_in,rowno):
    radio_button=ttk.Radiobutton(frame,text=name,variable=variable_in, value=value_in)
    radio_button.grid(column=0,row=rowno,sticky=(N, S, E, W))
    radio_button.bind('<Button-1>', execute_main)

#function for making a Checkbutton
def make_check_button(frame,name,variable_in,initial_state,rowno):
    check_button=ttk.Checkbutton(frame,text=name,variable=variable_in,onvalue='On',offvalue='Off')
    check_button.grid(column=0,row=rowno,sticky=(N, S, E, W))
    check_button.state(['!alternate']) #clear alternate state
    if initial_state=='On':
        check_button.state(['selected'])
    else:
        check_button.state(['!selected'])

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

    co2_initial_update = co2_initial.get() 
    co2_rate_update = co2_rate.get()
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
    time_interval_update = int(time_interval.get())
    time_duration_update = int(time_duration.get())
    xaxis_update = xaxis.get()



root = Tk()
#set style
root.tk.call('source','climatepredictor/sun-valley.tcl')
root.tk.call('set_theme','dark')
root.title('Climate Predictor')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#create mainframe
m=30 #number of rows in mainframe
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe.columnconfigure(0, weight=1)
for i in range(m):
    mainframe.rowconfigure(i, weight=1)

#make frame for changing variables - row 0 of mainframe
n=17 #rowspan of varframe in main frame
varframe=ttk.Frame(mainframe, padding="12 12 12 12")
varframe.grid(column=0, row=0, sticky=(N, S, E, W),rowspan=n)
varframe.columnconfigure(0, weight=1)
varframe.columnconfigure(1, weight=1)
#configure all rows to have same weight
for i in range(n):
    varframe.rowconfigure(i, weight=1)

#make frame for plot options - row 1 of mainframe
p=14 #rowspan of plot frame
plotframe=ttk.Frame(mainframe, padding="12 12 12 12")
plotframe.grid(column=0, row=19, sticky=(N, S, E, W),rowspan=p)
plotframe.columnconfigure(0, weight=1)
plotframe.columnconfigure(1, weight=1)
for i in range(p):
    varframe.rowconfigure(i, weight=1)

######################## Customise Variable Frame ################################################################
#default values
#change this to accurate values later
co2_initial = DoubleVar(root,value = 278.0)#preindustrial
co2_rate =  DoubleVar(root,value = 0.0)
cloud_initial = DoubleVar(root,value = 10.0)
cloud_rate = DoubleVar(root,value = 0.0)
albedo_initial = DoubleVar(root,value = 0.3)
albedo_rate = DoubleVar(root,value = 0.0)
epsilon1_initial = DoubleVar(root,value = 0.3)
epsilon1_rate = DoubleVar(root,value = 0.0)
epsilon2_initial = DoubleVar(root,value = 0.4)
epsilon2_rate = DoubleVar(root,value = 0.0)
solar_flux = DoubleVar(root,value = 1300.0)
time_interval = IntVar(value = 1)
time_duration = StringVar(value=50)

ttk.Label(varframe, text='Variable Options',width=30).grid(column=0,row=0, sticky=(N, S, E, W))

#create frame for labels - row=1, column=0 in variable frame
#spans the same number of rows as the make_new_entry thing so it lines up
q=4 #rowspan of frame
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

#add our entry options rows 2,3 in variable frame
# make_value_entry(root,caption,rowno,default_initial, default_rate, unit):
add_labels(label_frame,1)
make_value_entry(label_frame,u'CO\u2082 conc.',2, co2_initial, co2_rate, 'ppm')
make_value_entry(label_frame,'Cloud cover', 3, cloud_initial, cloud_rate, '%')

#add advanced frame dropdown in variable frame row 4
k=5 #rowspan
advanced_frame=ttk.Frame(varframe,padding="12 12 12 12")
advanced_frame.grid(column=0,row=6,sticky=(N, S, E, W),rowspan=k,columnspan=2)
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



#functions for button for advanced frame
def reveal():
    
    return advanced_frame.grid(), hide_button.grid()

def hide():
    
    return advanced_frame.grid_remove(),hide_button.grid_remove()


button=ttk.Button(varframe,text='Advanced Options',command=reveal)
button.grid(row=5, column=0)
hide_button=ttk.Button(varframe,text='Hide',command=hide)
hide_button.grid(row=5,column=1)

#add land use widget here, row 6 in variable frame
from slider_setup_2 import Slider
rowspanf=6
slider_frame=ttk.Frame(varframe,padding="12 12 12 12")
slider_frame.grid(row=11,column=0,columnspan=2,rowspan=rowspanf,sticky=(N, S, E, W))
slider_frame.columnconfigure(0, weight=1)
slider_frame.columnconfigure(1, weight=1)
for i in range(rowspanf):
    slider_frame.rowconfigure(i, weight=1)
slider_title=ttk.Label(slider_frame,text='Land Uses')
slider_title.grid(row=0,column=0,sticky=(N, S, E, W))
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
forest_value = make_simple_entry(slider_frame,'Forest',slider.forest_perc,4,0)
ice_value = make_simple_entry(slider_frame,'Ice',slider.ice_perc,5,0)
water_value = make_simple_entry(slider_frame,'Water',slider.water_perc,6,0)
desert_value = make_simple_entry(slider_frame,'Desert',slider.desert_perc,7,0)

#add time widget with slider - row 8 in variable frame
slider_frame2 = ttk.Frame(varframe)
slider_frame2.grid(column = 0, row = 17,columnspan=2,rowspan=2,sticky=(N, S, E, W))
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
plot_options_label=ttk.Label(plotframe, text='Plot Options',width=30)
plot_options_label.grid(column=0,row=0, sticky=(N, S, E, W))


# 4 frames
rowspanf=4
xaxis_frame=ttk.Frame(plotframe,padding="12 12 12 12")
xaxis_frame.grid(row=1,column=0,columnspan=1,sticky=(N, S, E, W),rowspan=rowspanf)
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
xaxis_advanced.grid(row=5,column=0,sticky=(N, S, E, W),columnspan=1,rowspan=rowspanf)
xaxis_advanced.columnconfigure(0, weight=1)
for i in range(rowspanf):
    xaxis_advanced.rowconfigure(i, weight=1)

# customise x axis frame
xaxis = StringVar()
xaxis_label=ttk.Label(xaxis_frame,text='X Axis')
xaxis_label.grid(column=0,row=0,sticky=(N, S, E, W))
make_radio_button(xaxis_frame,'Time',xaxis,'time',1)
make_radio_button(xaxis_frame,'Cloud cover',xaxis,'cloud cover',2)
make_radio_button(xaxis_frame,u'CO\u2082',xaxis,'co2',3)

# customise y axis frame
yaxis_label=ttk.Label(yaxis_frame,text='Y Axis')
yaxis_label.grid(column=0,row=0,sticky=(N, S, E, W))
make_check_button(yaxis_frame,u'T\u2081','plot_T1','Off',1)
make_check_button(yaxis_frame,u'T\u2082','plot_T2','Off',2)
make_check_button(yaxis_frame,u'T\u209B','plot_Ts','On',3)

#X axis advanced options -initiall a button

make_radio_button(xaxis_advanced,'Albedo', xaxis,'albedo',0)
make_radio_button(xaxis_advanced,u'\u03B5\u2081',xaxis,'epsilon1',1)
make_radio_button(xaxis_advanced,u'\u03B5\u2082',xaxis,'epsilon2',2)
xaxis_advanced.grid_remove()

def show_plot():
    from energymodel import solve_over_time
    from plots import plotting
    import matplotlib.pyplot as plt

    albedo = 0.3
    #em1 = 0.5
    #em2 = 0.5
    timestep = 1 #years
    length = 50 #years
    delta_albedo = 0.00
    #delta_em1 = 0.02
    #delta_em2 = 0.02
    delta_Solar = 0
    calcs_per_timestep = 10
    co2 = 1
    delta_co2 = 1
    cc = 20
    delta_cc = 1

    solution = solve_over_time(solar_flux_update,albedo,epsilon1_initial_update,epsilon2_initial_update,timestep,length,delta_albedo,epsilon1_rate_update,epsilon2_rate_update,delta_Solar,calcs_per_timestep)
    plotting(solution, 'On', 'On', 'On',xaxis_update)
    plt.show()


#functions for button for advanced axis frame
def reveal_plot():
    
    return xaxis_advanced.grid(), hide_button2.grid(), button2.grid_remove()

def hide_plot():
    
    return xaxis_advanced.grid_remove(), hide_button2.grid_remove(), button2.grid()

hide_button2=ttk.Button(plotframe,text='Hide',command=hide_plot)
hide_button2.grid(row=8,column=0,sticky=(N, S, E, W))
hide_button2.grid_remove()
button2=ttk.Button(plotframe,text='Advanced X Axis Options',command=reveal_plot)
button2.grid(row=8, column=0,sticky=(N, S, E, W))
button3=ttk.Button(plotframe, text='Plot',command=show_plot)
button3.grid(row=10, column=0,sticky=(N,S,E,W))

# add save button
def save_plot(): #create this function
    pass

button_save=ttk.Button(plotframe,text='Save Plot',command=save_plot)
button_save.grid(row=10, column=1,sticky=(N, S, E, W))
root.mainloop()



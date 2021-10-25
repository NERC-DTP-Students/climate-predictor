#import tkinter as tk
from tkinter import *
from tkinter import ttk

#from energymodel import *

root = Tk()

def albedo_to_cloud(pressed):
    albedo = albedo_value.get()
    cloud_initial_value.set("cloud" + albedo)
    take_inputs()

def cloud_to_albedo(pressed):
    cloud = cloud_initial_value.get()
    albedo_value.set("albedo" + cloud)
    take_inputs()


def take_inputs(pressed=None):
    co2_initial_input = cO2_initial_value.get()
    co2_change_input = cO2_change_value.get()

    Solar = solar_value.get()
    albedo = albedo_value.get()
    #em1 = 
    #em2 = 

    timestep = time_step_value.get()
    length = duration_value.get()

    #delta_albedo = 
    #delta_em1 = 
    #delta_em2 = 
    delta_Solar = 0

    #our_solution = solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar)

# create label
greeting = ttk.Label(text = "Hello, test")
greeting.pack()


# CO2 inputs
cO2_initial_value = StringVar(root, value = "100ppm")
cO2_initial_entry = ttk.Entry(textvariable=cO2_initial_value)
cO2_initial_entry.pack()

cO2_change_value = StringVar(root, value = 10)
cO2_change_entry = ttk.Entry(textvariable=cO2_change_value)
cO2_change_entry.pack()

# clouds input
cloud_initial_value = StringVar(root, value = "70%")
cloud_initial_entry = ttk.Entry(textvariable=cloud_initial_value)
cloud_initial_entry.pack()
cloud_initial_entry.bind('<KeyRelease>', cloud_to_albedo)

cloud_change_value = StringVar(root, value = 10)
cloud_change_entry = ttk.Entry(textvariable=cloud_change_value)
cloud_change_entry.pack()

# time input
time_step_value = StringVar(root, value =  5)
time_step_entry = ttk.Entry(textvariable=time_step_value)
time_step_entry.pack()
time_step_entry.bind('<KeyRelease>', take_inputs)

duration_value = StringVar(root, value =  30)
duration_entry = ttk.Entry(textvariable=duration_value)
duration_entry.pack()
duration_entry.bind('<KeyRelease>', take_inputs)

# Solar input
solar_value = StringVar(root, value =  1000)
solar_entry = ttk.Entry(textvariable=solar_value)
solar_entry.pack()
solar_entry.bind('<KeyRelease>', take_inputs)

# albedo box
albedo_value = StringVar(root, value =  0.5)
albedo_entry = ttk.Entry(textvariable=albedo_value)
albedo_entry.pack()
albedo_entry.bind('<KeyRelease>', albedo_to_cloud)

# event when something is typed
#root.bind('<KeyPress>', take_inputs)



root.mainloop()
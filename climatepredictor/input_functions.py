#import tkinter as tk
from tkinter import *
from tkinter import ttk

from energymodel import calculate_albedo

#Default albedo values
ocean_albedo = 0.06
ice_albedo = 0.65
green_albedo = 0.12
desert_albedo = 0.35
cloud_albedo = 0.5

root = Tk()

# probably don't need now?
def albedo_to_cloud(pressed):
    albedo = albedo_value.get()
    ocean_percent.set("not applicable, aledbo edited")
    ice_percent.set("not applicable, aledbo edited")
    green_percent.set("not applicable, aledbo edited")
    desert_percent.set("not applicable, aledbo edited")
    cloud_percent.set("not applicable, aledbo edited")
    ocean_percent_entry.config(state='disabled')
    ice_percent_entry.config(state='disabled')
    green_percent_entry.config(state='disabled')
    desert_percent_entry.config(state='disabled')
    cloud_percent_entry.config(state='disabled')
    take_inputs()

def update_albedo(pressed):
    ocean = ocean_percent.get()
    ice = ice_percent.get()
    green = green_percent.get()
    desert = desert_percent.get()
    cloud = cloud_percent.get()
    albedo = calculate_albedo(ocean,ice,green,desert,cloud)
    albedo_value.set(albedo)
    take_inputs()

# def calculate_albedo(ocean_perc,ice_perc,green_perc,desert_perc,cloud_perc):
#     ocean = ocean_percent.get()
#     ice = ice_percent.get()
#     green = green_percent.get()
#     desert = desert_percent.get()
#     cloud = cloud_percent.get()
#     earth_albedo = (ocean * ocean_albedo) + (ice * ice_albedo) + (green * green_albedo) + (desert * desert_albedo)
#     total_albedo = (cloud * cloud_albedo) + ((1 - cloud) * earth_albedo)
#     return total_albedo

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
cO2_initial_value = DoubleVar(root, value = "100ppm")
cO2_initial_entry = ttk.Entry(textvariable=cO2_initial_value)
cO2_initial_entry.pack()

cO2_change_value = DoubleVar(root, value = 10)
cO2_change_entry = ttk.Entry(textvariable=cO2_change_value)
cO2_change_entry.pack()

# oceans input
ocean_percent = DoubleVar(root, value = "0.65") #can we make the percentage sign sticky?
ocean_percent_entry = ttk.Entry(textvariable=ocean_percent)
ocean_percent_entry.pack()
ocean_percent_entry.bind('<KeyRelease>', update_albedo)

ocean_change_value = DoubleVar(root, value = 10)
ocean_change_entry = ttk.Entry(textvariable=ocean_change_value)
ocean_change_entry.pack()

# ice input
ice_percent = DoubleVar(root, value = "0.15") #can we make the percentage sign sticky?
ice_percent_entry = ttk.Entry(textvariable=ice_percent)
ice_percent_entry.pack()
ice_percent_entry.bind('<KeyRelease>', update_albedo)

ice_change_value = DoubleVar(root, value = 10)
ice_change_entry = ttk.Entry(textvariable=ice_change_value)
ice_change_entry.pack()

# green input
green_percent = DoubleVar(root, value = "0.15") #can we make the percentage sign sticky?
green_percent_entry = ttk.Entry(textvariable=green_percent)
green_percent_entry.pack()
green_percent_entry.bind('<KeyRelease>', update_albedo)

green_change_value = DoubleVar(root, value = 10)
green_change_entry = ttk.Entry(textvariable=green_change_value)
green_change_entry.pack()

# desert input
desert_percent = DoubleVar(root, value = "0.05") #can we make the percentage sign sticky?
desert_percent_entry = ttk.Entry(textvariable=desert_percent)
desert_percent_entry.pack()
desert_percent_entry.bind('<KeyRelease>', update_albedo)

desert_change_value = DoubleVar(root, value = 10)
desert_change_entry = ttk.Entry(textvariable=desert_change_value)
desert_change_entry.pack()

# clouds input
cloud_percent = DoubleVar(root, value = "0.5") #can we make the percentage sign sticky?
cloud_percent_entry = ttk.Entry(textvariable=cloud_percent)
cloud_percent_entry.pack()
cloud_percent_entry.bind('<KeyRelease>', update_albedo)

cloud_change_value = DoubleVar(root, value = 10)
cloud_change_entry = ttk.Entry(textvariable=cloud_change_value)
cloud_change_entry.pack()


# time input
time_step_value = DoubleVar(root, value =  5)
time_step_entry = ttk.Entry(textvariable=time_step_value)
time_step_entry.pack()
time_step_entry.bind('<KeyRelease>', take_inputs)

duration_value = DoubleVar(root, value =  30)
duration_entry = ttk.Entry(textvariable=duration_value)
duration_entry.pack()
duration_entry.bind('<KeyRelease>', take_inputs)

# Solar input
solar_value = DoubleVar(root, value =  1000)
solar_entry = ttk.Entry(textvariable=solar_value)
solar_entry.pack()
solar_entry.bind('<KeyRelease>', take_inputs)

# albedo box
albedo_value = DoubleVar(root, value = calculate_albedo(ocean_percent,ice_percent,green_percent,desert_percent,cloud_percent))
albedo_entry = ttk.Entry(textvariable=albedo_value)
albedo_entry.pack()
albedo_entry.bind('<KeyRelease>', albedo_to_cloud)

# event when something is typed
#root.bind('<KeyPress>', take_inputs)

root.mainloop()
#import functions required
from energymodel import solve_over_time, calculate_albedo
from plots import plotting
from save import saving

#import variables for solving - need to make sure gui is changed so they don't make the GUI run again
from config import *

calcs_per_timestep = 10 #just define manually for now

# #import variables for plotting
# from gui import as plot_Ts
# from gui import as plot_T1
# from gui import as plot_T2
# from gui import as xaxis


# #calculate albedo and the change in albedo
# albedo = calculate_albedo(ocean_perc,ice_perc,green_perc,desert_perc,cloud_perc)
# cloud_perc_final = cloud_perc + cloud_change*length/timestep
# albedo_final = calculate_albedo(ocean_perc_final,ice_perc_final,green_perc_final,desert_perc_final,cloud_perc_final)
# delta_albedo = (albedo+albedo_final)/(length/timestep)

# #solve to give matrix
# solution = solve_over_time(solar,albedo,em1,em2,timestep,length,delta_albedo,delta_em1,delta_em2,delta_solar,calcs_per_timestep)

# #plot solution
# figure = plotting(solution, plot_Ts, plot_T1, plot_T2, xaxis)

# #save as a png
# saving(figure)



#import functions required
from climatepredictor.energymodel import solve_over_time, calculate_albedo
from climatepredictor.plots import plotting
from climatepredictor.save import saving

# #import variables to calculate albedo
# from climatepredictor.gui import as ocean_perc
# from climatepredictor.gui import as ice_perc
# from climatepredictor.gui import as green_perc
# from climatepredictor.gui import as desert_perc
# from climatepredictor.gui import as cloud_perc
# from climatepredictor.gui import as ocean_perc_final
# from climatepredictor.gui import as ice_perc_final
# from climatepredictor.gui import as green_perc_final
# from climatepredictor.gui import as desert_perc_final
# from climatepredictor.gui import as cloud_change

#import variables for solving - need to make sure gui is changed so they don't make the GUI run again
from climatepredictor.gui import solar_flux as solar
if solar == 0.0: solar = 1368
else: solar *= 1368 #if there is no entry in advanced solar flux field, default to present day earth
# from climatepredictor.gui import as em1
# from climatepredictor.gui import as em2
# from climatepredictor.gui import as timestep
# from climatepredictor.gui import as length
# from climatepredictor.gui import as delta_em1
# from climatepredictor.gui import as delta_em2
# from climatepredictor.gui import as delta_solar

calcs_per_timestep = 10 #just define manually for now

# #import variables for plotting
# from climatepredictor.gui import as plot_Ts
# from climatepredictor.gui import as plot_T1
# from climatepredictor.gui import as plot_T2
# from climatepredictor.gui import as xaxis


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



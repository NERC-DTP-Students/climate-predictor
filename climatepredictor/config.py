"""
Defines variables to be used across the program.

:co2_initial_update: initial CO2 (ppm), currently not used in program
:co2_rate_update: change rate of CO2 (ppm), currently not used in program
:cloud_initial_update: initial percent of global cloud cover (%)
:cloud_rate_update: change rate of global cloud cover (%)
:albedo_initial_update: initial albedo (unitless)
:albedo_rate_update: change rate of albedo (unitless)
:epsilon1_initial_update: inital emissivity of lower atmospheric layer (unitless)
:epsilon1_rate_update: change rate of emissivity of lower atmospheric layer (unitless)
:epsilon2_initial_update: inital emissivity of upper atmospheric layer (unitless)
:epsilon2_rate_update: emissivity of upper atmospheric layer (unitless)
:solar_flux_update: flux from the Sun at the top of Earth's atmosphere (W/m^2)
:forest_update: initial percent of Earth covered by forest (%)
:ice_update: initial percent of Earth covered by ice and snow (%)
:water_update: initial percent of Earth covered by liquid water (%)
:desert_update: initial percent of Earth covered by desert and bare earth (%)
:forest_final_update: final percent of Earth covered by forest (%)
:ice_final_update: final percent of Earth covered by ice and snow (%)
:water_final_update: final percent of Earth covered by liquid water (%)
:desert_final_update: final percent of Earth covered by desert and bare earth (%)
:time_interval_update: time interval over which change rate occurs (years)
:time_duration_update: total time duration of interest (years)
:xaxis_update: default X axis variable on plot, set to 'time'
:Ts_update: On/Off switch for plotting T of surface on plot
:T1_update: On/Off switch for plotting T of lower atmosphere on plot
:T2_update: On/Off switch for plotting T of upper atmosphere on plot

"""
co2_initial_update = 278.0
co2_rate_update = 0.0
cloud_initial_update = 50.0
cloud_rate_update = 0.0
albedo_initial_update = 0.0
albedo_rate_update =  0.0
epsilon1_initial_update = 0.5
epsilon1_rate_update = 0.0
epsilon2_initial_update = 0.5
epsilon2_rate_update = 0.0
solar_flux_update = 1370.0
forest_update = 15.0
ice_update = 15.0
water_update = 65.0
desert_update = 5.0
forest_final_update = 15.0
ice_final_update = 15.0
water_final_update = 65.0
desert_final_update = 5.0
time_interval_update = 1.0
time_duration_update = 50.0
xaxis_update = 'time'
Ts_update='On' 
T1_update='On' 
T2_update='On' 


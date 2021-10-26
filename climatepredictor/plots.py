import numpy as np
import matplotlib.pyplot as plt
from climatepredictor import solve_over_time
import matplotlib.path as mplPath

Solar = 1368 #Wm^2
albedo = 0.3
em1 = 0.5
em2 = 0.5
sigma = 5.67e-8
timestep = 1 #years
length = 50 #years
delta_albedo = 0.00
delta_em1 = 0.02
delta_em2 = 0.02
delta_Solar = 0
calcs_per_timestep = 10
co2 = 1
delta_co2 = 1
cc = 1
delta_cc = 1

solution = solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep)

def plotting(solution, plot_Ts, plot_T1, plot_T2, xaxis):
    plt.figure()

    if xaxis == 'co2':
        inc_co2 = []
        for i in range(len(solution[0,:])):
            inc_co2.append(co2+ (i*delta_co2))

        if plot_Ts == 'On': plt.plot(inc_co2,solution[0,:],label = 'Surface temperature')
        elif plot_T1 == 'On': plt.plot(inc_co2,solution[1,:], label = 'Lower atmospheric temperature')
        elif plot_T2 == 'On': plt.plot(inc_co2,solution[2,:], label = 'Upper atmospheric temperature')
        else: raise ValueError('No y variable selected')
    
    elif xaxis == 'cloud cover':
        inc_cc = []
        for i in range(len(solution[0,:])):
            inc_cc.append(cc + (i*delta_cc))

        if plot_Ts == 'On': plt.plot(inc_cc,solution[0,:],label = 'Surface temperature')
        elif plot_T1 == 'On': plt.plot(inc_cc,solution[1,:], label = 'Lower atmospheric temperature')
        elif plot_T2 == 'On': plt.plot(inc_cc,solution[2,:], label = 'Upper atmospheric temperature')
        else: raise ValueError('No y variable selected')

    elif xaxis == 'time':
        t = []
        for i in range(len(solution[0,:])):
            t.append(i*timestep)
        
        if plot_Ts == 'On': plt.plot(t,solution[0,:],label = 'Surface temperature')
        elif plot_T1 == 'On': plt.plot(t,solution[1,:], label = 'Lower atmospheric temperature')
        elif plot_T2 == 'On': plt.plot(t,solution[2,:], label = 'Upper atmospheric temperature')
        else: raise ValueError('No y variable selected')
    

    plt.suptitle('GLobal average temperature timeseries')
    plt.title(f'Final surface temperature = {round(solution[0,-1],2)}')
    plt.legend()
    if xaxis == 'co2': plt.xlabel('CO2 Concentration (ppm)')
    elif xaxis == 'cloud cover': plt.xlabel('Cloud Cover')
    elif xaxis == 'time': plt.xlabel('Time (years)')
    plt.ylabel('Temerature (K)')
    plt.show()

plotting(solution, 'On', 'On', 'On','time')

if __name__ == '__main__':
    plotting()


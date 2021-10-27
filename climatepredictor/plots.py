import numpy as np
import matplotlib.pyplot as plt
from energymodel import solve_over_time #not required I don't think as we don't want to solve in this file
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
cc = 20
delta_cc = 1

solution = solve_over_time(Solar,albedo,em1,em2,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep)

def plotting(solution, plot_Ts, plot_T1, plot_T2, xaxis):
    fig = plt.figure()

    if xaxis == 'co2':
        inc_co2 = []
        for i in range(len(solution[0,:])):
            inc_co2.append(co2+ (i*delta_co2)/calcs_per_timestep)

        if plot_Ts == 'On': plt.plot(inc_co2,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': plt.plot(inc_co2,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': plt.plot(inc_co2,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    elif xaxis == 'cloud cover':
        inc_cc = []
        for i in range(len(solution[0,:])):
            inc_cc.append(cc + (i*delta_cc)/calcs_per_timestep)

        if plot_Ts == 'On': plt.plot(inc_cc,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': plt.plot(inc_cc,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': plt.plot(inc_cc,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')

    elif xaxis == 'time':
        t = []
        for i in range(len(solution[0,:])):
            t.append(i*timestep/calcs_per_timestep)
        
        if plot_Ts == 'On': plt.plot(t,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': plt.plot(t,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': plt.plot(t,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    elif xaxis == 'albedo':
        inc_alb = []
        for i in range(len(solution[0,:])):
            inc_alb.append(albedo+(i*delta_albedo)/calcs_per_timestep)
        
        if plot_Ts == 'On': plt.plot(inc_alb,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': plt.plot(inc_alb,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': plt.plot(t,solution[inc_alb,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    elif xaxis == 'emissivity':
        inc_em = []
        for i in range(len(solution[0,:])):
            inc_em.append(em1+(i*delta_em1)/calcs_per_timestep)
        
        if plot_Ts == 'On': plt.plot(inc_em,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': plt.plot(inc_em,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': plt.plot(inc_em,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    else: raise ValueError('No x axis selected')
    

    plt.suptitle('GLobal average temperature timeseries')
    plt.title(f'Final surface temperature = {round(solution[0,-1],2)}')
    plt.legend()
    if xaxis == 'co2': plt.xlabel('CO2 Concentration (ppm)')
    elif xaxis == 'cloud cover': plt.xlabel('Cloud Cover (%)')
    elif xaxis == 'time': plt.xlabel('Time (years)')
    elif xaxis == 'albedo': plt.xlabel('Albedo')
    elif xaxis == 'emissivity': plt.xlabel('Emissivity')
    plt.ylabel('Temerature (K)')

    #plt.show()
    return fig

#commenting out so doesn't run when imported
plotting(solution, 'On', 'On', 'On','time')
plt.show()

#don't think this is needed but no harm for now.
if __name__ == '__main__':
    plotting(solution, 'On','On','On','time')


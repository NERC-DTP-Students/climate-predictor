""" Makes plots of the planet surface and two levels of atmosphere depending on an array of parameters. 
    To see the parameters, check out under the function make_plot. 
"""

import numpy as np
import matplotlib.pyplot as plt
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


def make_plot(solution, t, plot_Ts, plot_T1, plot_T2, xaxis, cc, delta_cc, albedo,delta_albedo\
    , em1, delta_em1, em2, delta_em2):
    """
    Define a function that plots the 2 layer energy balance model against time or a rate of change of a relevant parameter.

    :param solution: The solution over time array created by solve_over_time() in energymodel.py
    :param t: The time axis created by solve_over_time in energymodel.py
    :param plot_Ts: A string of either 'On' or 'Off' that records whether plotting surface temperature has been checked.
    :param plot_T1: A string of either 'On' or 'Off' that records whether plotting lower atmosphere temperature has been checked.
    :param plot_T2: A string of either 'On' or 'Off' that records whether plotting upper atmosphere temperature has been checked.
    :param xaxis: A string denoting which xaxis has been selected in the gui.
    :param cc: The initial cloud cover value, used to generate cloud cover xaxis.
    :param delta_cc: The rate of change of cloud cover, used to generate cloud cover xaxis.
    :param albedo: The initial albedo, used to generate albedo axis.
    :param delta_albedo: The rate of change of albedo, used to generate albedo axis.
    :param em1: The initial emissivity of the lower atmosphere, used to generate em1 axis.
    :param delta_em1: The rate of change of emissivity of the lower atmosphere, used to genreate em1 axis.
    :param em2: The initial emissivity of the upper atmosphere, used to generate albedo axis.
    :param delta_em2: THe rate of change of emissivity of the upper atmopshere, used to generate em2 axis.
    """

    plt.close('all')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    if xaxis == 'cloud cover':
        inc_cc = []
        for i in range(len(solution[0,:])):
            inc_cc.append(cc + (i*delta_cc)/calcs_per_timestep)

        if plot_Ts == 'On': ax1.plot(inc_cc,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': ax1.plot(inc_cc,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': ax1.plot(inc_cc,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')

    elif xaxis == 'time':
      
        #for i in range(len(solution[0,:])):
            #t.append(i*(timestep/calcs_per_timestep))
        
        if plot_Ts == 'On': ax1.plot(t,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': ax1.plot(t,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': ax1.plot(t,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    elif xaxis == 'albedo':
        inc_alb = []
        for i in range(len(solution[0,:])):
            inc_alb.append(albedo+(i*delta_albedo)/calcs_per_timestep)
        
        if plot_Ts == 'On': ax1.plot(inc_alb,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': ax1.plot(inc_alb,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': ax1.plot(inc_alb,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    elif xaxis == 'epsilon1':
        inc_em = []
        for i in range(len(solution[0,:])):
            inc_em.append(em1+(i*delta_em1)/calcs_per_timestep)
        
        if plot_Ts == 'On': ax1.plot(inc_em,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': ax1.plot(inc_em,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': ax1.plot(inc_em,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    elif xaxis == 'epsilon2':
        inc_em = []
        for i in range(len(solution[0,:])):
            inc_em.append(em2+(i*delta_em2)/calcs_per_timestep)
        
        if plot_Ts == 'On': ax1.plot(inc_em,solution[0,:],label = 'Surface temperature')
        if plot_T1 == 'On': ax1.plot(inc_em,solution[1,:], label = 'Lower atmospheric temperature')
        if plot_T2 == 'On': ax1.plot(inc_em,solution[2,:], label = 'Upper atmospheric temperature')
        if plot_Ts == 'Off' and plot_T1 == 'Off' and plot_T2 == 'Off': raise ValueError('No y variable selected')
    
    else: raise ValueError('No x axis selected')
    
    fig.suptitle('Global Average Temperature')
    ax1.set_title(f'Final Surface Temperature = {round(solution[0,-1],2)} K')
    ax1.legend()

    if xaxis == 'cloud cover': ax1.set_xlabel('Cloud Cover (%)')
    elif xaxis == 'time': ax1.set_xlabel('Time (years)')
    elif xaxis == 'albedo': ax1.set_xlabel('Albedo')
    elif xaxis == 'epsilon1': ax1.set_xlabel(u'\u03B5\u2081')
    elif xaxis == 'epsilon2': ax1.set_xlabel(u'\u03B5\u2082')
    plt.ylabel('Temerature (K)')
    return fig


import numpy as np
import matplotlib.pyplot as plt
from climatepredictor import energymodel
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

solution = energymodel.solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep)

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

#plotting(solution, 'On', 'On', 'On','On')


#####

#Silly 2d plot

#####


def solar(So, lat):
    value = So*np.cos(lat*np.pi/180)
    if value < 0: return 0
    else: return value

def alb(lat, lon):
    if abs(lat) >= 60: value = 0.8
    elif abs(lat) <60 and abs(lat) > 20: value = 0.15
    else: value = 0.4
    #little squre ocean
    #if lat >= -20 and lat <= 50 and lon >= 50 and lon <= 120: value = 0.06
    #poly = mplPath.Path(indianOcean)
    #if poly.contains_point((lat,lon)) == True: value = 0.06
    return value

def two_d_plot(Solar,albedo,em1,em2,sigma):
    lat = np.arange(-90,90,3)
    lon = np.arange(0,360,3)
    nlat = len(lat)
    nlon = len(lon)

    Ts = np.zeros((nlat, nlon))
    T1 = np.zeros((nlat, nlon))
    T2 = np.zeros((nlat, nlon))

    solution = np.zeros((nlat,nlon))
    
    for i in range(nlat):
        for j in range(nlon):
            Matrix1 = np.array([[-1, em1, (1-em1)*em2],[em1,-2*em1, em1*em2],[(1-em1)*em2,em1*em2, -2*em2]])
            Matrix2 = np.array([[-(solar(Solar,lat[i])/4)*(1-alb(lat[i],lon[j]))],[0],[0]])
            Matrix2 = Matrix2 / sigma

            solv = np.linalg.solve(Matrix1,Matrix2)
            solution[i,j] = np.sqrt(np.sqrt(solv[0]))

    plt.contourf(lon,lat,solution)
    plt.show()

#two_d_plot(Solar,albedo,em1,em2,sigma)


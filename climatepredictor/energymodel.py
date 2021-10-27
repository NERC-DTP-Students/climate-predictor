"""This energy model contains the input variables to calculate the resultant 3 x 50 matrix of
    temperature on the ground surface, lower layer atmosphere, and upper layer atmosphere. 

    Below are descriptions of each variable.
    
    Solar: solar flux at the top of the atmosphere
    albedo: reflectivity, or the proportion of the radiation reflected by a surface. 
    em1: broadband thermal emissivity of the lower atmospheric layer
    em2: broadband thermal emissivity of the upper atmospheric layer
    sigma: Stefan-Boltzmann constant
    tunestep: The incrememntal time unit
    length: the range of years in the model. This model runs up to 50 years. 

    delta_albedo: change of reflectivity
    delta_em1 = change of emissivity of the lower atmospheric layer
    delta_em2 = change of emissivity of the upper atmospheric layer 
    delta_Solar = change of solar flux at the top of the atmosphere
    calcs_per_timestep = interpolates betweeen timestep


    Reference: https://biocycle.atmos.colostate.edu/shiny/2layer/
"""

#import required packages
import numpy as np
import matplotlib.pyplot as plt

#Define default/test parameters; these will likely disappear later.
Solar = 1368 #Wm^2
albedo = 0.3
em1 = 0.5
em2 = 0.5
sigma = 5.67e-8
timestep = 1 #years
length = 50 #years
delta_albedo = 0
delta_em1 = 0.02
delta_em2 = 0.02
delta_Solar = 0
calcs_per_timestep = 10

#Default albedo values
ocean_albedo = 0.06
ice_albedo = 0.65
green_albedo = 0.12
desert_albedo = 0.35
cloud_albedo = 0.5

#default percentage coverages
ocean_perc, ice_perc, green_perc, desert_perc, cloud_perc = 0.65, 0.15, 0.15, 0.05, 0.50

def calculate_albedo(ocean_perc,ice_perc,green_perc,desert_perc,cloud_perc):
    """Function to calculate the albedo from the land coverage percentages, using the albedos defined above.
    
    Inputs
    :param ocean_perc: percentage of earth covered by oceans
    :param ice_perc: percentage of earth covered by ice and snow
    :param green_perc: percentage of earth covered by grasslands, forrests and urban areas
    :param desert_perc: percentage of earth covered by sandy deserts

    Outputs
    :param total_albedo: float number between 0 and 1, showing the earth's effective total albedo
"""
    earth_albedo = (ocean_perc * ocean_albedo) + (ice_perc * ice_albedo) + (green_perc * green_albedo) + (desert_perc * desert_albedo)
    total_albedo = (cloud_perc * cloud_albedo) + ((1 - cloud_perc) * earth_albedo)
    return total_albedo

# print(calculate_albedo(ocean_perc,ice_perc,green_perc,desert_perc,cloud_perc))

def solve_model(Solar,albedo,em1,em2,sigma = 5.67e-8):
    """Function to solve the model at one particular timestep.

    Inputs
    :param Solar: Solar flux in W/m2
    :param albedo: albedo, as calculated from user inputs
    :param em1: emissivity of the first layer
    :param em2: emissivity of the second layer
    :param sigma: Stefan-Boltzmann constant, 5.67e-8
    """
    solution = np.zeros((3,1)) #define solution as an empty matrix
    # define matrices s.t. Matrix1 x (Solution)^4 = Matrix2
    Matrix1 = np.array([[-1, em1, (1-em1)*em2],[em1,-2*em1, em1*em2],[(1-em1)*em2,em1*em2, -2*em2]])
    Matrix2 = np.array([[-(Solar/4)*(1-albedo)],[0],[0]]) / sigma
    solution = np.sqrt(np.sqrt(np.linalg.solve(Matrix1,Matrix2)))

    return solution # 3x1 matrix of [Ts,T1,T2]

def solve_over_time(Solar,albedo,em1,em2,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep,sigma = 5.67e-8):
    """Function to solve the model over many timesteps, to produce a time series of temperatures.

    Inputs:
    :param Solar: Solar flux in W/m2
    :param albedo: albedo, as calculated from user inputs
    :param em1: emissivity of the first layer
    :param em2: emissivity of the second layer
    :param timestep: timestep specified by the user in years
    :param length: length of time to run the model for in years
    :param delta_albedo: change in albedo per timestep
    :param delta_em1: change in em1 per timesetp
    :param delta_em2: change in em2 per timestep
    :param delta_Solar: change in Solar per timestep
    :param calcs_per_timestep: number of calculations to perform per timestep (by interpolation)
    :param sigma: Stefan-Boltzmann constant, 5.67e-8
    
    """
    solutions_over_time = solve_model(Solar,albedo,em1,em2,sigma) #solves model for first time
    for t in range(1,int((length*calcs_per_timestep)/timestep)): #iterates over timesteps to solve at each one
        Solar += delta_Solar/calcs_per_timestep
        #limit albedo, em1, em2 to be between 0 and 1
        if albedo < 1 and albedo > 0: albedo += delta_albedo/calcs_per_timestep
        if em1 < 1 and em1 > 0: em1 += delta_em1/calcs_per_timestep
        if em2 < 1 and em2 > 0: em2 += delta_em2/calcs_per_timestep

        solutions_over_time = np.hstack([solutions_over_time, solve_model(Solar,albedo,em1,em2,sigma)]) #add solution to array

    return solutions_over_time #array, 3xn where n is how the temperatures evolve over time; rows are Ts, T1, T2

#FOr testing, will eventually disappear.
our_solution = solve_over_time(Solar,albedo,em1,em2,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep)

# #Test plots
# plt.figure()
# plt.plot(our_solution[0,:])
# plt.xlabel('Time / years')
# plt.ylabel('Surface temperature / K')
# plt.show()

if __name__ == '__main__':
     solve_model(), solve_over_time()


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


import numpy as np
import matplotlib.pyplot as plt

Solar = 1368 #Wm^2
albedo = 0.3
em1 = 0.5
em2 = 0.5
sigma = 5.67e-8
timestep = 1 #years
length = 50 #years
delta_albedo = -0.03
delta_em1 = 0.02
delta_em2 = 0.02
delta_Solar = 0
calcs_per_timestep = 10

solution = np.zeros((3,1))

def solve_model(Solar,albedo,em1,em2,sigma):
    Matrix1 = np.array([[-1, em1, (1-em1)*em2],[em1,-2*em1, em1*em2],[(1-em1)*em2,em1*em2, -2*em2]])
    Matrix2 = np.array([[-(Solar/4)*(1-albedo)],[0],[0]])
    Matrix2 = Matrix2 / sigma

    solution = np.linalg.solve(Matrix1,Matrix2)
    solution = np.sqrt(np.sqrt(solution))
    return solution #[Ts,T1,T2]

def solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep):
    solutions_over_time = solve_model(Solar,albedo,em1,em2,sigma)
    for t in range(1,int((length*calcs_per_timestep)/timestep)):
        Solar += delta_Solar/calcs_per_timestep
        if albedo < 1 and albedo > 0: albedo += delta_albedo/calcs_per_timestep
        elif albedo > 1: albedo = 1
        elif albedo < 0: albedo = 0
        if em1 < 1 and em1 > 0: em1 += delta_em1/calcs_per_timestep
        if em2 < 1 and em2 > 0: em2 += delta_em2/calcs_per_timestep

        solutions_over_time = np.hstack([solutions_over_time, solve_model(Solar,albedo,em1,em2,sigma)])

    return solutions_over_time

our_solution = solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar,calcs_per_timestep)
#Test plots

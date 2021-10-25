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

def solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar):
    solutions_over_time = solve_model(Solar,albedo,em1,em2,sigma)
    for t in range(1,int((length*calcs_per_timestep)/timestep)):
        Solar += delta_Solar/calcs_per_timestep
        if albedo < 1 and albedo > 0: albedo += delta_albedo/calcs_per_timestep
        print(albedo)
        em1 += delta_em1/calcs_per_timestep
        em2 += delta_em2/calcs_per_timestep

        solutions_over_time = np.hstack([solutions_over_time, solve_model(Solar,albedo,em1,em2,sigma)])

    return solutions_over_time

our_solution = solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar)

#Test plots
plt.figure()
plt.plot(our_solution[0,:])
plt.xlabel('Time years')
plt.ylabel('Temerature K')
plt.show()
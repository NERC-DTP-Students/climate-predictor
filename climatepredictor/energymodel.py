import numpy as np

Solar = 1368 #Wm^2
albedo = 0.3
em1 = 0.5
em2 = 0.5
sigma = 5.67e-8
timestep = 1 #years
length = 50 #years
delta_albedo = 0.01
delta_em1 = 0.02
delta_em2 = 0.02
delta_Solar = 0

solution = np.zeros((3,1))

def solve_model(Solar,albedo,em1,em2,sigma):
    Matrix1 = np.array([[-1, em1, (1-em1)*em2],[em1,-2*em1, em1*em2],[(1-em1)*em2,em1*em2, -2*em2]])
    Matrix2 = np.array([[-(Solar/4)*(1-albedo)],[0],[0]])
    Matrix2 = Matrix2 / sigma

    solution = np.linalg.solve(Matrix1,Matrix2)
    solution = np.sqrt(np.sqrt(solution))
    return solution #[Ts,T1,T2]


our_solution = solve_model(Solar,albedo,em1,em2,sigma)
print(our_solution)

def solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar):
    solutions_over_time = solve_model(Solar,albedo,em1,em2,sigma)
    for t in range(1,length):
        solutions_over_time = np.hstack([solutions_over_time, solve_model(Solar,albedo,em1,em2,sigma)])
        #solutions_over_time[:,t] = solve_model(Solar,albedo,em1,em2,sigma)
        Solar += delta_Solar
        albedo += delta_albedo
        em1 += delta_em1
        em2 += delta_em2

    return solutions_over_time

    

our_solution = solve_over_time(Solar,albedo,em1,em2,sigma,timestep,length,delta_albedo,delta_em1,delta_em2,delta_Solar)
print(our_solution)
print(np.shape(our_solution))

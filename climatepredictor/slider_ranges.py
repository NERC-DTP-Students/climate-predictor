"""Work out the end range for the time slider"""

def max_time(max, initial, change):
    """Works out the maximum time the model can run for each input
    
    inputs:
        max: maximum possible value for the input
        initial: initial value
        change: inputed change in the value /yr

    returns:
        maximum time the model can run for the input
    """
    if change > 0:
        max_t = (max-initial)/change
    elif change < 0:
        max_t = initial/abs(change)
    else:
        change = default
    return max_t

default = 10000 # default max time

albedo = 0.3
albedo_change = 0.01

cloud_cover = 50
cloud_change = 5

max_CO2 = 10000
CO2 = 100
CO2_change = 10

cloud_max = max_time(100, cloud_cover, cloud_change)
CO2_max = max_time(max_CO2, CO2, CO2_change)
albedo_max = max_time(1, albedo, albedo_change)

max_t = min(CO2_max, albedo_max, cloud_max)

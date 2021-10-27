import matplotlib.pyplot as plt

def saving(figure):
    filename = input('Filename: ') #can we make this in the GUI? atm it is just in terminal
    plt.savefig(filename)
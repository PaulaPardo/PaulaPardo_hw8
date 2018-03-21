import numpy as np
import matplotlib.pyplot as plt
import os 

def normal_dist(x,mean,sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*(np.exp(-((x-mean)**2)/(2*(sigma**2))))

def get_fit(filename):
    archivo = np.genfromtxt(filename)
    x = archivo
    promedio = np.mean(x)
    varianza = np.std(x)**2
    print 'El promedio es: ', promedio
    print 'La varianza es: ', varianza
    a = filename.split(".")
    b = a[0]
    plt.hist(x)
    f = normal_dist(x, promedio, np.sqrt(varianza))
    plt.savefig(str(b) + ".png")
    


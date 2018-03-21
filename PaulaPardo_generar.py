import numpy as np
import matplotlib.pyplot as plt

def sample_1(N):
    return np.random.choice([-10,-5,3,9], size = N, p = [0.1, 0.4, 0.2, 0.3])

def sample_2(N):
    return np.random.exponential(scale = 0.5, size = N)


def get_mean(sampling_fun,N,M):
    promedios = []
    # Calcula M promedios asociados a los N valores que puede tomar alguna de las distribuciones de probabilidad anteriores
    for i in range(M):
        promedios.append(np.mean(sampling_fun(N)))
    return promedios


N = [10,100,1000]
M = 10000

# Se crean los archivos de texto con los M promedios para la funcion de sampleo sample_1
for i in N:
    datos = get_mean(sample_1,i,M)
    np.savetxt('sample_1_' + str(i) + '.txt', datos)

# Se crean los archivos de texto con los M promedios para la funcion de sampleo sample_2
for j in N:
    datos2 = get_mean(sample_2,j,M)
    np.savetxt('sample_2_' + str(j) + '.txt', datos2)

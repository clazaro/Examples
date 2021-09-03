import matplotlib.pyplot as plt
import numpy as np

with open("fsi_sdof/fsi_sdof_cfd_results_disp.dat",'r') as file:
    values = np.genfromtxt(file)

with open("fsi_sdof_cfd_results_disp_ref.dat",'r') as file:
    values_ref = np.genfromtxt(file)

plt.plot(values[:,0], values[:,2])
plt.plot(values_ref[:,0], values_ref[:,2])
plt.savefig("force.png")
plt.clf()
plt.plot(values[:,0], values[:,1])
plt.plot(values_ref[:,0], values_ref[:,1])
plt.savefig("disp.png")

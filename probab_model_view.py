import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from lifting import utils

mats = scipy.io.loadmat('data/saved_sessions/prob_model/prob_model_params.mat')
e = mats['e']
mu = mats['mu']
sigma = mats['sigma']

mu = np.reshape(mu, (mu.shape[0], 3, -1))
e = np.reshape(e, (e.shape[0], e.shape[1], 3, -1))

sh = np.shape(e)

for i in range(sh[0]):
    for j in range(sh[1]):
        #pose0 = mu[i, :, :]
        pose0 = e[i, j, :, :]
        utils.plot_pose(pose0)

plt.show()




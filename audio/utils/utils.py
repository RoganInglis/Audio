import numpy as np
from scipy.interpolate import interp1d


def timestretch(data, stretch=1.25):
    x = np.linspace(0, 1, data.shape[0])
    f = interp1d(x, data, axis=0, kind='cubic')

    x_stretched = np.linspace(0, 1, int(data.shape[0] * stretch))
    data_stretched = f(x_stretched)

    # Re-normalise data
    data_stretched /= np.max(np.abs(data_stretched), axis=(0, 1))

    return data_stretched



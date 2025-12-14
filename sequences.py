from scipy.stats import qmc
import numpy as np

def sobol_points(n_samples, scramble=True, seed=None):
    sampler = qmc.Sobol(d=2, scramble=scramble, seed=seed)
    return sampler.random(n_samples)

def estimate_pi_sobol(n_samples, scramble=True, seed=None):
    points = sobol_points(n_samples, scramble, seed)
    inside = points[:, 0] ** 2 + points[:, 1] ** 2 <= 1.0
    return 4.0 * inside.mean()

def estimate_pi_sobol_stream(n_samples, scramble=True, seed=None):
    points = sobol_points(n_samples, scramble, seed)
    count_inside = 0
    estimates = np.empty(n_samples)
    for i in range(n_samples):
        inside = points[i, 0] ** 2 + points[i, 1] ** 2 <= 1.0
        if inside:
            count_inside += 1
        estimates[i] = 4.0 * count_inside / (i + 1)
    return estimates
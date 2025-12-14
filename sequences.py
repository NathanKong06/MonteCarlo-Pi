from scipy.stats import qmc

def sobol_points(n_samples, scramble=True, seed=None):
    sampler = qmc.Sobol(d=2, scramble=scramble, seed=seed)
    return sampler.random(n_samples)

def estimate_pi_sobol(n_samples, scramble=True, seed=None):
    points = sobol_points(n_samples, scramble, seed)
    inside = points[:, 0] ** 2 + points[:, 1] ** 2 <= 1.0
    return 4.0 * inside.mean()
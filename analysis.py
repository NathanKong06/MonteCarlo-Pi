import numpy as np
from estimators import estimate_pi_mc
from sequences import estimate_pi_sobol

def error_vs_samples(sample_sizes, trials=50):
    mc_errors = []
    sobol_errors = []

    for n in sample_sizes:
        mc_vals = [estimate_pi_mc(n) for _ in range(trials)]
        sobol_vals = [estimate_pi_sobol(n, scramble=True) for _ in range(trials)]

        mc_errors.append(abs(np.mean(mc_vals) - np.pi))
        sobol_errors.append(abs(np.mean(sobol_vals) - np.pi))

    return np.array(mc_errors), np.array(sobol_errors)

def variance_scaling(sample_sizes, trials=100):
    stds = []
    for n in sample_sizes:
        estimates = [estimate_pi_mc(n) for _ in range(trials)]
        stds.append(np.std(estimates))
    return np.array(stds)
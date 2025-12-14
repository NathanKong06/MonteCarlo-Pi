import numpy as np
import matplotlib.pyplot as plt

def plot_convergence(mc_estimates, sobol_estimates=None):
    plt.figure()
    plt.plot(mc_estimates, label="Monte Carlo", alpha=0.8)
    plt.plot(sobol_estimates, label="Sobol", alpha=0.8)
    plt.axhline(np.pi, linestyle="--", color="black", label="π")
    plt.xlabel("Samples")
    plt.ylabel("Estimate")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_error(sample_sizes, mc_errors, sobol_errors):
    plt.figure()
    plt.loglog(sample_sizes, mc_errors, label="Monte Carlo")
    plt.loglog(sample_sizes, sobol_errors, label="Sobol")
    plt.xlabel("Samples")
    plt.ylabel("Absolute Error")
    plt.legend()
    plt.grid(True, which="both")
    plt.show()
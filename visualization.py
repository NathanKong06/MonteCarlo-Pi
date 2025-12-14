import numpy as np
import matplotlib.pyplot as plt

def plot_convergence(estimates):
    plt.figure()
    plt.plot(estimates, label="Estimate")
    plt.axhline(np.pi, linestyle="--", color="black", label="π")
    plt.xlabel("Samples")
    plt.ylabel("Estimate")
    plt.legend()
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
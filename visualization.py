import numpy as np
import matplotlib.pyplot as plt

def plot_convergence(mc_estimates, sobol_estimates):
    _, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
    ax1.set_title("Convergence of π Estimates")

    ax1.plot(mc_estimates, label="Monte Carlo", alpha=0.8)
    ax1.plot(sobol_estimates, label="Sobol", alpha=0.8)

    ax1.axhline(np.pi, linestyle="--", color="black", label="π")
    ax1.set_ylabel("Estimate")
    ax1.legend()
    ax1.grid(True)

    ax2.plot(mc_estimates - np.pi, label="Monte Carlo", alpha=0.8)
    ax2.plot(sobol_estimates - np.pi, label="Sobol", alpha=0.8)

    ax2.axhline(0.0, linestyle="--", color="black")
    ax2.set_xlabel("Samples")
    ax2.set_ylabel("Estimate - π")
    ax2.legend()
    ax2.grid(True)
    ax2.set_title("Deviation from π Over Time")

    plt.tight_layout()
    plt.show()

def plot_error(sample_sizes, mc_errors, sobol_errors, stratified_errors):
    plt.figure()
    plt.loglog(sample_sizes, mc_errors, label="Monte Carlo")
    plt.loglog(sample_sizes, sobol_errors, label="Sobol")
    plt.loglog(sample_sizes, stratified_errors, label="Stratified")
    plt.xlabel("Samples")
    plt.ylabel("Absolute Error")
    plt.legend()
    plt.grid(True, which="both")
    plt.show()
import numpy as np
from estimators import estimate_pi_mc, estimate_pi_stream
from sequences import estimate_pi_sobol, estimate_pi_sobol_stream
from analysis import error_vs_samples
from visualization import plot_convergence, plot_error

sobol_samples = 2**17
monte_caro_samples = 1_000_000

def run_single_estimates():
    print("Single Estimate Comparison")
    pi_mc = estimate_pi_mc(monte_caro_samples)
    pi_sobol = estimate_pi_sobol(sobol_samples)

    print(f"Monte Carlo ({monte_caro_samples:,} samples): {pi_mc}")
    print(f"Sobol ({sobol_samples:,} samples): {pi_sobol}")
    print(f"True π: {np.pi}")

def run_convergence_demo():
    print("Convergence Graphs")
    mc_estimates = estimate_pi_stream(2**16)
    sobol_estimates = estimate_pi_sobol_stream(2**16)
    plot_convergence(mc_estimates, sobol_estimates)

def run_error_comparison():
    print("Error Comparison")
    sample_sizes = 2 ** np.arange(5, 15)
    mc_err, sobol_err = error_vs_samples(sample_sizes)

    plot_error(sample_sizes, mc_err, sobol_err)

def main():
    run_single_estimates()
    run_convergence_demo()
    run_error_comparison()

if __name__ == "__main__":
    main()

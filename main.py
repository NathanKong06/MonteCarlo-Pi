import numpy as np
from estimators import estimate_pi_mc, estimate_pi_stream, estimate_pi_stratified_stream
from sequences import estimate_pi_sobol, estimate_pi_sobol_stream
from analysis import error_vs_samples, multi_run_statistics
from visualization import plot_convergence, plot_error

sobol_samples = 2**17
monte_caro_samples = 1_000_000
n_strata = 256

def run_single_estimates():
    print("Single Estimate Comparison\n")
    pi_mc = estimate_pi_mc(monte_caro_samples)
    pi_sobol = estimate_pi_sobol(sobol_samples)
    pi_strat = estimate_pi_stratified_stream(n_strata)[-1]

    print(f"Monte Carlo ({monte_caro_samples:,} samples): {pi_mc}")
    print(f"Sobol ({sobol_samples:,} samples): {pi_sobol}")
    print(f"Stratified ({n_strata**2:,} samples): {pi_strat}")
    print(f"True π: {np.pi}")

def run_multi_run_statistics(n_samples=256*256, runs=50):
    print("\nMulti-Run Statistics\n")
    stats = multi_run_statistics(n_samples, runs)
    for method, data in stats.items():
        print(f"{method:12s} | mean={data['mean']:.6f} "
              f"| std={data['std']:.6e} | rmse={data['rmse']:.6e}")

def run_convergence_demo():
    mc_estimates = estimate_pi_stream(2**16)
    sobol_estimates = estimate_pi_sobol_stream(2**16)
    plot_convergence(mc_estimates, sobol_estimates)

def run_error_comparison():
    sample_sizes = (2 ** np.arange(4, 9)) ** 2
    mc_err, sobol_err, strat_err = error_vs_samples(sample_sizes)
    plot_error(sample_sizes, mc_err, sobol_err, strat_err)

def main():
    run_single_estimates()
    run_multi_run_statistics()
    run_convergence_demo()
    run_error_comparison()

if __name__ == "__main__":
    main()

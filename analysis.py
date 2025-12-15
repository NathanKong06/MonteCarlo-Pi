import numpy as np
from estimators import estimate_pi_mc, estimate_pi_stratified_stream
from sequences import estimate_pi_sobol

def error_vs_samples(sample_sizes, trials=100):
    mc_errors = []
    sobol_errors = []
    stratified_errors = []

    for n in sample_sizes:
        mc_vals = [estimate_pi_mc(n) for _ in range(trials)]
        mc_errors.append(abs(np.mean(mc_vals) - np.pi))

        sobol_vals = [estimate_pi_sobol(n, scramble=True) for _ in range(trials)]
        sobol_errors.append(abs(np.mean(sobol_vals) - np.pi))

        n_strata = int(np.sqrt(n))
        if n_strata * n_strata != n:
            raise ValueError("Stratified sampling requires sample sizes that are perfect squares")

        strat_vals = []
        for _ in range(trials):
            stream = estimate_pi_stratified_stream(n_strata)
            strat_vals.append(stream[-1])

        stratified_errors.append(abs(np.mean(strat_vals) - np.pi))

    return (
        np.array(mc_errors),
        np.array(sobol_errors),
        np.array(stratified_errors),
    )

def multi_run_statistics(n_samples, runs=100):
    results = {}

    mc_vals = np.array([estimate_pi_mc(n_samples) for _ in range(runs)])
    results["Monte Carlo"] = {
        "mean": mc_vals.mean(),
        "std": mc_vals.std(),
        "rmse": np.sqrt(np.mean((mc_vals - np.pi) ** 2)),
    }

    sobol_vals = np.array([
        estimate_pi_sobol(n_samples, scramble=True) for _ in range(runs)
    ])
    results["Sobol"] = {
        "mean": sobol_vals.mean(),
        "std": sobol_vals.std(),
        "rmse": np.sqrt(np.mean((sobol_vals - np.pi) ** 2)),
    }

    n_strata = int(np.sqrt(n_samples))
    if n_strata * n_strata != n_samples:
        raise ValueError("Stratified sampling requires n_samples to be a perfect square")

    strat_vals = []
    for _ in range(runs):
        stream = estimate_pi_stratified_stream(n_strata)
        strat_vals.append(stream[-1])

    strat_vals = np.array(strat_vals)
    results["Stratified"] = {
        "mean": strat_vals.mean(),
        "std": strat_vals.std(),
        "rmse": np.sqrt(np.mean((strat_vals - np.pi) ** 2)),
    }

    return results

def variance_scaling(sample_sizes, trials=100):
    stds = []
    for n in sample_sizes:
        estimates = [estimate_pi_mc(n) for _ in range(trials)]
        stds.append(np.std(estimates))
    return np.array(stds)
import numpy as np

def estimate_pi_mc(n_samples, rng=None):
    if rng is None:
        rng = np.random.default_rng()

    x = rng.random(n_samples)
    y = rng.random(n_samples)
    inside = x * x + y * y <= 1.0
    return 4.0 * inside.mean()

def estimate_pi_stream(n_samples, rng=None):
    if rng is None:
        rng = np.random.default_rng()

    count_inside = 0
    estimates = np.empty(n_samples)
    for i in range(n_samples):
        x, y = rng.random(), rng.random()
        if x * x + y * y <= 1.0:
            count_inside += 1
        estimates[i] = 4.0 * count_inside / (i + 1)

    return estimates
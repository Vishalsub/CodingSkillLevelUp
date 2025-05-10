# Annotated Adaptive Monte Carlo Localization (AMCL) Demo (Simplified 2D)
# Simulates a robot localizing using adaptive particles and fake LiDAR

import numpy as np
import matplotlib.pyplot as plt

# --- Settings ---
MAP_SIZE = (100, 100)
MAX_PARTICLES = 500
MIN_PARTICLES = 100
Neff_threshold = 0.5  # threshold for effective sample size

# Initial state
true_pose = np.array([20, 50, 0.0])
particles = np.random.uniform([0, 0, -np.pi], [MAP_SIZE[0], MAP_SIZE[1], np.pi], (MIN_PARTICLES, 3))

# --- Motion Model: Simulates noisy motion update ---
def sample_motion_model(pose, control):
    dx, dy, dtheta = control
    noise = np.random.normal(0, 0.5, 3)  # Add Gaussian noise
    new_pose = pose + np.array([dx, dy, dtheta]) + noise
    new_pose[2] = np.arctan2(np.sin(new_pose[2]), np.cos(new_pose[2]))  # Normalize angle
    return new_pose

# --- Sensor Model: Returns a fake LiDAR reading from x to right wall ---
def fake_lidar(pose):
    return 100 - pose[0] + np.random.normal(0, 1.0)

def predict_sensor(pose):
    return 100 - pose[0]

def compute_likelihood(observed, expected):
    error = observed - expected
    return np.exp(-0.5 * (error**2) / 4.0)

# --- Resampling ---
def effective_sample_size(weights):
    return 1.0 / np.sum(weights ** 2)

def low_variance_sampler(particles, weights):
    n = len(particles)
    positions = (np.arange(n) + np.random.uniform(0, 1)) / n
    indexes = np.zeros(n, 'i')
    cumsum = np.cumsum(weights)
    i, j = 0, 0
    while i < n:
        if positions[i] < cumsum[j]:
            indexes[i] = j
            i += 1
        else:
            j += 1
    return particles[indexes]

# --- Main Loop ---
for step in range(6):
    # --- Step 1: Simulate Robot Motion ---
    control = [5, 0, 0]  # move right
    true_pose += np.array(control)

    # --- Step 2: Motion Update ---
    particles = np.array([sample_motion_model(p, control) for p in particles])

    # --- Step 3: Sensor Update ---
    z = fake_lidar(true_pose)  # Real sensor reading
    weights = np.array([compute_likelihood(z, predict_sensor(p)) for p in particles])
    weights += 1e-300  # avoid zeros
    weights /= np.sum(weights)

    # --- Step 4: Check Effective Sample Size ---
    Neff = effective_sample_size(weights)
    if Neff < Neff_threshold * len(particles):
        particles = low_variance_sampler(particles, weights)

    # --- Step 5: Adapt Number of Particles ---
    if Neff < 0.3 * len(particles) and len(particles) < MAX_PARTICLES:
        # Add more particles
        extra = np.random.uniform([0, 0, -np.pi], [MAP_SIZE[0], MAP_SIZE[1], np.pi], (50, 3))
        particles = np.vstack((particles, extra))
    elif Neff > 0.9 * len(particles) and len(particles) > MIN_PARTICLES:
        # Reduce particles
        particles = particles[:int(0.9 * len(particles))]

    # --- Step 6: Estimate Pose ---
    # Ensure weights and particles are consistent
    if len(weights) != len(particles):
        weights = np.ones(len(particles)) / len(particles)

    estimated_pose = np.average(particles, axis=0, weights=weights)


    # --- Visualization ---
    plt.figure(figsize=(6, 6))
    plt.xlim(0, MAP_SIZE[0])
    plt.ylim(0, MAP_SIZE[1])
    plt.plot(true_pose[0], true_pose[1], 'ro', label='True Pose')
    plt.plot(particles[:, 0], particles[:, 1], 'b.', alpha=0.3, label='Particles')
    plt.plot(estimated_pose[0], estimated_pose[1], 'go', label='Estimated Pose')
    plt.title(f"AMCL Step {step}")
    plt.legend()
    plt.grid(True)
    plt.show()

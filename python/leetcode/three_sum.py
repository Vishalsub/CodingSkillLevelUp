# # ICP Point-to-Point with SVD: Working Example
# # Aligns two 3D point clouds using numpy

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# def generate_point_cloud(n=30):
#     return np.random.uniform(0, 10, size=(n, 3))

# def apply_transform(points, R, t):
#     return (R @ points.T).T + t

# def icp_svd(source, target):
#     # 1. Compute centroids
#     centroid_src = np.mean(source, axis=0)
#     centroid_tgt = np.mean(target, axis=0)

#     # 2. Center the point clouds
#     src_centered = source - centroid_src
#     tgt_centered = target - centroid_tgt

#     # 3. Cross-covariance matrix
#     H = src_centered.T @ tgt_centered

#     # 4. SVD
#     U, S, Vt = np.linalg.svd(H)
#     R = Vt.T @ U.T

#     # 5. Reflection check
#     if np.linalg.det(R) < 0:
#         Vt[2, :] *= -1
#         R = Vt.T @ U.T

#     # 6. Translation
#     t = centroid_tgt - R @ centroid_src
#     return R, t

# # Create random point cloud A
# A = generate_point_cloud(50)

# # Apply a known transform to A to create B
# true_R = np.array([[0.866, -0.5, 0], [0.5, 0.866, 0], [0, 0, 1]])  # Rotation around Z
# true_t = np.array([2, 1, 0])  # Translation
# B = apply_transform(A, true_R, true_t)

# # Estimate R and t using ICP
# est_R, est_t = icp_svd(A, B)
# A_aligned = apply_transform(A, est_R, est_t)

# # Plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(*A.T, color='blue', label='Original A')
# ax.scatter(*B.T, color='red', label='Target B')
# ax.scatter(*A_aligned.T, color='green', label='Aligned A')
# ax.set_title("ICP via SVD")
# ax.legend()
# plt.show()

# # Print transform
# print("Estimated Rotation:\n", est_R)
# print("Estimated Translation:\n", est_t)

# 2D ICP Example – Simulating LiDAR-like scan matching using SVD
# Author: ChatGPT

# 2D ICP Animation – Frame-by-frame LiDAR-style registration (with drift simulation)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simulate circular lidar scan with noise
def generate_lidar_scan(num_points=60, radius=5.0):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = radius * np.cos(angles) + np.random.normal(0, 0.05, size=num_points)
    y = radius * np.sin(angles) + np.random.normal(0, 0.05, size=num_points)
    return np.stack((x, y), axis=1)

def apply_transform_2d(points, R, t):
    return (R @ points.T).T + t

def icp_2d_svd(P, Q):
    mu_P = np.mean(P, axis=0)
    mu_Q = np.mean(Q, axis=0)
    P_centered = P - mu_P
    Q_centered = Q - mu_Q
    H = P_centered.T @ Q_centered
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[1, :] *= -1
        R = Vt.T @ U.T
    t = mu_Q - R @ mu_P
    return R, t

# Initialization
num_frames = 20
initial_scan = generate_lidar_scan()
accumulated_scan = initial_scan.copy()
poses = [(np.eye(2), np.zeros(2))]  # Store (R, t)

# Simulate odometry drift: each frame is a slightly rotated + translated scan
theta_drift = np.radians(5)
t_drift = np.array([0.2, 0.1])
R_drift = np.array([[np.cos(theta_drift), -np.sin(theta_drift)],
                    [np.sin(theta_drift),  np.cos(theta_drift)]])

scans = [initial_scan]
for i in range(1, num_frames):
    prev_scan = scans[-1]
    new_scan = apply_transform_2d(prev_scan, R_drift, t_drift)
    scans.append(new_scan)

# Set up the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-5, 20)
ax.set_ylim(-5, 20)
ax.set_title("ICP Scan Alignment Animation")
ax.set_aspect('equal')
scan_A = ax.plot([], [], 'bo', label='Previous Scan')[0]
scan_B = ax.plot([], [], 'ro', label='New Scan')[0]
scan_aligned = ax.plot([], [], 'gx', label='Aligned')[0]
ax.legend()

# Animation function
def update(frame):
    global accumulated_scan
    A = accumulated_scan
    B = scans[frame]
    R, t = icp_2d_svd(A, B)
    aligned = apply_transform_2d(B, R.T, -R.T @ t)  # Invert estimated transform

    scan_A.set_data(A[:, 0], A[:, 1])
    scan_B.set_data(B[:, 0], B[:, 1])
    scan_aligned.set_data(aligned[:, 0], aligned[:, 1])

    # Accumulate new aligned scan into A
    accumulated_scan = aligned
    return scan_A, scan_B, scan_aligned

ani = FuncAnimation(fig, update, frames=num_frames, interval=800, repeat=False)
plt.show()



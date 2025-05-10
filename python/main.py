# Solve ICP Problems 1–3 using synthetic 2D scans and SVD-based ICP
import numpy as np
import matplotlib.pyplot as plt

# --- ICP Core (same as before) ---
def icp_2d(P, Q):
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

def transform(points, R, t):
    return (R @ points.T).T + t

# --- Problem 1: ICP Convergence ---
def problem_1():
    print("Problem 1: ICP Convergence Test")
    np.random.seed(42)
    A = np.random.rand(50, 2) * 10
    theta = np.radians(30)
    R_true = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    t_true = np.array([2, 1])
    B = transform(A, R_true, t_true)

    R_est, t_est = icp_2d(A, B)
    A_aligned = transform(A, R_est, t_est)

    plt.figure()
    plt.title("Problem 1: ICP Convergence")
    plt.scatter(*A.T, label="Original A", alpha=0.5)
    plt.scatter(*B.T, label="Transformed B", alpha=0.5)
    plt.scatter(*A_aligned.T, label="Aligned A", marker='x')
    plt.axis('equal'); plt.legend(); plt.grid(True)
    print("Estimated R:\n", R_est)
    print("Estimated t:\n", t_est)
    plt.show()

# --- Problem 2: Cumulative Drift ---
def problem_2():
    print("Problem 2: ICP with Cumulative Drift")
    scans = []
    poses = [np.eye(2)]
    t = np.array([0.5, 0.2])
    R = np.array([[np.cos(0.05), -np.sin(0.05)], [np.sin(0.05), np.cos(0.05)]])
    scan = np.random.rand(100, 2) * 5
    scans.append(scan)
    path = [np.array([0, 0])]

    for i in range(1, 10):
        scan = transform(scan, R, t)
        scans.append(scan)

    current_pose = np.eye(2)
    current_pos = np.array([0, 0])

    for i in range(1, len(scans)):
        R_est, t_est = icp_2d(scans[i-1], scans[i])
        current_pose = R_est @ current_pose
        current_pos += current_pose @ t_est
        path.append(current_pos.copy())

    path = np.array(path)
    plt.figure()
    plt.title("Problem 2: Estimated Robot Path via ICP")
    plt.plot(path[:, 0], path[:, 1], marker='o')
    plt.axis('equal'); plt.grid(True)
    plt.xlabel("X"); plt.ylabel("Y")
    plt.show()

# --- Problem 3: Noise & Filtering ---
def problem_3():
    print("Problem 3: ICP with Noise + Filtering")
    A = np.random.rand(60, 2) * 10
    theta = np.radians(25)
    R_true = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    t_true = np.array([1.5, -1])
    B = transform(A, R_true, t_true)
    B += np.random.normal(0, 0.3, B.shape)  # Gaussian noise

    # Optional filtering (naive: reject outliers based on distance to centroid)
    centroid_B = np.mean(B, axis=0)
    dists = np.linalg.norm(B - centroid_B, axis=1)
    B_filtered = B[dists < np.percentile(dists, 90)]

    A_trimmed = A[:len(B_filtered)]
    R_est, t_est = icp_2d(A_trimmed, B_filtered)
    A_aligned = transform(A_trimmed, R_est, t_est)

    plt.figure()
    plt.title("Problem 3: Noise & Filtering")
    plt.scatter(*A_trimmed.T, label="Original A")
    plt.scatter(*B.T, label="Noisy B", alpha=0.4)
    plt.scatter(*B_filtered.T, label="Filtered B", marker='^')
    plt.scatter(*A_aligned.T, label="Aligned A", marker='x')
    plt.axis('equal'); plt.legend(); plt.grid(True)
    print("Estimated R:\n", R_est)
    print("Estimated t:\n", t_est)
    plt.show()

# --- Run all problems ---
problem_1()
problem_2()
problem_3()

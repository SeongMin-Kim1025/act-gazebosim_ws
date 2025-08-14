import h5py
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def plot_qpos_from_hdf5(filename):
    with h5py.File(filename, 'r') as f:
        qpos = f['observations/qpos'][:]  # (T, 8)

    timesteps = np.arange(qpos.shape[0])

    # Plot all 8 joints (7 arm + 1 gripper)
    fig, axes = plt.subplots(8, 1, figsize=(10, 16), sharex=True)

    for i in range(8):
        ax = axes[i]
        ax.scatter(timesteps, qpos[:, i], label=f'qpos[{i}]', color='tab:blue', s=10)
        ax.set_ylabel(f'Joint {i+1}')
        ax.grid(True)
        ax.legend(loc='upper right')

    axes[-1].set_xlabel("Timestep")
    fig.suptitle("Joint Positions from HDF5 qpos", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.97])

    save_path = os.path.join(os.path.dirname(filename), "qpos_plot.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved plot to: {save_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plot_qpos_from_hdf5.py <filename.hdf5>")
        sys.exit(1)

    plot_qpos_from_hdf5(sys.argv[1])

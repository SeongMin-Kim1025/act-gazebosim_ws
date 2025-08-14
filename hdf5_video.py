import h5py
import cv2
import numpy as np
import sys
import os

def main(filename):
    print(f"Opening HDF5 file: {filename}")

    with h5py.File(filename, "r") as f:
        images = f["observations/images/hand_cam"][:]  # shape: (T, H, W, 3)
        num_frames = len(images)
        height, width = images.shape[1:3]

    # 총 길이 9초로 고정 -> fps 계산
    duration_sec = 9.0
    fps = num_frames / duration_sec
    print(f"Loaded {num_frames} images -> fps: {fps:.2f}")

    # 비디오 저장 설정
    output_path = os.path.splitext(filename)[0] + "_handcam_8s.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for img in images:
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        out.write(img_bgr)

    out.release()
    print(f"Video saved to {output_path} with duration {duration_sec} seconds")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hdf5_handcam_viewer.py <episode_0.hdf5>")
        sys.exit(1)

    main(sys.argv[1])

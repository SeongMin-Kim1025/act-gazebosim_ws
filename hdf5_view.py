import h5py
import sys

def print_hdf5_structure(name, obj, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    print(f"{prefix}{connector}{name}/" if isinstance(obj, h5py.Group) else f"{prefix}{connector}{name}: {obj.shape}, {obj.dtype}")

    if isinstance(obj, h5py.Group):
        items = list(obj.items())
        for idx, (key, item) in enumerate(items):
            is_child_last = (idx == len(items) - 1)
            child_prefix = prefix + ("    " if is_last else "│   ")
            print_hdf5_structure(key, item, child_prefix, is_child_last)

def print_dataset_details(dataset):
    print(f"\nDataset Details:")
    print(f"- Shape: {dataset.shape}")
    print(f"- Data type: {dataset.dtype}")
    print(f"- Sample data (first entries):\n{dataset[:1]}")

def print_group_contents(group):
    print(f"\nGroup Contents:")
    for key in group:
        item = group[key]
        if isinstance(item, h5py.Dataset):
            print(f"- {key}: Dataset, shape={item.shape}, dtype={item.dtype}")
        elif isinstance(item, h5py.Group):
            print(f"- {key}/: Group")
        else:
            print(f"- {key}: Unknown type {type(item)}")

def analyze_hdf5(file_path, target_path=None):
    with h5py.File(file_path, 'r') as hdf_file:
        print(f"Analyzing HDF5 file: {file_path}\n")
        if target_path is None:
            print("/")
            items = list(hdf_file.items())
            for idx, (key, item) in enumerate(items):
                is_last = (idx == len(items) - 1)
                print_hdf5_structure(key, item, "", is_last)
        else:
            if target_path not in hdf_file:
                print(f"Path '{target_path}' not found in the file.")
                return
            obj = hdf_file[target_path]
            print(f"\nExploring '{target_path}':")
            if isinstance(obj, h5py.Group):
                print_group_contents(obj)
            elif isinstance(obj, h5py.Dataset):
                print_dataset_details(obj)
            else:
                print(f"Unknown type: {type(obj)}")

# 실행
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hdf5_view.py <file_path> [target_path]")
        sys.exit(1)

    file_path = sys.argv[1]
    target_path = sys.argv[2] if len(sys.argv) > 2 else None

    analyze_hdf5(file_path, target_path)

import sys
import torch

# Mapping GPU model to number of CUDA cores per multiprocessor
cuda_cores_per_sm_map = {
    "H100": 128,
    "A100": 64,
    "A40": 64,
    "Tesla V100": 64,
    "Tesla P100": 64,
    "Tesla T4": 64,
    "Tesla K80": 192,
    "RTX A6000": 128,
    "RTX 6000": 72,
    "RTX 8000": 72,
    "RTX 30": 128,
    "RTX 40": 128,
    # Add more models as needed
}

# Function to find the number of CUDA cores on SM
def find_cuda_cores_per_sm(gpu_name):
    for key in cuda_cores_per_sm_map:
        if key in gpu_name:
            return cuda_cores_per_sm_map[key]
    return None

print("████████████████████████████████████████████████████")
print("█─▄▄▄─█▄─██─▄█▄─▄▄▀██▀▄─████─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█")
print("█─███▀██─██─███─██─██─▀─██████─████─▄█▀█▄▄▄▄─███─███")
print("▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀")
print()
print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print("Torch version: " + torch.__version__)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
print("___________________________________________________\n")
print("Number of available GPUs:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    prop = torch.cuda.get_device_properties(i)
    print(f"GPU {i+1}: {prop.name}")
    print(f"        Total memory: {prop.total_memory / 1e9:.2f} GB")
    print(f"        MultiProcessor Count: {prop.multi_processor_count}")
    cuda_cores_per_sm = find_cuda_cores_per_sm(prop.name)
    if cuda_cores_per_sm is not None:
        total_cuda_cores = prop.multi_processor_count * cuda_cores_per_sm
        print(f"        Total CUDA Cores: {total_cuda_cores}")
    else:
        print(f"        Total CUDA Cores: Unknown (model not in map)")
    print(f"        Is available: {torch.cuda.is_available()}")
    print("___________________________________________________\n")

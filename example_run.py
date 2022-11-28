import torch

# setting device on GPU if available, else CPU
print("Got cuda?", torch.cuda.is_available())
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_cached(0)/1024**3,1), 'GB')

    print(torch.cuda.current_device())
    print(torch.cuda.device(0))
    print(torch.cuda.device_count())
    print(torch.cuda.get_device_name(0))

print("Checking for bug fix:")

#addresses this issue: https://github.com/pytorch/pytorch/issues/67919
array = torch.ones([1, 200, 200])
print(torch.gradient(array, dim=(1, 2)))

print("Done!")

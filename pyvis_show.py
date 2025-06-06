import torch
print(torch.__version__)
print(torch.version.cuda)  # 应显示 CUDA 版本
print(torch.cuda.is_available())  # 应返回 True
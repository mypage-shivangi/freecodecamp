import numpy as np

def calculate(list):
  if len(list) !=9:
    raise ValueError("List must contain nine numbers.")
  arr=np.array(list).reshape(3,3)
  mean=[
         arr.mean(axis=0).tolist()
         ,arr.mean(axis=1).tolist()
         ,arr.mean().item()
         ]
  variance =[
        arr.var(axis=0).tolist(),
        arr.var(axis=1).tolist(),
        arr.var().item()
        ]
  sum_= [
        arr.sum(axis=0).tolist(),
        arr.sum(axis=1).tolist(),
        arr.sum().item()
    ]
  max_= [
        arr.max(axis=0).tolist(),
        arr.max(axis=1).tolist(),
        arr.max().item()
    ]
  min_= [
        arr.min(axis=0).tolist(),
        arr.min(axis=1).tolist(),
        arr.min().item()
    ]
  std= [
        arr.std(axis=0).tolist(),
        arr.std(axis=1).tolist(),
        arr.std().item()
    ]
  return {
    'mean': mean,
    'variance': variance,
    'standard deviation': std,
    'max': max_,
    'min': min_,
    'sum': sum_
}

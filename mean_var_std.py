import numpy as np

def calculate(numbers):
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")
        
    data = np.array(numbers).reshape(3, 3)
    calculations = {
        'mean': [np.mean(data, axis=0).tolist(), np.mean(data, axis=1).tolist(), np.mean(data)],
        'variance': [np.var(data, axis=0).tolist(), np.var(data, axis=1).tolist(), np.var(data)],
        'standard deviation': [np.std(data, axis=0).tolist(), np.std(data, axis=1).tolist(), np.std(data)],
        'max': [np.max(data, axis=0).tolist(), np.max(data, axis=1).tolist(), np.max(data)],
        'min': [np.min(data, axis=0).tolist(), np.min(data, axis=1).tolist(), np.min(data)],
        'sum': [np.sum(data, axis=0).tolist(), np.sum(data, axis=1).tolist(), np.sum(data)],
    }

    return calculations
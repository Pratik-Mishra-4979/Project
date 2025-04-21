import numpy as np

# === Input Validation ===
def calculate(numbers):
    # Check if the list has exactly 9 numbers
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # === Reshaping the Input ===
    # Convert the list to a 3x3 numpy array
    arr = np.array(numbers).reshape(3, 3)

    # === Calculations ===
    result = {
        # Calculate mean across columns, rows, and overall
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().item()],
        
        # Calculate variance across columns, rows, and overall
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().item()],
        
        # Calculate standard deviation across columns, rows, and overall
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().item()],
        
        # Calculate max values across columns, rows, and overall
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().item()],
        
        # Calculate min values across columns, rows, and overall
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().item()],
        
        # Calculate sum across columns, rows, and overall
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().item()]
    }

    # === Display Results ===
    # Print each statistic in the result dictionary
    for key, value in result.items():
        print(f"{key}: {value}")
    
    # Return the calculated result
    return result



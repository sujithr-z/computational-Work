import numpy as np
import time

N=2**16
DATA_INFO=[]

def compute_integer_computation_analysis():

    arr32 = np.arange(N, dtype=np.int32)
    arr64 = np.arange(N, dtype=np.int64)
    # Perform some computations on the arrays
    start_time = time.time()
    result32 = arr32 * 2 + 1
    end_time = time.time()
    DATA_INFO.append((end_time - start_time, "int32"))
    print(f"Time taken for int32 computation: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    result64 = arr64 * 2 + 1
    end_time = time.time()
    DATA_INFO.append((end_time - start_time, "int64"))
    print(f"Time taken for int64 computation: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    compute_integer_computation_analysis()
    
    if DATA_INFO[0] < DATA_INFO[1]:
        print("int32 computations are faster than int64 computations.")
    elif DATA_INFO[0] > DATA_INFO[1]:
        print("int64 computations are faster than int32 computations.") 
    else:
        print("int32 and int64 computations have the same performance.")    
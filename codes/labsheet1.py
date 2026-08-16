import numpy as np

def main():

    rng=np.random.default_rng(1024)
    B = rng.integers(0,100,(2,2))
    C = rng.integers(0,100,(2,2))
    print(f"Element-wise addition of B and C:\n{B+C}")
    print(f"Element-wise multiplication of B and C:\n{B*C}")
    print(f"Element-wise subtraction of B and C:\n{B-C}")

def question7():

    rng = np.random.default_rng(1024)
    A = rng.integers(0,360,(2,2))
    rad_A = np.radians(A)
    print(f"Sine of A:\n{np.sin(rad_A)}")
    print(f"Cosine of A:\n{np.cos(rad_A)}")
    print(f"Tangent of A:\n{np.tan(rad_A)}")

def question8():
    rng = np.random.default_rng(1024)
    A = rng.integers(0,100,(5,5))
    print(f"Min Value in array A:{np.min(A)}")
    print(f"Max Value in array A:{np.max(A)}")
    print(f"the matrix A:\n{A}")

def question9():
    rng = np.random.default_rng(1024)
    A = rng.integers(0,11,(3,5))
    f = lambda x: -1 if x>5 else x
    A = np.vectorize(f)(A)
    print(f"the matrix A:\n{A}")

def question10():
    pass
    

if __name__ == "__main__":
    question9()
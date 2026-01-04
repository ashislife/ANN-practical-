import numpy as np

# Step 1: Define P and N
P = [[1, 1], [1, 0], [0, 1]]  # Label 1
N = [[0, 0]]                  # Label 0

# Step 2: Initialize W randomly
W = np.random.randn(2)
print(f"Initial W: {W}")

# Step 3: Train
converged = False
iterations = 0

while not converged:
    iterations += 1
    converged = True
    
    # Pick random example
    if np.random.rand() < len(P)/(len(P)+len(N)):  # Pick from P
        z = P[np.random.randint(len(P))]
        z_in_P = True
    else:  # Pick from N
        z = N[np.random.randint(len(N))]
        z_in_P = False
    
    # Compute W^T z
    score = W[0]*z[0] + W[1]*z[1]
    
    # Step 5: If z in P and W^T z < 0
    if z_in_P and score < 0:
        W = W + z
        converged = False
    
    # Step 6: If z in N and W^T z > 0  
    elif not z_in_P and score > 0:
        W = W - z
        converged = False
    
    # Stop if too many iterations
    if iterations > 1000:
        print("Max iterations reached")
        break

print(f"\nFinal W: {W}")
print(f"Iterations: {iterations}")

# Test
print("\nTesting:")
for x,y in [(0,0), (0,1), (1,0), (1,1)]:
    s = W[0]*x + W[1]*y
    pred = 1 if s >= 0 else 0
    print(f"({x},{y}) -> score={s:.2f}, pred={pred}")
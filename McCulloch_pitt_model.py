# Complete OR gate check
print("VERIFICATION: McCulloch-Pitts Neuron as OR Gate")
print("="*50)

# Correct OR gate truth table
correct_or = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 1
}

# McCulloch-Pitts neuron for OR
def mp_or(x1, x2):
    return 1 if (x1 + x2) >= 1 else 0

print("\nChecking all inputs:")
print("Input | Correct OR | MP Neuron | Match?")
print("-"*40)

all_correct = True
for (x1, x2), correct_output in correct_or.items():
    mp_output = mp_or(x1, x2)
    match = "✓" if mp_output == correct_output else "✗"
    
    if mp_output != correct_output:
        all_correct = False
    
    print(f"({x1},{x2})   |     {correct_output}     |     {mp_output}     |   {match}")

print("\n" + "="*50)
if all_correct:
    print("SUCCESS: McCulloch-Pitts neuron correctly implements OR gate!")
else:
    print("FAILED: Does not correctly implement OR gate")
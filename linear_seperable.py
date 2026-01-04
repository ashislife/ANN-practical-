import numpy as np
import matplotlib.pyplot as plt

def plot_gate(gate_name, data_points, labels, gate_type):
    """Plot gate points and check linear separability"""
    plt.figure(figsize=(6, 5))
    
    # Separate points by class
    points = np.array(data_points)
    labels_arr = np.array(labels)
    
    class0 = points[labels_arr == 0]
    class1 = points[labels_arr == 1]
    
    # Plot points
    if len(class0) > 0:
        plt.scatter(class0[:, 0], class0[:, 1], color='blue', s=200, 
                   marker='o', label='Output 0', edgecolors='black', linewidth=2)
    if len(class1) > 0:
        plt.scatter(class1[:, 0], class1[:, 1], color='red', s=200, 
                   marker='s', label='Output 1', edgecolors='black', linewidth=2)
    
    # Set plot properties
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    plt.xticks([0, 1])
    plt.yticks([0, 1])
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Input X1')
    plt.ylabel('Input X2')
    
    # Check if linearly separable and draw line if possible
    separable = check_linear_separability_simple(points, labels_arr, gate_type)
    
    if separable:
        # Draw separating line
        if gate_type == "AND":
            # Line for AND: x1 + x2 = 1.5
            x = np.linspace(-0.5, 1.5, 100)
            y = 1.5 - x
            plt.plot(x, y, 'g--', linewidth=3, label='Decision Boundary')
            plt.fill_between(x, y, 1.5, color='red', alpha=0.1)
            plt.fill_between(x, y, -0.5, color='blue', alpha=0.1)
            
        elif gate_type == "OR":
            # Line for OR: x1 + x2 = 0.5
            x = np.linspace(-0.5, 1.5, 100)
            y = 0.5 - x
            plt.plot(x, y, 'g--', linewidth=3, label='Decision Boundary')
            plt.fill_between(x, y, 1.5, color='red', alpha=0.1)
            plt.fill_between(x, y, -0.5, color='blue', alpha=0.1)
            
        elif gate_type == "XOR":
            # XOR is NOT linearly separable
            # Show why with attempted lines
            plt.plot([0.5, 0.5], [-0.5, 1.5], 'r:', linewidth=2, alpha=0.5, label='Cannot separate')
            plt.plot([-0.5, 1.5], [0.5, 0.5], 'r:', linewidth=2, alpha=0.5)
        
        status = "✓ Linearly Separable"
        color = "green"
    else:
        status = "✗ NOT Linearly Separable"
        color = "red"
    
    plt.title(f'{gate_name} Gate\n{status}', color=color, fontsize=14, fontweight='bold')
    plt.legend(loc='upper right')
    
    # Add truth table as text
    truth_table = f"Truth Table:\n"
    truth_table += f"X1 X2 | Out\n"
    truth_table += f"------------\n"
    for (x1, x2), out in zip(data_points, labels):
        truth_table += f" {x1}  {x2}  |  {out}\n"
    
    plt.text(1.65, 0.5, truth_table, fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    return separable

def check_linear_separability_simple(points, labels, gate_type):
    """Simple check for linear separability"""
    if gate_type == "AND":
        return True  # AND is linearly separable
    elif gate_type == "OR":
        return True  # OR is linearly separable
    elif gate_type == "XOR":
        return False  # XOR is NOT linearly separable
    
    # For completeness, actual check:
    # Points: (0,0), (0,1), (1,0), (1,1)
    # AND: labels = [0, 0, 0, 1] - Separable by line x1 + x2 = 1.5
    # OR:  labels = [0, 1, 1, 1] - Separable by line x1 + x2 = 0.5
    # XOR: labels = [0, 1, 1, 0] - NOT separable by single line
    
    return None

# Main comparison
print("="*70)
print("GATE COMPARISON: LINEAR SEPARABILITY ANALYSIS")
print("="*70)

# Define all gates
gates = {
    "AND": {
        "points": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "labels": [0, 0, 0, 1],  # Only (1,1) = 1
        "type": "AND"
    },
    "OR": {
        "points": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "labels": [0, 1, 1, 1],  # Only (0,0) = 0
        "type": "OR"
    },
    "XOR": {
        "points": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "labels": [0, 1, 1, 0],  # 1 when inputs are different
        "type": "XOR"
    }
}

# Summary table
print("\n" + "-"*70)
print(f"{'Gate':<10} {'Linearly Separable?':<25} {'Perceptron Can Learn?':<25}")
print("-"*70)

# Plot each gate and show results
for gate_name, gate_data in gates.items():
    separable = plot_gate(gate_name, gate_data["points"], gate_data["labels"], gate_data["type"])
    
    if separable:
        linear_status = "✓ YES"
        perceptron_status = "✓ YES (Single layer)"
    else:
        linear_status = "✗ NO"
        perceptron_status = "✗ NO (Needs multi-layer)"
    
    print(f"{gate_name:<10} {linear_status:<25} {perceptron_status:<25}")

print("-"*70)

# Mathematical explanation
print("\n" + "="*70)
print("MATHEMATICAL EXPLANATION")
print("="*70)
print("\n1. AND GATE:")
print("   Decision Boundary: x1 + x2 = 1.5")
print("   Equation: w1*x1 + w2*x2 + b = 0")
print("   Weights: w1 = 1, w2 = 1, b = -1.5")
print("   Test: (1,1): 1+1-1.5=0.5≥0 → 1 ✓")
print("         (0,1): 0+1-1.5=-0.5<0 → 0 ✓")

print("\n2. OR GATE:")
print("   Decision Boundary: x1 + x2 = 0.5")
print("   Equation: w1*x1 + w2*x2 + b = 0")
print("   Weights: w1 = 1, w2 = 1, b = -0.5")
print("   Test: (0,1): 0+1-0.5=0.5≥0 → 1 ✓")
print("         (0,0): 0+0-0.5=-0.5<0 → 0 ✓")

print("\n3. XOR GATE:")
print("   NO single line can separate!")
print("   Why? Points (0,1) and (1,0) are class 1")
print("        Points (0,0) and (1,1) are class 0")
print("   These are diagonally opposite - need curved boundary")
print("   Solution: Multi-layer perceptron (neural network)")
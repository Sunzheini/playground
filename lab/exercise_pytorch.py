"""
MINIMAL PYTORCH STARTER CODE
Run this FIRST to understand PyTorch basics
"""

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

# ========== 1. CREATE SIMPLE DATA (y = 2x + 1 + noise) ==========
# Make 100 data points
X = torch.linspace(0, 10, 100).reshape(-1, 1)  # Shape: (100, 1)
true_slope = 2.0
true_intercept = 1.0
y = true_slope * X + true_intercept + torch.randn(X.shape) * 2  # Add noise

print(f"\nData shapes: X={X.shape}, y={y.shape}")
print(f"True relationship: y = {true_slope}*x + {true_intercept}")


# ========== 2. CREATE A SIMPLE MODEL ==========
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)  # 1 input, 1 output (weight and bias)

    def forward(self, x):
        return self.linear(x)


model = LinearModel()
print(f"\nModel: {model}")
print(f"Initial weight: {model.linear.weight.item():.3f}, bias: {model.linear.bias.item():.3f}")

# ========== 3. SETUP TRAINING ==========
criterion = nn.MSELoss()  # Mean Squared Error loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

# ========== 4. TRAIN THE MODEL ==========
losses = []
print("\nTraining starts...")
print("-" * 40)

for epoch in range(100):
    # Forward pass: compute predictions
    predictions = model(X)

    # Compute loss
    loss = criterion(predictions, y)
    losses.append(loss.item())

    # Backward pass: compute gradients
    optimizer.zero_grad()  # Clear old gradients
    loss.backward()  # Compute new gradients

    # Update parameters
    optimizer.step()

    # Print progress
    if epoch % 20 == 0:
        w = model.linear.weight.item()
        b = model.linear.bias.item()
        print(f"Epoch {epoch:3d}: loss = {loss.item():.4f}, w = {w:.3f}, b = {b:.3f}")

print("-" * 40)
print("Training completed!")

# ========== 5. SEE FINAL RESULTS ==========
final_weight = model.linear.weight.item()
final_bias = model.linear.bias.item()

print(f"\nFinal model: y = {final_weight:.3f}*x + {final_bias:.3f}")
print(f"True model:  y = {true_slope}*x + {true_intercept}")

# ========== 6. MAKE PREDICTIONS ==========
# Predict on new data
test_x = torch.tensor([[3.5], [7.2], [9.8]])  # New values
with torch.no_grad():  # Don't track gradients for inference
    predictions = model(test_x)

print("\nPredictions:")
for x_val, pred in zip(test_x, predictions):
    print(f"  x = {x_val.item():.1f} → predicted y = {pred.item():.2f}")

# ========== 7. VISUALIZE ==========
plt.figure(figsize=(12, 4))

# Plot 1: Data and fit
plt.subplot(1, 2, 1)
plt.scatter(X.numpy(), y.numpy(), alpha=0.5, label='Data with noise')
plt.plot(X.numpy(), model(X).detach().numpy(), 'r-', linewidth=3, label='Model fit')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Training loss
plt.subplot(1, 2, 2)
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss (MSE)')
plt.title('Training Loss Over Time')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ========== 8. SAVE THE MODEL ==========
torch.save(model.state_dict(), 'linear_model.pth')
print(f"\nModel saved as 'linear_model.pth'")

# ========== 9. LOAD AND USE LATER ==========
# How to load and use the model later:
"""
loaded_model = LinearModel()
loaded_model.load_state_dict(torch.load('linear_model.pth'))
loaded_model.eval()  # Set to evaluation mode
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate fabric image
height = 256
width = 256
fabric_image = np.zeros((height, width, 3), dtype=np.uint8)

# Generate smooth fabric pattern
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
X, Y = np.meshgrid(x, y)

# Red channel
fabric_image[:,:,0] = (255 * (1 - X)).astype(np.uint8)

# Green channel
fabric_image[:,:,1] = (255 * (1 - Y)).astype(np.uint8)

# Blue channel
fabric_image[:,:,2] = 100

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

# Display the fabric image
ax1.imshow(fabric_image)
ax1.set_title('Fabric Image')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

# Calculate mean and standard deviation of the image
mean_val = np.mean(fabric_image)
std_dev = np.std(fabric_image)

# Display mean and standard deviation below the image
ax1.text(-150, 20, f'Mean: {mean_val:.4f}', fontsize=10, color='black', ha='left')
ax1.text(-150, 30, f'Std Dev: {std_dev:.4f}', fontsize=10, color='black', ha='left')

# Plot histograms for RGB channels
ax2.hist(fabric_image[:,:,0].flatten(), bins=100, color='red')
ax2.set_title('Red Channel Histogram')
ax2.set_xlabel('Intensity')
ax2.set_ylabel('Frequency')

ax3.hist(fabric_image[:,:,1].flatten(), bins=100, color='green')
ax3.set_title('Green Channel Histogram')
ax3.set_xlabel('Intensity')
ax3.set_ylabel('Frequency')

ax4.hist(fabric_image[:,:,2].flatten(), bins=100, color='blue')
ax4.set_title('Blue Channel Histogram')
ax4.set_xlabel('Intensity')
ax4.set_ylabel('Frequency')

plt.tight_layout()
plt.show()
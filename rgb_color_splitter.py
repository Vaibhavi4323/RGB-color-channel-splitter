import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Load the image
image_path = "input.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Step 2: Convert BGR to RGB
# OpenCV loads images in BGR format by default.
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 3: Split the RGB channels
red_channel = rgb_image[:, :, 0]
green_channel = rgb_image[:, :, 1]
blue_channel = rgb_image[:, :, 2]

# Step 4: Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Step 5: Save individual grayscale channels
cv2.imwrite(
    os.path.join(output_dir, "red_channel.png"),
    red_channel
)

cv2.imwrite(
    os.path.join(output_dir, "green_channel.png"),
    green_channel
)

cv2.imwrite(
    os.path.join(output_dir, "blue_channel.png"),
    blue_channel
)

# Step 6: Create colored channel visualizations
red_visual = np.zeros_like(rgb_image)
red_visual[:, :, 0] = red_channel

green_visual = np.zeros_like(rgb_image)
green_visual[:, :, 1] = green_channel

blue_visual = np.zeros_like(rgb_image)
blue_visual[:, :, 2] = blue_channel

# Step 7: Display the images
images = [
    rgb_image,
    red_visual,
    green_visual,
    blue_visual
]

titles = [
    "Original Image",
    "Red Channel",
    "Green Channel",
    "Blue Channel"
]

plt.figure(figsize=(12, 8))

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()

print("RGB channels extracted successfully!")
print(f"Channel images saved in the '{output_dir}' folder.")
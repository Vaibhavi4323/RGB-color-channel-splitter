# 🎨 RGB Color Channel Splitter

A beginner-friendly **Computer Vision and Image Processing project** built using Python, OpenCV, NumPy, and Matplotlib. This project separates an image into its Red, Green, and Blue (RGB) color channels and visualizes each channel independently.

## 👩‍💻 Author

- **Name:** Vaibhavi Paliwal
- **Registration Number:** 24BAI10325
- **Project Domain:** Computer Vision
- **Programming Language:** Python

---

## 📌 Project Overview

Digital color images are composed of individual color channels that combine to produce the final image. The RGB color model represents each pixel using three components: Red, Green, and Blue.

The RGB Color Channel Splitter demonstrates how these components can be extracted and visualized separately using Python libraries.

The project loads an input image, extracts its three color channels, displays the original image alongside the individual channel visualizations, and saves the extracted channels as separate image files.

## ✨ Features

- 🖼️ Load an image from your local system.
- 🔴 Extract the Red color channel.
- 🟢 Extract the Green color channel.
- 🔵 Extract the Blue color channel.
- 🎨 Visualize the original image and individual color channels.
- 💾 Save each extracted channel as a separate PNG image.
- 📂 Automatically create an output directory for the processed images.
- ⚡ Perform image processing using OpenCV and NumPy.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Image loading, color conversion, and image saving |
| NumPy | Image array manipulation and channel extraction |
| Matplotlib | Image visualization and plotting |

## 📁 Project Structure

```text
RGB-Color-Channel-Splitter/
│
├── rgb_channel_splitter.py
├── input.jpg
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    ├── red_channel.png
    ├── green_channel.png
    └── blue_channel.png
```

**Note:** The `output/` directory and its images are generated automatically when the program runs. The `input.jpg` file is the input image used for processing.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/RGB-Color-Channel-Splitter.git
```

Navigate to the project directory:

```bash
cd RGB-Color-Channel-Splitter
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

For macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

If you need to create the `requirements.txt` file, add:

```text
opencv-python
numpy
matplotlib
```

### 4. Add an Input Image

Place an image named `input.jpg` in the root directory of the project.

If your image has a different name, update the following line in `rgb_channel_splitter.py`:

```python
image_path = "input.jpg"
```

### 5. Run the Project

Execute the Python script:

```bash
python rgb_channel_splitter.py
```

The program will display the original image and its Red, Green, and Blue channel visualizations.

The extracted channel images will be saved in the `output/` directory.

## 🔍 How It Works

### Step 1: Image Loading

OpenCV loads the input image using `cv2.imread()`.

```python
image = cv2.imread(image_path)
```

### Step 2: Color Space Conversion

OpenCV loads color images in BGR order by default. The image is converted to RGB order for correct channel extraction and visualization.

```python
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

### Step 3: RGB Channel Extraction

NumPy array slicing extracts the individual color channels.

```python
red_channel = rgb_image[:, :, 0]
green_channel = rgb_image[:, :, 1]
blue_channel = rgb_image[:, :, 2]
```

### Step 4: Channel Visualization

Separate arrays are created to visualize each channel independently while suppressing the other two channels.

- **Red Channel:** Displays red intensity values.
- **Green Channel:** Displays green intensity values.
- **Blue Channel:** Displays blue intensity values.

### Step 5: Save the Results

The individual channel intensity images are saved as PNG files using OpenCV.

```text
output/
├── red_channel.png
├── green_channel.png
└── blue_channel.png
```

The saved files are grayscale intensity maps, while the displayed channel visualizations are tinted with their respective colors.

## 📊 Output

The program displays four visualizations:

1. **Original Image:** The complete RGB image.
2. **Red Channel:** The image represented using red intensity values.
3. **Green Channel:** The image represented using green intensity values.
4. **Blue Channel:** The image represented using blue intensity values.

The output demonstrates how different color channels contribute to the appearance and intensity information of an image.

<!-- To display a screenshot in your README, add it to the repository and uncomment the lines below. -->
<!--
## 🖼️ Project Screenshot

![RGB Color Channel Splitter Output](screenshots/rgb-channel-output.png)
-->

## 🎯 Learning Outcomes

Through this project, I explored:

- Fundamentals of computer vision and digital image processing.
- RGB color representation and color channel separation.
- Differences between BGR and RGB channel ordering.
- Image array manipulation using NumPy.
- Image processing operations using OpenCV.
- Visualization of image data using Matplotlib.
- Saving processed images programmatically.

## 🚀 Future Enhancements

Potential improvements include:

- Adding an interactive interface using Streamlit.
- Supporting HSV color space conversion and visualization.
- Displaying color channel histograms.
- Calculating pixel intensity statistics.
- Implementing adjustable color thresholding.
- Adding color-based object detection and image segmentation.
- Supporting multiple images through batch processing.

## 📚 References

- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)

---

⭐ If you find this project useful for learning computer vision, feel free to explore and build upon it.

**Developed by Vaibhavi Paliwal 

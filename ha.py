import cv2
import numpy as np

# Read image (Change filename if needed)
img = cv2.imread(r"C:\Users\Asus\Downloads\backend\object.jpg")



if img is None:
    print("Error: Image not found. Make sure 'object.jpg' is in the same folder.")
    exit()

# Resize for better visibility (optional)
img = cv2.resize(img, (600, 500))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply binary threshold
_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Copy image for drawing
output = img.copy()

if len(contours) != 0:

    # Select largest contour (main object)
    c = max(contours, key=cv2.contourArea)

    # Calculate Area
    area = cv2.contourArea(c)

    # Calculate Perimeter
    perimeter = cv2.arcLength(c, True)

    # Draw contour
    cv2.drawContours(output, [c], -1, (0, 255, 0), 3)

    # Display area & perimeter on image
    cv2.putText(output, f"Area: {area:.2f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(output, f"Perimeter: {perimeter:.2f}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    print("Area of object:", area)
    print("Perimeter of object:", perimeter)

else:
    print("No object detected!")

# Show results
cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Output", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
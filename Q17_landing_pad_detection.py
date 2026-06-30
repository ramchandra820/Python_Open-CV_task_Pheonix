"""
Q17) Drone Landing Pad Detector
------------------------------------
Detect a rectangular white landing pad on a dark background from a
drone camera feed image, and "land" the drone on it (just print a
landing message — no real flight control). Save the annotated result
as 'sahi.jpg'.

NOTE: Replace INPUT_IMAGE_PATH below with the actual path to your
drone camera frame. A synthetic test frame ('landing_pad_frame.jpg')
is provided in the sample_images folder for testing.
"""

import cv2

INPUT_IMAGE_PATH = "landing_pad_frame.jpg"  # <-- replace with your own drone frame if needed

# Step 1: Load the drone camera frame from disk
img = cv2.imread(INPUT_IMAGE_PATH)

if img is None:
    raise FileNotFoundError(f"Could not load image at '{INPUT_IMAGE_PATH}'. Check the path.")

# Step 2: Convert to grayscale -> easier to threshold brightness than full color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Threshold the grayscale image so only bright (white) pixels survive
# Pixels above 200 brightness become white (255), everything else becomes black (0)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Step 4: Find the outlines (contours) of the white blobs left after thresholding
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

landing_pad_found = False
best_contour = None
best_area = 0

# Step 5: Examine each contour to find the one that looks like our landing pad
for cnt in contours:
    area = cv2.contourArea(cnt)

    # Ignore tiny specks of white noise; a real landing pad will be reasonably large
    if area < 500:
        continue

    # Get the bounding rectangle of this contour to check its shape
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = w / float(h)

    # A landing pad should be roughly rectangular (not extremely thin/long)
    if 0.3 < aspect_ratio < 3.0 and area > best_area:
        best_area = area
        best_contour = (x, y, w, h)
        landing_pad_found = True

# Step 6: Draw a bounding box around the detected landing pad (if found)
if landing_pad_found:
    x, y, w, h = best_contour
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # green box

    # Mark the center point of the landing pad
    center_x, center_y = x + w // 2, y + h // 2
    cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)  # red center dot

    cv2.putText(img, "LANDING PAD", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Step 7: "Land" the drone — just print the message as instructed
    print(f"Landing pad detected at center ({center_x}, {center_y}), area={best_area:.0f} px")
    print("Landing")
else:
    print("No landing pad detected. Holding position.")

# Step 8: Save the annotated result image as required
cv2.imwrite("sahi.jpg", img)
print("Result saved as 'sahi.jpg'")

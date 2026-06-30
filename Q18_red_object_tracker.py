"""
Q18) Drone Camera Red Object Tracker
-----------------------------------------
Simulate a drone's camera following a red object (ball/marker) in live
video using OpenCV's HSV color filtering.

Run this on a machine with a webcam attached -- it opens VideoCapture(0)
and shows a live window. Press 'q' to quit.

For headless testing/screenshots (no camera available), this file also
has a TEST_MODE flag that processes a single static demo image instead
of a live feed (see sample_images/red_object_frame.jpg).
"""

import cv2
import numpy as np

TEST_MODE = False  # set to True to run on a static test image instead of a webcam


def detect_red_object(frame):
    """
    Takes one BGR video frame, finds the largest red blob using HSV
    color filtering, draws a circle around it, and overlays detection
    status text. Returns the annotated frame.
    """
    # Step 1: Convert frame from BGR color space to HSV
    # HSV separates color (Hue) from brightness/saturation, making
    # color-based filtering far more reliable than using raw BGR values.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 2: Define the HSV range for "red".
    # Red sits at the very start AND the very end of the Hue wheel (0 and 180),
    # so two ranges are needed to fully capture all shades of red.
    lower_red_1 = np.array([0, 120, 70])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([170, 120, 70])
    upper_red_2 = np.array([180, 255, 255])

    # Step 3: Create binary masks for each red range and combine them
    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Step 4: Clean up the mask a little (remove small noise specks)
    red_mask = cv2.erode(red_mask, None, iterations=2)
    red_mask = cv2.dilate(red_mask, None, iterations=2)

    # Step 5: Find contours (outlines) of all red blobs in the mask
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    object_detected = False

    if contours:
        # Pick the largest red contour -> assume that's our tracked object
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # Ignore tiny red specks (noise) -- require a minimum area
        if area > 300:
            # Get the smallest circle that fully encloses the contour
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Draw the tracking circle and its center point
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.circle(frame, center, 4, (255, 255, 255), -1)
            object_detected = True

    # Step 6: Overlay status text depending on whether we found the object
    if object_detected:
        cv2.putText(frame, "Object detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Object lost", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return frame, object_detected


if __name__ == "__main__":
    if TEST_MODE:
        # Headless single-image test (useful when no webcam is available)
        frame = cv2.imread("sample_images/red_object_frame.jpg")
        result, detected = detect_red_object(frame)
        cv2.imwrite("red_object_result.jpg", result)
        print(f"Object detected: {detected}. Result saved as 'red_object_result.jpg'")
    else:
        # Live webcam mode (this is the actual drone-camera simulation)
        cap = cv2.VideoCapture(0)  # 0 = default webcam; replace with a video file path if needed

        if not cap.isOpened():
            print("Could not access the camera. Set TEST_MODE = True to test on a static image.")
        else:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame. Exiting.")
                    break

                frame, _ = detect_red_object(frame)

                cv2.imshow("Drone Red Object Tracker", frame)

                # Press 'q' to quit the live feed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

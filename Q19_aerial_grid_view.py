"""
Q19) Aerial Grid View — Click to Select a Cell
-----------------------------------------------------
Simulate an aerial view from a drone: draw an 8x8 grid over an image.
When the user clicks a cell, print its (row, col) coordinates and
highlight that cell in blue.

Run this on a machine with a display -- it opens a window and waits
for mouse clicks. Press any key to close the window.
"""

import cv2

IMAGE_PATH = "aerial_view.jpg"  # replace with your own aerial image if you like
ROWS, COLS = 8, 8

# Step 1: Load the base image
img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Could not load image at '{IMAGE_PATH}'. Check the path.")

height, width = img.shape[:2]

# Step 2: Work out how big each grid cell is in pixels
cell_height = height // ROWS
cell_width = width // COLS

# Keeps track of which cell (row, col) was last clicked, so we can re-draw
# the highlight every time the display is refreshed
selected_cell = None


def draw_grid_view():
    """
    Draws the 8x8 grid lines on a fresh copy of the image, and if a cell
    has been selected, highlights it with a blue rectangle. Then shows
    the result in the window.
    """
    display_img = img.copy()  # always draw on a fresh copy so old highlights don't stack up

    # Draw vertical grid lines
    for col in range(1, COLS):
        x = col * cell_width
        cv2.line(display_img, (x, 0), (x, height), (255, 255, 255), 1)

    # Draw horizontal grid lines
    for row in range(1, ROWS):
        y = row * cell_height
        cv2.line(display_img, (0, y), (width, y), (255, 255, 255), 1)

    # If a cell has been selected, highlight it with a blue filled-ish rectangle
    if selected_cell is not None:
        sel_row, sel_col = selected_cell
        top_left = (sel_col * cell_width, sel_row * cell_height)
        bottom_right = ((sel_col + 1) * cell_width, (sel_row + 1) * cell_height)
        # Blue (BGR = 255,0,0), thickness 3 for a visible highlight border
        cv2.rectangle(display_img, top_left, bottom_right, (255, 0, 0), 3)

        # Label the selected cell's coordinates near the top-left of the cell
        label = f"({sel_row},{sel_col})"
        cv2.putText(display_img, label, (top_left[0] + 5, top_left[1] + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow("Aerial Grid View", display_img)


def mouse_callback(event, x, y, flags, param):
    """
    Called automatically by OpenCV whenever a mouse event happens on
    the window. We only care about left-button clicks.
    """
    global selected_cell

    if event == cv2.EVENT_LBUTTONDOWN:
        # Convert pixel (x, y) into a grid (row, col) index
        col = x // cell_width
        row = y // cell_height
        selected_cell = (row, col)

        print(f"Clicked at: x={x}, y={y} -> Grid cell: row={row}, col={col}")

        # Re-draw the grid with the new highlight applied
        draw_grid_view()


# Step 3: Show the initial grid (no cell selected yet) and register the click handler
draw_grid_view()
cv2.setMouseCallback("Aerial Grid View", mouse_callback)

# Step 4: Wait for the user to press any key, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

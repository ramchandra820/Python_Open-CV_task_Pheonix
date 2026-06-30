# Python & OpenCV Task — Drone Systems

This repository contains the complete solutions for the **Python & OpenCV Task**, covering
fundamental Python concepts (data types, control flow, recursion, data structures, OOP) and
applied computer vision with OpenCV — all themed around drone systems (telemetry, fleet
management, mission planning, and camera-based detection).

## 📁 Repository Structure

```
.
├── Q1_drone_movement.py              # Roll/Pitch/Yaw movement selector
├── Q2_weight_checker.py              # Body + payload weight calculator (kg/g)
├── Q3_drone_specs.py                 # Drone specs, types, payload calc, unit conversion
├── Q4_telemetry_parser.py            # Parses a pipe-delimited telemetry string
├── Q5_flight_path_analyser.py        # Altitude list analysis (max, avg, climb rates)
├── Q6_waypoint_mission_planner.py    # Tuple unpacking, search, immutability demo
├── Q7_fleet_health_monitor.py        # Dictionary-based fleet management
├── Q8_airspace_conflict_checker.py   # Set operations for airspace zone checking
├── Q9_auto_rth_system.py             # RTH trigger rules + descent simulation (while loop)
├── Q11_recursive_waypoint_distance.py # Pure recursion: path distance + longest leg
├── Q13_coordinate_mover.py           # Step-by-step coordinate movement
├── Q14_login_authentication.py       # Case-insensitive login check
├── Q15_vowel_counter.py              # Vowel counter
├── Q16_ord_chr_uppercase.py          # Lowercase→uppercase using ord()/chr() only
├── Q17_landing_pad_detection.py      # OpenCV: detect white landing pad, save sahi.jpg
├── Q18_red_object_tracker.py         # OpenCV: HSV-based red object tracking (live feed)
├── Q19_aerial_grid_view.py           # OpenCV: 8x8 clickable grid overlay
├── WRITTEN_ANSWERS_Q10_Q12_Q20.md    # Q10 (data structures), Q12 (OOP), Q20 (color detection)
├── sample_images/                    # Synthetic test images used to verify Q17–Q19
└── verification_outputs/             # Example output images proving the CV logic works
```

> **Note on Q10, Q12, Q20:** these are descriptive/theory questions (no code to run), so
> their answers are written up in `WRITTEN_ANSWERS_Q10_Q12_Q20.md`, including a text-based
> flowchart for Q20.

## ▶️ How to Run

Each Python file is self-contained and can be run independently:

```bash
python3 Q1_drone_movement.py
```

Most scripts (Q1–Q16) take input directly from the terminal via `input()`, exactly as
described in the task's sample inputs/outputs.

### OpenCV scripts (Q17–Q19)

These need an image and/or a webcam:

- **Q17** (`Q17_landing_pad_detection.py`) reads `landing_pad_frame.jpg` (a synthetic
  white-rectangle-on-dark-background test image is provided in `sample_images/` — copy it
  to the working directory, or point `INPUT_IMAGE_PATH` at your own drone frame) and saves
  the annotated result as `sahi.jpg`.
- **Q18** (`Q18_red_object_tracker.py`) opens your webcam (`cv2.VideoCapture(0)`) by
  default and tracks a red object live — press `q` to quit. Set `TEST_MODE = True` inside
  the file to instead run it once on the static `sample_images/red_object_frame.jpg` (no
  webcam needed).
- **Q19** (`Q19_aerial_grid_view.py`) reads `aerial_view.jpg` (also provided in
  `sample_images/`), opens a window with an 8x8 grid overlay, and prints + highlights the
  cell you click. Press any key to close the window.

### Requirements

```bash
pip install opencv-python numpy
```

## ✅ Verification

Since the original task didn't supply any sample images, synthetic test images were
generated (see `sample_images/`) to verify the OpenCV detection logic actually works
correctly before submission. The corresponding results are saved in
`verification_outputs/`:

- `sahi.jpg` — landing pad correctly detected and boxed in green (Q17)
- `red_object_result.jpg` — red ball correctly detected and circled, with "Object
  detected" overlay text (Q18)
- `aerial_grid_result.jpg` — 8x8 grid drawn with a simulated click correctly highlighting
  cell `(2, 5)` in blue (Q19)

All Q1–Q16 scripts were also run with the sample inputs given in the task PDF and produced
output matching the expected examples exactly.

## 🧠 Concepts Covered

- Input/output, type conversion, string formatting (f-strings)
- Conditionals (`if`/`elif`/`else`) and loops (`for`, `while`)
- Lists, tuples, sets, dictionaries — and *why* each is the right tool for a given job
- String parsing/methods (`.split()`, `.replace()`, `.strip()`, case handling)
- Exception handling (`try`/`except`) and immutability
- Recursion (no-loop path/distance calculations)
- Object-Oriented Programming pillars (encapsulation, abstraction, inheritance,
  polymorphism)
- OpenCV: color spaces (BGR → HSV → grayscale), thresholding, contour detection,
  bounding shapes, mouse callbacks, and basic image annotation

## ✍️ Author's Note

Every line of code is commented to explain *what* it does and *why*, as requested in the
task instructions. Feel free to open an issue if anything is unclear!

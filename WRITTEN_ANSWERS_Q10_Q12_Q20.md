# Written Answers — Q10, Q12, Q20

---

## Q10) Choosing the Right Data Structure (List, Tuple, or Set)

**A) Live sensor stream (altitude, speed, battery — captured every 100 ms)**
A **list** is the best fit here. Lists are mutable and support fast `.append()` calls
(amortised O(1)), which matters because new readings arrive constantly and need to be
added to the end of the stream without rebuilding the whole collection. Lists also give
O(1) random access by index, so the program can instantly pull up "the reading from 5
seconds ago" or update a specific entry. If a tuple were used instead, every new reading
would force the creation of an entirely new tuple (since tuples are immutable), which is
wasteful and slow at high frequency. A set would be even worse: it has no guaranteed
order and no indexing at all, so "what was the altitude 2 seconds ago" becomes
impossible to answer directly.

**B) GPS home-point coordinates (set once before takeoff)**
A **tuple** is ideal here, e.g. `home_point = (23.0225, 72.5714)`. The whole point of the
home point is that it must *never* change mid-flight — accidentally overwriting it could
send the drone to the wrong location during an emergency Return-to-Home. Tuples are
immutable, so Python itself enforces this safety: any attempt to reassign an element
raises a `TypeError`. If a list were used instead, nothing would stop a stray line of
code (or a bug) from quietly mutating the coordinates mid-mission, which is a serious
safety risk for something this critical.

**C) Unique error codes logged during flight**
A **set** is the right structure. Sets automatically discard duplicates, which matches
the requirement that repeated error codes like "E01" appearing twice are meaningless —
we only care about *which* errors occurred, not how many times. Sets also use hashing
internally, giving O(1) average-case membership checks, so testing `"E99" in error_set`
to check for a critical error is essentially instant. Using a list instead would mean
duplicate codes pile up uselessly and checking membership requires scanning the entire
list (O(n)), which gets slower as the flight log grows.

---

## Q12) OOP Concepts in Python — The Four Pillars

Object-Oriented Programming (OOP) organizes code around **objects** — bundles of data
(attributes) and behavior (methods) modeled on real-world entities (e.g. a `Drone`
class with `battery`, `altitude` attributes and a `take_off()` method). Python supports
OOP fully, and it rests on four core pillars:

**1. Encapsulation**
Encapsulation means bundling an object's data and the methods that operate on that data
together inside a class, and restricting direct access to internal details. In Python,
this is commonly done with a leading underscore (`_battery`) for "internal use" or
double underscore (`__battery`) for name-mangled private attributes, paired with
getter/setter methods or `@property` decorators. This protects an object's internal
state from being changed in invalid ways from outside the class — e.g. preventing
`drone.battery = -50`, which makes no physical sense.

**2. Abstraction**
Abstraction means hiding complex implementation details and exposing only the
essential features a user of the class needs. For example, a `Drone` class might expose
a simple `.land()` method, while internally it handles motor throttling, sensor checks,
and stabilization logic that the caller never has to think about. Python supports this
through abstract base classes (the `abc` module), which let you define a required
interface without specifying *how* it's implemented.

**3. Inheritance**
Inheritance allows one class (the child/subclass) to reuse and extend the attributes and
methods of another class (the parent/superclass). For example, a `Quadcopter` class
could inherit from a general `Drone` class, automatically gaining its `take_off()` and
`land()` methods while adding its own specialized behavior. This avoids rewriting common
code and models natural "is-a" relationships (a Quadcopter *is a* Drone).

**4. Polymorphism**
Polymorphism means objects of different classes can be used interchangeably through a
shared interface, with each class providing its own specific behavior for the same
method call. For example, both `Quadcopter` and `FixedWingDrone` might implement a
`move()` method, but each does it differently internally — yet calling `drone.move()`
works correctly regardless of which type `drone` actually is. Python achieves this
naturally through duck typing ("if it walks like a duck and quacks like a duck...") and
method overriding.

Together, these four pillars let large programs (like fleet-management or flight-control
software) stay organized, reusable, and easier to extend safely as requirements grow.

---

## Q20) The Logic of Colour Detection

**Description:**
Colour detection in OpenCV almost always works by converting an image from BGR (the
default OpenCV colour order) into the **HSV** colour space, rather than working directly
with BGR or RGB values. This is because HSV separates colour information into three
independent, more intuitive components:

- **Hue (H)** — the actual colour itself (red, green, blue, etc.), represented as an
  angle around a colour wheel (0–180 in OpenCV's 8-bit scaling).
- **Saturation (S)** — how vivid/pure the colour is, versus washed out or gray.
- **Value (V)** — how bright or dark the colour is.

Because Hue alone captures "which colour", a target colour like red can be isolated by
defining a Hue range (plus reasonable Saturation/Value minimums to avoid noise) and
ignoring lighting and shadow variation almost entirely — something that's very difficult
to do reliably in raw BGR, where a colour's RGB numbers change drastically under
different lighting.

**The overall pipeline is:**
1. Capture a frame from the camera (BGR format).
2. Convert it to HSV using `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`.
3. Define a lower and upper HSV bound for the target colour (two ranges for red, since
   red wraps around both ends of the Hue circle: 0 and 180).
4. Use `cv2.inRange()` to produce a binary mask — white where the colour matches, black
   everywhere else.
5. Clean up the mask (erode/dilate) to remove small noise specks.
6. Find contours on the mask with `cv2.findContours()` to locate the actual blob(s) of
   that colour.
7. Pick the largest contour (assumed to be the target object), draw a bounding shape
   around it, and report "detected" or "lost" depending on whether a contour of
   sufficient size was found.

**Flowchart:**

```
 +-----------------------+
 |  Capture video frame   |
 |       (BGR)            |
 +-----------+------------+
             |
             v
 +-----------------------+
 | Convert BGR -> HSV     |
 +-----------+------------+
             |
             v
 +-----------------------------+
 | Apply cv2.inRange() with     |
 | lower/upper HSV bounds       |
 |   -> produces binary mask    |
 +-----------+-------------------+
             |
             v
 +-----------------------+
 | Erode + Dilate mask    |
 | (remove noise)          |
 +-----------+------------+
             |
             v
 +-----------------------+
 | cv2.findContours()     |
 +-----------+------------+
             |
        +----+-----+
        | Any large |
        | contour?   |
        +----+--+----+
         Yes |  | No
             v  v
 +--------------+  +--------------+
 | Draw circle/  |  | Print "Object |
 | box, print     |  | lost"          |
 | "Object         |  +--------------+
 | detected"       |
 +--------------+
```


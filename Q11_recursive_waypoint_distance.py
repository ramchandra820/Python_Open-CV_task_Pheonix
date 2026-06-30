"""
Q11) Recursive Waypoint Distance Calculator
-----------------------------------------------
Pure recursion (no loops) to compute total path distance and the
longest single leg between consecutive waypoints.
"""

waypoints = [(0, 0), (3, 4), (6, 8), (10, 8), (10, 0)]


def euclidean_distance(p1, p2):
    """
    Straight-line distance between two (x, y) points.
    Not recursive itself (it's a one-step formula), used as a helper
    by the recursive functions below.
    """
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def total_distance(waypoints, index=0):
    """
    Recursively computes the total path distance across all waypoints.

    Base case: if we're at the last waypoint (or beyond), there's no
    further leg to travel, so the remaining distance is 0.

    Recursive case: distance of the CURRENT leg (index -> index+1)
    PLUS the total distance of the REST of the path (index+1 onward).
    """
    # Base case: only one waypoint left (or none) -> nothing more to travel
    if index >= len(waypoints) - 1:
        return 0

    # Distance for just this one leg (current point to next point)
    current_leg = euclidean_distance(waypoints[index], waypoints[index + 1])

    # Recursively add the distance of all remaining legs
    return current_leg + total_distance(waypoints, index + 1)


def find_longest_leg(waypoints, index=0, max_dist=0):
    """
    Recursively finds the longest single leg (segment) in the journey.

    Base case: if we're at the last waypoint (or beyond), there's no
    more legs to compare, so we simply return the max_dist found so far.

    Recursive case: compute the current leg's distance, compare with
    max_dist found so far, and pass the larger of the two onward to
    the next recursive call.
    """
    # Base case: no more legs left to check -> return what we've found
    if index >= len(waypoints) - 1:
        return max_dist

    # Distance of the current leg
    current_leg = euclidean_distance(waypoints[index], waypoints[index + 1])

    # Update max_dist if this leg is longer than anything found so far
    new_max = max(max_dist, current_leg)

    # Recurse onward to check the rest of the legs
    return find_longest_leg(waypoints, index + 1, new_max)


# ----------------------------------------------------------------------
# Run and display results
# ----------------------------------------------------------------------
print(f"Waypoints: {waypoints}\n")

total = total_distance(waypoints)
print(f"Total path distance: {round(total, 3)} units")

longest_leg = find_longest_leg(waypoints)
print(f"Longest single leg distance: {round(longest_leg, 3)} units")

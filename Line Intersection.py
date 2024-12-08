import matplotlib.pyplot as plt

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - p[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

def intersection_point(p1, q1, p2, q2):
    x1, y1 = p1
    x2, y2 = q1
    x3, y3 = p2
    x4, y4 = q2

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None  
    
    intersect_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    intersect_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    return (intersect_x, intersect_y)

def plot_lines(p1, q1, p2, q2, intersect):
    fig, ax = plt.subplots()

    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)

    x_values1, y_values1 = [p1[0], q1[0]], [p1[1], q1[1]]
    x_values2, y_values2 = [p2[0], q2[0]], [p2[1], q2[1]]
    
    ax.plot(x_values1, y_values1, label="Հատված 1", color="brown")
    ax.plot(x_values2, y_values2, label="Հատված 2", color="yellow")

    if intersect:
        ax.scatter([intersect[0]], [intersect[1]], color="green", label="Հատման կետ", zorder=5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid(True)
    plt.title("Line Intersection")
    plt.show()

segment1_start = (1, 2)
segment1_end = (10, 2)

segment2_start = (5, 0)
segment2_end = (5, 5)

intersect_1_2 = do_intersect(segment1_start, segment1_end, segment2_start, segment2_end)

intersect_point = intersection_point(segment1_start, segment1_end, segment2_start, segment2_end)

plot_lines(segment1_start, segment1_end, segment2_start, segment2_end, intersect_point) 

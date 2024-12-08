import matplotlib.pyplot as plt
import random
import math

points = [(random.randint(0, 20), random.randint(0, 20)) for i in range(20)]  

start = min(points, key=lambda p: (p[1], p[0]))

def polar_angle(p):
    return math.atan2(p[1] - start[1], p[0] - start[0])

sorted_points = sorted(points, key=polar_angle)

def is_left_turn(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

convex_hull = [start]
for point in sorted_points[1:]:
    while len(convex_hull) > 1 and not is_left_turn(convex_hull[-2], convex_hull[-1], point):
        convex_hull.pop()
    convex_hull.append(point)
convex_hull.append(convex_hull[0])  

x, y = zip(*points)
hx, hy = zip(*convex_hull)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="pink", label="Բոլոր կետերը")  
plt.plot(hx, hy, color="green", label="Կոնվեքս պատյան")  
plt.legend()
plt.title("Graham scan")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

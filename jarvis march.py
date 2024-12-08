import matplotlib.pyplot as plt
import random

points = [(random.randint(0, 20), random.randint(0, 20)) for i in range(20)]  

def is_left_turn(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def jarvis_march(points):
    start = min(points, key=lambda p: (p[0], p[1]))
    hull = [start]  

    current = start
    while True:
        next_point = points[0]  
        for p in points:
            if next_point == current or is_left_turn(current, next_point, p):
                next_point = p
        if next_point == start:
            break
        hull.append(next_point)  
        current = next_point

    hull.append(start)  
    return hull

convex_hull = jarvis_march(points)

x, y = zip(*points)
hx, hy = zip(*convex_hull)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="#e06170", label="Բոլոր կետերը") 
plt.plot(hx, hy, color="#508e2a", label="Կոնվեքս պատյան")  
plt.legend()
plt.title("Jarvis March")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

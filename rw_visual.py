# Req 1 Import pyplot from matplotlib as plt
import matplotlib.pyplot as plt
# Req 2 Import the RandomWalk class from random_walk.py
from random_walk import RandomWalk

# Req 3.1 Keep making new walks, as long as the program is active.
while True:
    # Req 3.2 Make a random walk initializing with 50,000 points.
    rw = RandomWalk(50_000)
    # Req 3.3 Call fill_walk function
    rw.fill_walk()

    # Req 3.4 User the classic style
    plt.style.use('classic')
    # Req 3.5 Plot the points in the walk.
    fig, ax = plt.subplots(figsize=(21, 9),dpi=140)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)

    # Req 3.6 Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Req 4
    plt.show()

    # Req 5 Continue or end the loop
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

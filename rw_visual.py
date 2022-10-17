import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Keep making new walks as long as the program is active
while True:
    # Make a random walk.
    rw = Randomwalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues,
               edgecolor='none', s=1)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Emphasize the first and last point.
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none',
               s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

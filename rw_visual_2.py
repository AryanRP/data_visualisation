from plotly import Scatter

from random_walk import Randomwalk

# Keep making new walks as long as the program is active
while True:
    # Make a random walk.
    rw = Randomwalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    fig = Scatter(rw.x_value, rw.y_value)

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

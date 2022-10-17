import matplotlib.pyplot as plt


from die import Die


# create three D6 dies.
die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list
results = [die_1.roll() * die_2.roll() for roll_num in range(50_000)]

# Analyse the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# visualize the results.
x_values = list(range(1, max_result+1))
y_values = frequencies

plt.bar(x_values, y_values)
plt.title('Dices Rolled * calculation')
plt.xlabel('Possible outcomes')
plt.ylabel('Frequency of outcomes')
plt.show()

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)
ax.set_title("Cubic values", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cubic Values', fontsize=14)
ax.axis([0, 5100, 0, 91000000000])
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()

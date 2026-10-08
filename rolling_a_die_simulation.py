import numpy as np
import matplotlib.pyplot as plt

#probability
rolls = np.random.randint(1, 7, 100000)
counts = []
for number in range(1, 7):
  count = np.sum(rolls == number)
  counts.append(count)
  probability = count/100000
  print(number, count, probability)

#bar graph
plt.bar(range(1, 7), counts)
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.title("Rolling dice simulation")
plt.savefig("rolling_dice_simulation.png")
plt.close()
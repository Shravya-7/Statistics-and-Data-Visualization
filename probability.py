import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#marks of students in a dataframe graph
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [65, 72, 81, 55, 90]
}
df = pd.DataFrame(data)
print(df)
print(df["Marks"].mean())

#bar graph
plt.bar(df["Name"],df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.savefig("student_marks.png")
plt.close()

#histogram
plt.hist(df["Marks"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")
plt.savefig("marks_distribution.png")
plt.close()

#coin toss probability
trails = [10, 100, 1000, 10000]
for n in trails:
  result = np.random.choice(["Head","Tail"],size = n)
  probability = np.sum(result == "Head")/n
  print(n,probability)
  counts = [
    np.sum(result == "Head"),
    np.sum(result == "Tail")
]
  
#bar graph representing the counts of heads and tails
plt.bar(["Head","Tail"],counts)
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.title("Coin toss simulation")
plt.savefig("coin_toss_simulation.png")
plt.close()
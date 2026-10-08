import numpy as np
import itertools
import matplotlib.pyplot as plt

#1.Coin Toss probability
#Write a Python program to generate the sample space for three coin tosses and calculate the probability of:
#- a) Getting exactly 3 Heads
#- b) Getting exactly 2 Heads
#- c) Getting at least 1 Head
#Hint: Use itertools.product().
coin_space = ['H', 'T']
three_coins = list(itertools.product(coin_space, coin_space, coin_space))
print("Sample space = ", three_coins)

three_heads = [s for s in three_coins if s.count('H') == 3]
P_3H = len(three_heads)/len(three_coins)
print(f"P(3 heads) = ",P_3H)

two_heads = [s for s in three_coins if s.count('H') == 2]
P_2H = len(two_heads)/len(three_coins)
print(f"P(2 heads) = ",P_2H)

one_heads = [s for s in three_coins if s.count('H') >= 1]
P_1H = len(one_heads)/len(three_coins)
print(f"P(1 head) = ",P_1H)


#2. Dice Probability
#Write a Python program to calculate the probability of getting:
#- a) An even number
#- b) An odd number
#- c) A number greater than 4
#- d) A number less than or equal to 3
#Use the sample space of a single die.
dice = list(range(1, 7))
A = [x for x in dice if x % 2 == 0]#even
P_E = len(A)/len(dice)
print("Probability of getting even = ",P_E)

dice = list(range(1, 7))
A = [x for x in dice if x % 2 != 0]#odd
P_O = len(A)/len(dice)
print("Probability of getting odd = ",P_O)

dice = list(range(1, 7))
A = [x for x in dice if x > 4]#even
P_F = len(A)/len(dice)
print("Probability of getting greater than 4 = ",P_F)

dice = list(range(1, 7))
A = [x for x in dice if x <= 3]#even
P_E = len(A)/len(dice)
print("Probability of getting even = ",P_E)


#3. Two-Dice Experiment
#Generate the sample space for rolling two dice and calculate the probability that:
#- a) The sum is 7
#- b) The sum is greater than 8
#- c) Both dice show the same number
#- d) At least one die shows 6
#Hint: Use itertools.product(range(1,7), range(1,7)).
dice = list(range(1, 7))
two_dice = list(itertools.product(dice, dice))
print("Sample space: ",two_dice)

A =[]
for x in two_dice:
  if sum(x) == 7:
      A.append(x)
print("Probability that sum is 7 = ", len(A)/len(two_dice))

A = []
for x in two_dice:
  if sum(x) >= 8:
    A.append(x)
print("Probability  that sum greater than 8= ", len(A)/len(two_dice))

A =[]
for x in two_dice:
  if x[0] == x[1]:
    A.append(x)
prob = len(A)/len(two_dice)
print("Probability that both number are same = ",prob)


#5. Law of Large Numbers
#Simulate 10,000 fair coin tosses and calculate the cumulative probability of Heads after every toss.
#Plot:
#- X-axis → Number of tosses
#- Y-axis → Cumulative probability of Heads
#- Horizontal line → \(P(H)=0.5\)
#Use a logarithmic X-axis.
n_total = 10000
tosses  = np.random.binomial(1, 0.5, n_total)
emp_prob = [tosses[:i].mean() for i in range(1, n_total+1)]
plt.figure(figsize=(10,4))
plt.plot(emp_prob, color='steelblue', linewidth=1)
plt.axhline(0.5, color='red', linestyle='--', label='P(H)=0.5')
plt.xscale('log')
plt.title('Cumilative probability')
plt.xlabel('Number of tosses')
plt.ylabel('Cumilative probability of heads')
plt.legend(); plt.tight_layout(); plt.savefig("Cumilative probability")
plt.close()



#6. Conditional Probability with Dice
#Roll a die.
#Define:
#- \(A\): number is even
#- \(B\): number is greater than 3
#- Write a program to calculate: P(A|B)
#- Verify the result manually.
P_even = float(input("Enter the probability that the numvber is even (A)"))
P_greaterthn3 = float(input("Enter the probability that the number is greater than 3 (B)"))
P_both = float(input("Enter the probability that the number is both even and greater than 3 (A and B)"))
P_AafterB = P_both/P_greaterthn3
print(f"P(A/B) = {P_AafterB*100:.2f}%")


#7. Bayes' Theorem - Medical Test Problem
#A disease affects 2% of a population.
#A diagnostic test has:
#- Sensitivity = 95%
#- False-positive rate = 4%
#- Write a Python program to calculate: P(Disease|Positive)
#- Display the answer as a percentage.
sensitivity = 0.95
false_pos = 0.04
P_disease = 0.02
P_pos = sensitivity * P_disease + false_pos*(1-P_disease)
P_pos_disease = (P_pos * P_disease)/P_pos
print(f"P(Disease / Positive) = {P_pos_disease:.4f}({P_pos_disease*100:.2f}%)")
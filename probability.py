#suppose 100 srudents are surveyed 60 know python 40 know ml 30 know both
#what is p(ml|python) = p(ml and python)/p(python)
python_students= 60
knwboth = 30
probability = knwboth / python_students
print(probability)

#probability that a student fails subject 1 if he fails subject 2
fail1= 0.25
fail2= 0.15
both = 0.1
probability = both/fail2
print(probability)

#probability that people love cricket also love football
#probability that people love football also love cricket
cricket = 60
football = 40
both = 25
prob = (both/cricket)*100
prob2 = (both/football)*100
print(f"{round(prob,2)}%,{prob2}%")

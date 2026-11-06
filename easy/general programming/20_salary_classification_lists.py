#this is a list of salaries. Classify them to 2 categories. Low salaries and high salaries if they are under/over 2.000 respectively

raw_salaries = [900, 1500, 3200, 850, 4100, 1200, 2800, 950, 5000, 1100]

low_salaries = []
high_salaries = []

for salary in raw_salaries:
  if salary < 2000:
    low_salaries.append(salary)
  else:
    high_salaries.append(salary)

low_salaries.sort()
high_salaries.sort()

print(f" low salaries are {low_salaries} and the number of them is {len(low_salaries)}")
print(f" high salaries are {high_salaries} and the number of them {len(high_salaries)}")



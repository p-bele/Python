problem: The restaurant tip calculator

print("Welcome to our restaurant")
bill = float(input("ho much is the bill? "))  #input is always str, cast it to int if it's number

tips = 15/100* bill

print(f"the tips are {tips:.2f} euros")      #for rounding in 2 decimal points {tips:.2f}
print(f"in total you are paying {bill+tips:.2f} euros")

is_student = True
age = int(input("what is your age? "))

if is_student or age<18:
  print(f"the ticket costs {6} euros")
else:                                         
  print(f"the ticket costs {10} euros")

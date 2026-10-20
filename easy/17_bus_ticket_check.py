counter_valid = 0
counter_invalid = 0

for seats in range(1,6):
  print(f"seat number {seats}")
  answer = input("do you have a ticket? yes/no ")
  if answer.upper() == "YES":
    counter_valid +=1
  elif answer.upper()=="NO":
    counter_invalid +=1
  else:
    while answer.upper() != "YES" and answer.upper() != "NO":
      print("invalid answer")
      answer = input("do you have a ticket? yes/no ")
      if answer.upper() == "YES":
        counter_valid +=1
      elif answer.upper()=="NO":
        counter_invalid +=1




print(f"valid tickets: {counter_valid}")
print(f"invalid tickets: {counter_invalid}")

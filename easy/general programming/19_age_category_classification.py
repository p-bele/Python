#ask user's age and check it.
#is.digit() ελέγχει ένα string και σου επιστρέφει True αν το κείμενο περιέχει μόνο ψηφία/αριθμούς

underage=0
adult=0

while True:
  age = input("give me your age: ")
  if len(age) == 0:
    print("please type something")
    continue
  elif age.lower()== "stop":
    break

  if not age.isdigit():
    print("give a number")
    continue

  age = int(age)

  if age > 120 or age < 0:
      print("not realistic...")
      continue
  elif age < 18:
      underage += 1
      print(f"age={age}, category: underage")
  else:
      adult += 1
      print(f"age={age}, category: adult")

print(f"underage: {underage}")
print(f"adults: {adult}")

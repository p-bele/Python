# ATM validation checks

pin = "1234"

while True:
  user = input("enter your password ")      # input returns always a string value

  if len(user)==0:
    print("type something ")
    continue
  elif not user.isdigit():
    print("only numbers")
    continue

  if user != pin:
    print("incorrect pin, try again ")
  else:
    print("welcome to your account ")
    break

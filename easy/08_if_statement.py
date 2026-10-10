age = int(input("how old are you? "))

if age>=18:
  print("you can vote")
elif age>=13:
  print("teenager, you can vote in " + str(18-age) + " years")   #cast age to string to concat with text
else:
  print("kid, drink your milk...")

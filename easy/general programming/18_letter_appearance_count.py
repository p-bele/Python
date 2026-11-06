# in the sentence "good morning beautiful little baby" find how many letters (including spaces )
# are before the first 'e'

text = "good morning beautiful little baby"
counter = 0

for i in text:
  counter +=1
  if i=="e":
    break

print(f"there are {counter} letters before 'e'")

#now count only the letters, do not include the spaces
counter = 0
counter_spaces = 0

for i in text:
  if i==" ":
    counter_spaces +=1
    continue
  else:
    counter +=1

  if i =="e":
    break

print(f"there are {counter} letters before 'e'")
print(f"there are {counter_spaces} spaces")



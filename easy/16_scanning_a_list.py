#scanning a string

for letter in "Panos":
  print(letter)


for letter in "Panos":
  print(letter)
  if letter=="n":
    break

#scanning a list

friends = ["Nick", "Helen", "John"]

for i in friends:
  print(f"Hello {i}")


# problem: search in a text how many times there is the letter "o"

text = "Good morning"
counter = 0

for letter in text:
  if letter =="o":
    counter +=1

print(f"the letter 'o' appeared {counter} times")

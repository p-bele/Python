universities = {
    "Netherlands": ["Utrecht", "UvA", "Tilburg", "Leiden"],
    "Greece": ["UniPi", "Kapodestrian", "Panteion", "AUEB"]
}

user_choice = input("what country do you want? ")

if user_choice in universities.keys():
  print(universities[user_choice])
  print(f"number of universities: {len(universities[user_choice])}")
else:
  print("no such country in our list")
  print("here is our list of countries")
  for i in universities:  #looks the keys
    print(i)

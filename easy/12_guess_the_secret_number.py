secret_number = 7

guess = int(input("guess your number, between 1 and 10: "))
tries = 1

while guess!=secret_number:
  guess = int(input("try again, try another number between 1 and 10: "))
  tries +=1

print(f"congrats, you found the magic number after {tries} tries")

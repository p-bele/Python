secret_number = 7  #this is the defined secret number

guess = int(input("guess your number, between 1 and 10: "))  #the user starts guessing till he finds the secret  number
tries = 1

while guess!=secret_number:
  guess = int(input("try again, try another number between 1 and 10: "))
  tries +=1   #counter for the number of tries 

print(f"congrats, you found the magic number after {tries} tries")

secret_number = 7

while True:                            # Τρέχει ασταμάτητα
    guess = int(input("Μάντεψε: "))

    if guess == secret_number:
       print("Το βρήκες!")
       break                    # <--- Σπάει τη while ΑΜΕΣΩΣ και βγαίνει έξω!
    else:
      print("Λάθος, πάμε ξανά...")


x=0

while x<5:
  x +=1

  if x == 3:    # <--- Μόλις το x γίνει 3, πηδάει αμέσως στην κορυφή!
    continue    # Η print(x) από κάτω ΔΕΝ θα εκτελεστεί για το 3.
  else:
    print(x)



# pass, λειτουργεί σαν placeholder (κενή εντολή), συνεχίζεται ο κώδικας κανονικά

x = 0
while x < 10:
    x += 1
    if x == 5:
        # Ξέρω ότι στο 5 θέλω να κάνω κάτι ειδικό, αλλά δεν το έχω σκεφτεί ακόμα!
        pass
    else:
      print(x)

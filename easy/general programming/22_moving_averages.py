daily_sales = [120, 150, 180, 200, 170, 210, 230]

moving_averages = []
total_sum = 0
b = 0
e = 3

for i in range(5): # Χρησιμοποιούμε το 'i' για τις 5 επαναλήψεις
    my_slice = slice(b, e)

    # Κάνουμε το slice πάνω στη daily_sales!
    # Το x θα πάρει με τη σειρά τους 3 αριθμούς του τρέχοντος μπλοκ
    for x in daily_sales[my_slice]:
        total_sum = total_sum + x

    # Χρησιμοποιούμε το total_sum που υπολογίσαμε παραπάνω
    moving_averages.append(round(total_sum / 3, 2))

    b += 1
    e += 1
    total_sum = 0 # Μηδενισμός για το επόμενο μπλοκ

print(f"the list is {moving_averages}")
# Έξοδος: [150.0, 176.67, 183.33, 193.33, 203.33]

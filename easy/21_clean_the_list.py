#clean the following list

customer_ids = [101, 102, -5, 101, 103, 0, 104, 102, 105, -10, 101]

clean_ids = []

for id in customer_ids:
  if id>0 and id not in clean_ids:    # to avoid duplicates
    clean_ids.append(id)

clean_ids.sort()

print(f"the clean list is {clean_ids} and the number of values is {len(clean_ids)}")

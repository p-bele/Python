problem: slice the full name into two variables using string slicing


full_name = "pink floyd"

first_name = full_name[:4]    #[start:stop:step]
last_name = full_name[5:]

print(f"first_name = {first_name.capitalize()}")   #capitalize() to cap the first letter 
print(f"last_name = {last_name.capitalize()}")

has_driver_license = True
is_sober = True

if has_driver_license and is_sober:     --if has_driver==True and is_sober==True
  print("you can drive")
else:
  print("you cannot drive")



has_driver_license = True
is_drunk = False

if has_driver_license and not is_drunk:     # not reverses the boolean
  print("you can drive")                    # (True and True)== True, so the first if runs
else:
  print("you cannot drive")

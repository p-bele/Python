url1 = "http://google.com"
url2 = "http://facebook.com"
url3 = "http://wikipedia.com"

print(url1[7:-4])
print(url2[7:-4])
print(url3[7:-4])


my_slice = slice(7, -4)    # for reusing the same slice

print(url1[my_slice])
print(url2[my_slice])
print(url3[my_slice])

### too many values to unpack


name, email, *_ = ("dave", "email", "resto", "resto") # unpacking the rest

print(name, email)

*trailing, current = [10, 22, 33, 9, 10, 3]

print(current) # out: 3
print(trailing) # out: [10,22,33,9,10]

####

record = ("Rfael", 55, 122.3, (12, 18, 2021))
name, *_, (*_, year) = record
print(name, year)
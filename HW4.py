
last_name: str
first_name: str
country: str
city_address: str
zipcode: str

last_name = input('enter last name: ')
while True:
    if last_name.isupper() and last_name.isalpha():
        break
    last_name = input('enter last name in uppercase: ')

first_name = input('enter first name: ')
while True:
    if first_name.islower() and first_name.isalpha():
        break
    first_name = input('enter first name in lowercase: ')

country = input('enter country: ')
while True:
    if len(country) <= 3 and country.isalpha() and country.isupper():
        break
    country = input('enter no more than 3 upper cased letters: ')

city_address = input('enter city address: ')

zipcode = input('enter zipcode: ')
while True:
    if zipcode.isdigit() and len(zipcode) >= 4:
        break
    zipcode = input('enter at least 4 numbers')

print(f"FOR: {last_name}, {first_name}\n"
      f"COUNTRY: {country}\n"
      f"ADDRESS: {city_address}\n"
      f"ZIPCODE: {zipcode}")
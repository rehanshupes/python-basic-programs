import  numbers
from   numbers  import geocoder
phone_number1 = numbers.parse("+917427824417")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, ))

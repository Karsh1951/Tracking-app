#import the required modules
import phonenumbers
from phonenumbers import geocoder,carrier,timezone
number = input("Enter the phone number to search the location: ")
phone_numbers = phonenumbers.parse(number)
print(f"location: {geocoder.description_for_number(phone_numbers,'en')}")
print(f"Carrier: {carrier.name_for_number(phone_numbers,'en')}")
print(f"Time Zone: {timezone.time_zones_for_number(phone_numbers)}")

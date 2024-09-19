import phonenumbers
from phonenumbers import geocoder

# Parse the phone number (E.164 format preferred, like "+14155552671")
phone_number = phonenumbers.parse("+233501424889")

# Get the geographical location of the phone number
location = geocoder.description_for_number(phone_number, 'en')  # 'en' is for English

print(f"Location: {location}")


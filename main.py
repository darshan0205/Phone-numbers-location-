import phonenumbers
from num import a

from phonenumbers import geocoder
ch_number = phonenumbers.parse(a, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(a, "ds")
print(carrier.name_for_number(service_number, "en"))

#!/usr/bin/python3

import sys, phonenumbers # pip install phonenumbers
from phonenumbers import carrier, geocoder, timezone

def phone_study(phone_number):
    data = {}

    phone_number = phonenumbers.parse(phone_number)
    # get timezone a phone number
    data['Timezone'] = timezone.time_zones_for_number(phone_number)
    # get carrier of a number
    data['Carrier'] = carrier.name_for_number(phone_number, "en")
    # get region information
    data['Region'] = geocoder.description_for_number(phone_number, "en")
    # validate
    data['Validate'] = phonenumbers.is_valid_number(phone_number)
    # check possibility of a number
    data['Posibility'] = phonenumbers.is_possible_number(phone_number)
    
    return data


if __name__ == '__main__':
    phone_number = sys.argv[1]
    try:
        for k, v in phone_study(phone_number).items():
            print('[*]', k, '\t=', v)
    except:
        pass

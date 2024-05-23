import re
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from django.core.exceptions import ValidationError

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


# to'g'irlashilar kerak!

def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        return "email"

    try:
        phone_number = phonenumbers.parse(email_or_phone)
        if phonenumbers.is_valid_number(phone_number):
            return 'phone'
        else:
            raise ValidationError({
                "success": False,
                "message": "Telefon raqamingiz notogri"
            })
    except NumberParseException:
        raise ValidationError({
            "success": False,
            "message": "Email yoki telefon raqamingiz notogri"
        })

import re


phone_numbers = [
     "    +38(050)123-32-34",
     "     0503451234",
     "(050)8889900",
     "38050-111-22-22",
     "38050 111 22 11   "
 ]

def normalize_and_add_country_code(phone_numbers, country_code="+380"):
    pattern = r"[^\d+]"
    prefixes = ["+380", "380", "80", "0"]
    normalized_phones = []
    
    for phone in phone_numbers:
        phone = re.sub(pattern, "", phone)
        for prefix in prefixes:
            if phone.startswith(prefix):
                phone = phone.removeprefix(prefix)
                break
        normalized_phones.append(country_code + phone)
    
    return normalized_phones

# Виклик функції
phones_with_country_code = normalize_and_add_country_code(phone_numbers)
print(phones_with_country_code)



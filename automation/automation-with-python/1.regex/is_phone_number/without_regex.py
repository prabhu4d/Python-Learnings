def is_phone_number(text):
    def check_decimal(start, end):
        for i in range(start, end):
            if not text[i].isdecimal():
                return False
        return True

    def check_hyphen(index):
        if text[index] != "-":
            return False
        return True

    if len(text) != 12:
        return False
    if not check_decimal(0, 3):
        return False
    if not check_hyphen(3):
        return False
    if not check_decimal(4, 7):
        return False
    if not check_hyphen(7):
        return False
    if not check_decimal(8, 12):
        return False
    return True


print("415-555-4242 is a phone number:")
print(is_phone_number("415-555-4242"))
print("Moshi moshi is a phone number:")
print(is_phone_number("Moshi moshi"))

## Find Phone number in the message
message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i : i + 12]
    if is_phone_number(chunk):
        print("Phone number found: " + chunk)
print("Done")

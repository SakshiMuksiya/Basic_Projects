"""An IBAN-compliant account number consists of:

a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country"""

# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():  # check if the IBAN contains only letters and digits
    print("You have entered invalid characters.")
elif len(iban) < 15:  # shortest IBAN is 15 characters long (Norway)
    print("IBAN entered is too short.")
elif len(iban) > 31:  # longest IBAN is 31 characters long (Malta)
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()   # move the first four characters to the end of the string and convert to uppercase
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A')) # convert letters to numbers (A=10, B=11, ..., Z=35)
    iban = int(iban2)
    if iban % 97 == 1:  # valid IBANs give a remainder of 1 when divided by 97
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

# sample IBAN: DE89 3704 0044 0532 0130 00
# sample IBAN: GB82 WEST 1234 5698 7654 32
# sample IBAN: FR14 2004 1010 0505 0001 3M02 606
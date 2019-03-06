import re


for _ in range(int(input())):
    cc_number = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", cc_number) and not re.search(r"([\d])\1\1\1", cc_number.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")

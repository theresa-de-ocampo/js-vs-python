# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

import re

phone_number = input("Phone Number: ").strip()
digits = re.findall(r"\d+", phone_number)

if len(digits) > 0:
    stripped = "".join(digits)
    if len(stripped) == 10:
        area_code = stripped[:3]
        office_code = stripped[3:7]
        line_number = stripped[7:]
        print(f"We'll contact you at ({area_code}) {office_code}-{line_number}")
    else:
        print("Please enter exactly 10 digits.")

'''
Q4: Write a Python function to validate the Regular Expression for the following:-
    a) Email Address
    b) Mobile numbers of Bangaladesh
    c) Telephone numbers of USA
    d) 16 character Alpha-Numeric password composed of alphabets of Uppercase,
       Lowercase,Special Characters,Numbers.
'''

'''
Input:
    a) Email Address
    b) Mobile numbers of Bangaladesh
    c) Telephone numbers of USA
    d) 16 character Alpha-Numeric password composed of alphabets of Uppercase,
       Lowercase,Special Characters,Numbers.

       
logic = 
1. Import re module
2. MyRegex class with mthods to validate
    a) Email Address
    b) Mobile numbers of Bangaladesh
    c) Telephone numbers of USA
    d) 16 character Alpha-Numeric password composed of alphabets of Uppercase,
       Lowercase,Special Characters,Numbers.

Output:
Validated :
    a) Email Address
    b) Mobile numbers of Bangaladesh
    c) Telephone numbers of USA
    d) 16 character Alpha-Numeric password composed of alphabets of Uppercase,
       Lowercase,Special Characters,Numbers.
  '''

# import re module
import re

# MyRegex class
class MyRegex:
    def __init__(self,email_address, mobile_number_of_Bangladesh, telephone_number_of_USA, password_16_char):
        self.email_address = email_address
        self.mobile_number_of_Bangladesh = mobile_number_of_Bangladesh
        self.telephone_number_of_USA = telephone_number_of_USA
        self.password_16_char = password_16_char

    # Method to validate email address
    def validate_email_address(self):
        pattern = r"^[a-z0-9_.]+@[a-z]+\.[a-z]{3}"

        if re.match(pattern, self.email_address):
            print(f"\n{self.email_address} is valid Email Address")
        else:
            print(f"\n{self.email_address} is invalid Email Address")

    # Method to validate mobile_number_of_Bangladesh
    def validate_mobile_number_of_Bangladesh(self):
        pattern = r"^(?:\+880)?01[3-9]\d{8}|(?:\+1)?\(?\d{3}\)?[ .-]?\d{4}$"

        if re.match(pattern, self.mobile_number_of_Bangladesh):
            print(f"\nThis mobile number {self.mobile_number_of_Bangladesh} belogs to bangladesh")
        else:
            print(f"\nThis mobile number {self.mobile_number_of_Bangladesh} does not belogs to bangladesh")

    # Method to validate telephone_number_of_USA
    def validate_telephone_number_of_USA(self):
        pattern = r"^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$"

        if re.match(pattern, self.telephone_number_of_USA):
            print(f"\nThis telephone number {self.telephone_number_of_USA} belogs to USA")
        else:
            print(f"\nThis telephone number {self.telephone_number_of_USA} does not belogs to USA")

    # Method to validate 16 character Alpha Numberic password with special characters
    def validate_password_16_char(self):
        pattern = r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*[A-Z])(?=.*[-\#\$\.\%\&\*])(?=.*[a-zA-Z]).{8,16}$"

        if re.match(pattern, self.password_16_char):
            print("\nCongratulations! Valid Password")
        else:
            print("\nPassword must have 16 characters and contain at least 1 UPPERCASE, 1 lower case, 1 number, 1 special character\n")

# Creating Object
regex = MyRegex("WhoCares@gmail.com", "01672598624", "(123) 123-1234", "Guvi@geeks2")

# Function Call
regex.validate_email_address()
regex.validate_mobile_number_of_Bangladesh()
regex.validate_telephone_number_of_USA()
regex.validate_password_16_char()
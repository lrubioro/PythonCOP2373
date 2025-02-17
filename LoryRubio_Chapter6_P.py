# Lory Rubio Programming Assignment 6
# This code has functions to validate phone numbers, social security numbers and zip codes using regular expressions.
# The main function gets input from a user and then displays if the phone number, social security number and zip code they entered is valid.

# Import the module for re
import re

# create function to validate phone numbers, checks input for the correct format
# this accepts formats with parantheses dashes spaces  or with no seperators
def phonenumb_validation (phone):
    pattern = r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$'
    return re.match(pattern,phone) is not None

# create one to validate the social security, regex and check if it matches
# this accepts formats with the common dashes as seperators
def ssn_validation(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None

# validate the zipcodes regex and check if it matches
# accepts 5 digits zipcodes
def zipcode_validate(zipcode):
    pattern= r'^\d{5}$'
    return re.match(pattern, zipcode) is not None

# create main function to ask for use input and displays results
def main():
    phone = input("Please enter a phone number: ")
    ssn = input("Please enter a Social Security Number (SSN): ")
    zip_code = input("Please enter a zip code: ")

    # Validate and display results
    print(f"Phone number '{phone}' is {'valid' if phonenumb_validation(phone) else 'invalid'}.")
    print(f"SSN '{ssn}' is {'valid' if ssn_validation(ssn) else 'invalid'}.")
    print(f"Zip code '{zip_code}' is {'valid' if zipcode_validate(zip_code) else 'invalid'}.")

# Run the main function
if __name__ == "__main__":
    main()
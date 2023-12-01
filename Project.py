#QAP 4
#Prepared by Maryam Shaheen
# Python Lists and functions

import datetime

# Default values
next_policy_number = 1944
basic_premium = 869.00
discount_for_additional_cars = 0.25
cost_of_extra_liability_coverage = 130.00
cost_of_glass_coverage = 86.00
cost_for_loaner_car_coverage = 58.00
hst_rate = 0.15
processing_fee_monthly_payments = 39.99

# Lists to store customer information
policy_numbers = []
first_names = []
last_names = []
addresses = []
cities = []
provinces = []
postal_codes = []
phone_numbers = []
num_cars = []
extra_liability_options = []
glass_coverage_options = []
loaner_car_options = []
payment_methods = []
down_payments = []
claim_dates = []
claim_amounts = []

#function to get province
def get_province():
    provinces = ["ON", "BC", "AB", "MB", "SK", "QC", "NB", "NL", "NS", "PE", "NT", "NU", "YT"] 
    province = input("Enter the province (ON, BC, AB, MB, SK, QC, NB, NL, NS, PE, NT, NU, YT): ").upper()

#Validates the entered province against a predefined list of valid provinces.   
    while province not in provinces:
        print("Invalid province. Please enter a valid province.")
        province = input("Enter the province (ON, BC, AB, MB, SK, QC, NB, NL, NS, PE, NT, NU, YT): ").upper()
    return province

# Function to get yes/no input
def get_yes_no_input(prompt):
    user_input = input(prompt).upper()
    while user_input not in ["Y", "N"]:
        print("Invalid input. Please enter Y or N.")
        user_input = input(prompt).upper()
    return user_input

# Function to get payment method
def get_payment_method():
    payment_methods = ["FULL", "MONTHLY", "DOWN PAY"]
    payment_method = input("Enter payment method (FULL, MONTHLY, DOWN PAY): ").upper()
    while payment_method not in payment_methods:
        print("Invalid payment method. Please enter FULL, MONTHLY, or DOWN PAY.")
        payment_method = input("Enter payment method (FULL, MONTHLY, DOWN PAY): ").upper()
    return payment_method

# Function to get customer information
def get_customer_information():
    global next_policy_number  # Declare next_policy_number as global

    # Get customer information
    first_name = input("Enter first name: ").title()
    last_name = input("Enter last name: ").title()
    address = input("Enter address: ")
    city = input("Enter city: ").title()
    province = get_province()
    postal_code = input("Enter postal code: ")
    phone_number = input("Enter phone number: ")

    # Get insurance details
    num_car = int(input("Enter the number of cars being insured: "))
    extra_liability = get_yes_no_input("Extra liability coverage? (Y/N): ")
    glass_coverage = get_yes_no_input("Glass coverage? (Y/N): ")
    loaner_car = get_yes_no_input("Loaner car coverage? (Y/N): ")
    payment_method = get_payment_method()

    # If payment method is DOWN PAY, get down payment amount
    down_payment = 0.0
    if payment_method == "DOWN PAY":
        down_payment = float(input("Enter down payment amount: "))

    # Store customer information in lists
    policy_numbers.append(next_policy_number)
    first_names.append(first_name)
    last_names.append(last_name)
    addresses.append(address)
    cities.append(city)
    provinces.append(province)
    postal_codes.append(postal_code)
    phone_numbers.append(phone_number)
    num_cars.append(num_car)
    extra_liability_options.append(extra_liability)
    glass_coverage_options.append(glass_coverage)
    loaner_car_options.append(loaner_car)
    payment_methods.append(payment_method)
    down_payments.append(down_payment)

    # Increment the next policy number for the next customer
    next_policy_number += 1

def calculate_premium(index):
    # Calculate total premium
    total_premium = basic_premium * (1 + (num_cars[index] - 1) * discount_for_additional_cars)

    # Calculate total extra costs
    total_extra_costs = 0.0
    if extra_liability_options[index] == "Y":
        total_extra_costs += cost_of_extra_liability_coverage * num_cars[index]
    if glass_coverage_options[index] == "Y":
        total_extra_costs += cost_of_glass_coverage * num_cars[index]
    if loaner_car_options[index] == "Y":
        total_extra_costs += cost_for_loaner_car_coverage * num_cars[index]

    # Calculate total insurance premium
    total_insurance_premium = total_premium + total_extra_costs

    # Calculate HST
    hst = total_insurance_premium * hst_rate

    # Calculate total cost
    total_cost = total_insurance_premium + hst

    # If payment method is MONTHLY or DOWN PAY, calculate monthly payment
    if payment_methods[index] in ["MONTHLY", "DOWN PAY"]:
        monthly_payment = (total_cost - down_payments[index]) / 8 + processing_fee_monthly_payments
    else:
        monthly_payment = 0.0

    return total_insurance_premium, hst, total_cost, monthly_payment

# Function to display customer receipt

def display_receipt(index):
    # Display customer information
    print("\nReceipt for Customer:", first_names[index], last_names[index])
    print("Policy Number:", policy_numbers[index])
    print("Address:", addresses[index])
    print("City:", cities[index])
    print("Province:", provinces[index])
    print("Postal Code:", postal_codes[index])
    print("Phone Number:", phone_numbers[index])

    # Display insurance details
    print("\nInsurance Details:")
    print("Number of Cars:", num_cars[index])
    print("Extra Liability Coverage:", extra_liability_options[index])
    print("Glass Coverage:", glass_coverage_options[index])
    print("Loaner Car Coverage:", loaner_car_options[index])
    print("Payment Method:", payment_methods[index])
    if payment_methods[index] == "DOWN PAY":
        print("Down Payment:", "${:,.2f}".format(down_payments[index]))

    # Calculate and display premium details
    total_premium, hst, total_cost, monthly_payment = calculate_premium(index)
    print("\nPremium Details:")
    print("Basic Premium: ${:,.2f}".format(basic_premium))
    print("Discount for Additional Cars: ${:,.2f}".format(total_premium - basic_premium))
    print("Total Premium: ${:,.2f}".format(total_premium))
    print("Total Extra Costs: ${:,.2f}".format(total_cost - total_premium - hst))
    print("HST ({}%): ${:,.2f}".format(hst_rate * 100, hst))
    print("Total Cost: ${:,.2f}".format(total_cost))

    # Display payment details
    if payment_methods[index] in ["MONTHLY", "DOWN PAY"]:
        print("\nPayment Details:")
        print("Monthly Payment (8 months): ${:,.2f}".format(monthly_payment))
        print("Invoice Date:", datetime.date.today())
        print("First Payment Date:", datetime.date.today().replace(day=1) + datetime.timedelta(days=32))

    # Display previous claims
    if claim_dates:
        print("\nPrevious Claims:")
        print("Claim\t#Claim Date\tAmount")
        print("-" * 45)
        for i in range(len(claim_dates)):
            print(f"{i+1}.  {claim_dates[i]}\t${claim_amounts[i]:,.2f}")

# Main loop to allow entering multiple customers
while True:
    get_customer_information()

    # Add at least 2-3 claims for the customer
    for _ in range(2):
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: $"))
        claim_dates.append(claim_date)
        claim_amounts.append(claim_amount)

    display_receipt(len(policy_numbers) - 1)

    # Ask if the user wants to enter another customer
    another_customer = input("Do you want to enter another customer? (Y/N): ").upper()
    if another_customer != "Y":
        break

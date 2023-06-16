from tabulate import tabulate

FED_TAX = 0.10
STATE_TAX = 0.06
FICA = 0.03
NORMAL_HRS = 40
MAX_HRS = 168   #24*7=168
OVERTIME_PAY = 1.5

#Calculate the pay for an employee based on the hours worked and hourly rate
def calculate_pay(emp_name, rate, hrs):
    if hrs > NORMAL_HRS:
        otpay = float((hrs - NORMAL_HRS) * (rate * OVERTIME_PAY))
        regpay = float(rate * hrs)
        grosspay = round(float(otpay + regpay), 2)
        fedtax = round((grosspay * FED_TAX), 2)
        statetax = round((grosspay * STATE_TAX), 2)
        fica = round((grosspay * FICA), 2)
        netpay = round((grosspay - (fedtax + statetax + fica)), 2)
    else:
        otpay = float(0.0)
        regpay = float(rate * hrs)
        grosspay = round((otpay + regpay), 2)
        fedtax = round((grosspay * FED_TAX), 2)
        statetax = round((grosspay * STATE_TAX), 2)
        fica = round((grosspay * FICA), 2)
        netpay = round((grosspay - (fedtax + statetax + fica)), 2)

    # # Store all the pay-related data in a list
    res = emp_name, rate, hrs, regpay, otpay, grosspay, fedtax, statetax, fica, netpay

    return res

def main():
    emp_list = []
    
    company = input("Enter your company name: ")
    company = company.upper()
    print("Welcome to payroll system of", company)
    
    while True:  # accept only numbers  and no blank allowed
        employees = input("How many employees do you have in your company? ").strip()
        if employees.strip() == '':
            print("Value has to be entered")

            continue
        if not employees.isnumeric():
            print("Only numbers are allowed.")

            continue
        if employees == '0':
            print("Invalid input. Enter a value greater than zero")
            continue
        
        else:
            break

    employees = int(employees)
    print(" ")
    i = 1
    entered_names = []
    while i < (employees + 1):
        while True:  # accept only letters and no blank allowed
            emp_name = input("Enter Employee Name: ")
            if emp_name == '':
                print("Value has to be entered")

                continue
            if not emp_name.isalpha():
                print("Only letters are allowed.")

                continue
            
            if emp_name in entered_names:   #to avoid duplicates
                print("This employee already exists. Please enter another name")
                continue
            
            else:
                entered_names.append(emp_name)
                break

        while True:  # value needs to be entered and can't be negative
            try:
                rate = float(input("Enter pay rate per hour: "))
            except ValueError:
                print("Please enter a value")
                continue
            if rate <= 0:
                print("Zero and Negative value not allowed")
                continue
            else:
                break

        while True:  # value needs to be entered and can't be negative

            try:
                hrs = float(input("Enter the number of hours worked for the week: "))
            except ValueError:
                print("Please enter a value")
                continue
            if hrs < 0:
                print("Negative value not allowed")
                continue
            elif hrs > MAX_HRS:  
                print("24 hours * 7 days = 168 hours.So you cannot work more than 168 hours in a week. Enter a value between 1 and 168")
            else:
                break
        print(" ")
        
        #Calculate and store the pay related data of the employee
        res = calculate_pay(emp_name, rate, hrs)
        emp_list.append(res)

        i += 1

    # making table and headers

    mydata = emp_list
    head = ["Employee Name", "Pay Rate($)", "Hours Worked(hrs)", "Regular Pay($)", "OT Pay($)", "Gross Pay($)",
            "Fed Tax($)", "State Tax($)", "FICA($)", "Net Pay($)"]

    # print table
    print(tabulate(mydata, headers=head, tablefmt="fancy_grid", showindex=range(1, employees+1)))



if __name__ == "__main__":
    main()

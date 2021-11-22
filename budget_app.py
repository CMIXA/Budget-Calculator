import matplotlib.pyplot as plt

#This function will be the menu display of the program
def menu_display():
    
    print("*** MENU ***")
    print("\n(B) Budget Calculator")
    print("\n($) Income Calculator *after taxes*")
    print("\n(I) Info")
    print("\n(Q) Quit")
    print("\n*****************************************")
    print("*****************************************")


#Income Calculator Function

def actual_income():
    
    #Requires User to enter pay and hours weekly or salary
    
    print('')
    income = input("Please select the mode to calculate your actual income:\n**(1)** pay/hours per week\n**(2)** Bi-Weekly Salary\n**(3)** Annual Salary\n-> ")

#------------------------------------------------------------------------
#This loop makes sure the user inputs "1" or "2" in order to calculate the users income 
#Input "1" calculates the user's income by hourly pay and hours per week
#Input "2" calculates the user's income from Bi-Weekly salary
#Input "3" calculates the user's income from annual salary


    while True:
    
        if income == "1":
            print('')
            print("Please enter your hourly pay and hours per week:")

            pay = int(input("Hour pay: $"))

            hours = int(input("Hours per week: "))

            gross_annual_income = (pay * hours) * 56

            break

        elif income == "2":
            print('')

            bi_weekly = int(input("Please enter your bi-weekly salary: $"))

            gross_annual_income = bi_weekly * 28

            break

        elif income == "3":
            print('')

            gross_annual_income = int(input("Please enter your annual salary: $"))

            break

        else:
            income = input("Invalid choice: Please select:\n**(1)** pay/hours per week\n**(2)** Bi-Weekly Salary\n**(3)** Annual Salary\n-> ")

            continue  

#Requires User to enter their marital status
   
    print('')
    marital_status = input("Please enter your marital status:\n**(S)** Single\n**(M)** Married\n-> ").upper()

    
    while True:
        if marital_status == "S":    
            if gross_annual_income <= 9950:
                tax = 0.10
            elif gross_annual_income > 9950 and gross_annual_income <= 40525:
                tax = 0.12
            elif gross_annual_income > 40525 and gross_annual_income <= 86375:
                tax = 0.22
            elif gross_annual_income > 86375 and gross_annual_income <= 164925:
                tax = 0.24
            elif gross_annual_income > 164925 and gross_annual_income <= 209425:
                tax = 0.32
            elif gross_annual_income > 209425 and gross_annual_income <= 518400:
                tax = 0.35
            elif gross_annual_income > 518400:
                tax = 0.37    
            break
            
        elif marital_status == "M":
            if gross_annual_income <= 19900:
                tax = 0.10
            elif gross_annual_income > 19900 and gross_annual_income <= 81050:
                tax = 0.12
            elif gross_annual_income > 81050 and gross_annual_income <= 172750:
                tax = 0.22
            elif gross_annual_income > 172750 and gross_annual_income <= 329850:
                tax = 0.24
            elif gross_annual_income > 329850 and gross_annual_income <= 418850:
                tax = 0.32
            elif gross_annual_income > 418850 and gross_annual_income <= 628300:
                tax = 0.35
            elif gross_annual_income > 628300:
                tax = 0.37    
            break
   

        elif marital_status != "S" or marital_status != "M":
        #else:
            marital_status = input("Invalid choice: please enter your marital status:\n**(S)** Single\n**(M)** Married\n-> ").upper() 
            continue   

#------------------------------------------------------------------------
#This section of code runs a while loop to ensure the user inputs the correct input (S) or (M) for mariatl status
#When the user inputs (S) or (M), they will tax their income by the corresponding tax brackets
#REFERENCE - Tax Bracket from https://www.johndaviscpa.com/taxrates2.php
   
    
    global monthly_income
    global annual_income
    global weekly_income
    taxed_income = int(gross_annual_income) * tax 
    annual_income = int(gross_annual_income) - taxed_income
    weekly_income = annual_income / 56
    monthly_income = annual_income / 12
    
    print("Your actual income per year, month, and week is:")
    print('')
    print("**Income BEFORE taxes**")
    print(f"Gross annual income: ${gross_annual_income}")
    print('')
    print("**Income AFTER taxes**")
    print(f"Annual income: ${int(annual_income)}")
    print(f"Monthly income: ${int(monthly_income)}")
    print(f"Weekly income: ${int(weekly_income)}")
    print("\n*****************************************")
    print("*****************************************")


#This is the initial interface for the program
print('')
print("* Welcome to the Budget App! *")
print('')

#Requires User to press enter to start the program
input("Please press *Enter* to start! ")
print('')

#Displays Menu
menu_display()


#--------------------------MENU CHOICES-----------------------------------
#Will begin the process of the budget calculator

while True:
    
    menu_choice = input("\nPlease chose an option from the Menu: ").upper()
    print("\n*****************************************")
    print("*****************************************")

#--------------------BUDGET CALCULATOR-----------------------
   
    if menu_choice == "B":
        
        print("\n***Budget Calculator***")
        print("\n\n* The list below will calculate your budget based off your income and expenses *")
        print("\n*INCOME*\n*RENT or MORTGAGE*\n*UTILITIES*\n*INSURANCE*\n*GROCERIES*\n*OTHER*")

        actual_income()
        
        #----------------- RENT/MORTGAGE -----------------
        
        rent = int(input("\nPlease enter your monthly *Rent or Mortgage*: $"))
        
        #----------------- UTILITY EXPENSES -----------------
        
        utilities = int(input("\nPlease enter your monthly *Utility* expesnse: $"))
        
        #----------------- GROCERY EXPENSES -----------------
        
        groceries = int(input("\nPlease enter your monthly *Grocery* expenses: $"))
        
        #----------------- OTHER EXPENSES -----------------
        
        other = int(input("\nPlease enter your monthly *Miscellaneous* expenses: $"))
        
        #----------------- DISPOSABLE INCOME CALCULATOR -----------------
        
        expenses = groceries + rent + utilities + other
        monthly_disposable_income = monthly_income - expenses
            
        print(f"\n**Your monthly expenses are: ${expenses}")
        
        #-------------------------------------------------------
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Rent/Mortgage', 'Utilities', 'Groceries', 'Other'
        sizes = [rent, utilities, groceries, other]
        explode = (0.1, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Rent/Mortgage')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()
        #------------------------------------------------------
        
        print(f"\n**Your monthly disposable income is: ${int(monthly_disposable_income)}")
        
        if expenses > monthly_disposable_income:
            print("\nOh no! You need to spend less!")
        if expenses < monthly_disposable_income:
            print("\nYou've got money to spend!")
        
        
        print("\n*****************************************")
        print("*****************************************")
        
        #Maybe implement a system where dependng on the percentage of money left over from income and expenses, print a different message
        #FOR EXAMPLE if MDI = x% of AMI print "x"
        
         
        continue

#--------------------INCOME CALCULATOR--------------------- 
   
    elif menu_choice == "$":
        
        print("\n***Income Calculator***\n")
        actual_income()
        
        continue 

#--------------------------INFO------------------------------
#Provides a detailed list of how the budget calculator will calculate the users disposable income
#Provides a detailed list of how the income calculator will calculate the users income after taxes
    
    if menu_choice == "I":
        print("\n******* INFO *******")
        print("\n****BUDGET CALCULATOR****")
        print("\nThe Budget Calculator calculates the your disposable income by intaking:")
        print("\n - Anual, Weekly or Bi-Weekly Income")
        print("\n - Monthly Rent or Mortgage Expenses")
        print("\n - Monthly Insurance expenses")
        print("\n - Monthly Grocery Expenses")
        print("\n - Monthly Miscellaneous Expenses")
        print("\n\n****INCOME CALCULATOR****")
        print("\nThe Income Calculator calculates your actual income after federal tax.")
        print("\nThere are three options to calculate your actual income:")
        print("\n - Anual Salary")
        print("\n - Bi-Weekly pay")
        print("\n - Hourly pay + Hours per week")
        print("\nOnce one of the 3 options have been fulfilled, the income calculator will present your income in four different ways:")
        print("\n - Gross Anual Income (before federal taxes)")
        print("\n - Actual Annual Income (after federal taxes)")
        print("\n - Actual Monthly Income (after federal taxes)")
        print("\n - Actual Weekly Income (after federal taxes)")
        print("\n*****************************************")
        print("*****************************************")
        continue 
        
#--------------------------QUIT------------------------------
#QUITS the program
   
    elif menu_choice == "Q":
        
        print("\nYou have exited the Budget App...")
        print("\nSeeya!")
        break
    
    #QUIT the program

#--------------------------ELSE-------------------------------     
    
    else:
        print("\nInvalid: Please choose an option from the Menu")



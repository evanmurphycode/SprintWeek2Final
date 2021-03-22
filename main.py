# Sprint Week 2!

# Author: Evan Murphy & Stephen Menecola

# Date: 03/12/21

import Backpack as BP
from datetime import datetime
CurDate = datetime.now()

ClaimNumber = 0
HST = 0.15
LowPerDiemRate = 85.00
HighPerDiemRate = 100
MileageRate = 0.10
RentalCarRate = 56

# Reads and initialises from Deflt.dat file

file = open('Deflt.dat', 'r')
ClaimNumber = int(file.readline())
HST = float(file.readline())
LowPerDiemRate = int(file.readline())
HighPerDiemRate = int(file.readline())
MileageRate = float(file.readline())
RentalCarRate = int(file.readline())
file.close()


# This function will process salesperson travel claims
def TravelClaim(ClaimNumber):
    while True:
        EmployeeNumber = BP.ValidEmployeeNumber9()
        EmployeeName = input("Enter employee name: ")
        TripLocation = input("Enter location of travel: ")

        # Format the dates to allow them to be subtracted****

        # newdate1 = time.strptime(date1, "%d/%m/%Y") and newdate2 = time.strptime(date2, "%d/%m/%Y")
        StartDatestr = input("Business trip start date (yyyy-mm-dd): ")
        EndDatestr = input("Business trip end date (yyyy-mm-dd): ")
        # formats start & end dates without time, and calculates travel days
        StartDate, EndDate, TotalTravelDays = BP.ProcessDate(StartDatestr, EndDatestr)

        OwnOrRented = input("Was the vehicle owned or rented? (O/R): ")
        TotalKilometers = int(input("Enter the total kilometers travelled: "))

        if TotalTravelDays <= 3:
            PerDiem = TotalTravelDays * 85.00
        else:
            PerDiem = TotalTravelDays * 100.00

        if OwnOrRented.upper() == "O":
            MileageAmount = TotalKilometers * 0.10
        elif OwnOrRented.upper() == "R":
            MileageAmount = TotalTravelDays * 56.00
        else:
            MileageAmount = 0

        ClaimAmount = PerDiem + MileageAmount
        TaxAmount = PerDiem * HST
        ClaimTotal = ClaimAmount + TaxAmount

        # Formatting

        #PerDiemStr = "${:,.2f}".format(PerDiem)
        #MileageAmountStr = "${:,.2f}".format(MileageAmount)
        #ClaimAmountStr = "${:,.2f}".format(ClaimAmount)
        TaxAmountStr = "${:,.2f}".format(TaxAmount)
        ClaimTotalStr = "${:,.2f}".format(ClaimTotal)


        # Printing results

        print()
        print("             NL Chocolate Company - Travel Claim")
        print()
        print("*" * 60)
        print()
        print("Employee Number: {}       Employee Name: {:<12}".format(EmployeeNumber, EmployeeName))
        print()
        print("Travel location: {}".format(TripLocation))
        print("Travel Start Date: {}    Travel End Date: {}".format(StartDate, EndDate))
        print()
        print("Total Days Travelled:         {}".format(TotalTravelDays))
        print("Car Status (Owned or Rented): {}".format(OwnOrRented))
        print("Total Kilometers Travelled:   {}".format(TotalKilometers))
        print()
        print("*" * 60)
        print()
        print("Daily Cost:   ${:,.2f}".format(PerDiem))
        print("Mileage Cost: ${:,.2f}".format(MileageAmount))
        print("Claim Amount: ${:,.2f}".format(ClaimAmount))
        print("Tax Amount:   {:<10}".format(TaxAmountStr))
        print("              ----------")
        print("Claim Total:  {:<10}".format(ClaimTotalStr))
        print()
        print("")

        file = open('Claims.dat', 'a')

        file.write("{}, ".format(ClaimNumber))
        file.write("{}, ".format(EmployeeNumber))
        file.write("{}, ".format(EmployeeName))
        file.write("{}, ".format(TripLocation))
        file.write("{}, ".format(StartDate))
        file.write("{}, ".format(EndDate))
        file.write("{}, ".format(TotalTravelDays))
        file.write("{}, ".format(OwnOrRented))
        file.write("{}, ".format(TotalKilometers))
        file.write("{}, ".format(PerDiem))
        file.write("{}, ".format(MileageAmount))
        file.write("{}, ".format(ClaimAmount))
        file.write("{}, ".format(TaxAmount))
        file.write("{}\n".format(ClaimTotal))

        file.close()

        # Increase claim number
        ClaimNumber += 1

        # Updates Deflt.dat with new claim number
        file = open('Deflt.dat', 'w')
        file.write("{}\n".format(str(ClaimNumber)))
        file.write("{}\n".format(str(HST)))
        file.write("{}\n".format(str(LowPerDiemRate)))
        file.write("{}\n".format(str(HighPerDiemRate)))
        file.write("{}\n".format(float(MileageRate)))
        file.write("{}\n".format(int(RentalCarRate)))
        file.close()

        print("Claim processed successfully")
        print()

        Continue = input("Process another data claim? (Enter Y for yes or any other key to end): ")
        if Continue.upper() != "Y":
            break

    Anykey = input("Press any key to continue.")


# This function will allow the user to edit the system default values
def EditDefaultValues():

    # Open the defaults file and read the values into variables
    f = open('Deflt.dat', 'r')
    ClaimNumber = int(f.readline())
    HSTRate = float(f.readline())
    LowPerDiemRate = int(f.readline())
    HighPerDiemRate = int(f.readline())
    MileageRate = float(f.readline())
    RentalCarRate = int(f.readline())
    f.close()

    print("NL Chocolate Company")
    print("Edit Default Values")
    print()
    print("For each value, enter an updated value, ")
    print("or press Enter to keep the existing value.")
    print("Current value is shown in ().")
    print()

    NewClaimNumber = input("Enter the claim number (" + str(ClaimNumber) + "): ")
    if NewClaimNumber == "":
        NewClaimNumber = ClaimNumber

    NewHSTRate = input("Enter the HSTRate (" + str(HSTRate) + "): ")
    if NewHSTRate == "":
        NewHSTRate = HSTRate

    NewLowPerDiemRate = input("Enter the low per diem rate (" + str(LowPerDiemRate) + "): ")
    if NewLowPerDiemRate == "":
        NewLowPerDiemRate = LowPerDiemRate

    NewHighPerDiemRate = input("Enter the high per diem rate (" + str(HighPerDiemRate) + "): ")
    if NewHighPerDiemRate == "":
        NewHighPerDiemRate = HighPerDiemRate

    NewMileageRate = input("Enter the new mileage rate (" + str(MileageRate) + "): ")
    if NewMileageRate == "":
        NewMileageRate = MileageRate

    NewRentalCarRate = input("Enter the rental care rate (" + str(RentalCarRate) + "): ")
    if NewRentalCarRate == "":
        NewRentalCarRate = RentalCarRate

    f = open('Deflt.dat', 'w')
    f.write("{}\n".format(str(NewClaimNumber)))
    f.write("{}\n".format(str(NewHSTRate)))
    f.write("{}\n".format(str(NewLowPerDiemRate)))
    f.write("{}\n".format(str(NewHighPerDiemRate)))
    f.write("{}\n".format(str(NewMileageRate)))
    f.write("{}\n".format(str(NewRentalCarRate)))
    f.close()

    print()
    print("Default values successfully updated")

    Anykey = input("Press any key to continue.")


# This function will allow the user to print a travel report
def PrintTravelReport():
    while True:

        print()
        print("         1         2         3         4         5         6         7         8")
        print("1234567890" * 8)
        print()
        print("                              NL Chocolate Company")
        print()
        print("                    Travel Claims Listing as of {}".format(CurDate.strftime("%m/%d/%Y")))
        print()
        print("Claim    Claim      Salesperson       Claim       Per Diem       Mileage       Claim")
        print("Number   Date          Name          Location      Amount        Amount        Amount")
        print("=" * 86)

        file = open('Claims.dat', 'r')

        ClaimCounter = 0
        PerDiemAccumulator = 0
        MileageAccumulator = 0
        ClaimAmountAccumulator = 0

        for claims in file:
            ClaimList = claims.split(",")
            ClaimNumber = ClaimList[0]
            ClaimDate = ClaimList[4].strip()
            Salesperson = ClaimList[2].strip()
            ClaimLocation = ClaimList[3].strip()
            PerDiemAmount = float(ClaimList[9].strip())
            MileageAmount = float(ClaimList[10].strip())
            ClaimAmount = float(ClaimList[11].strip())

            print("{:<3}   {:<10}   {:<12}      {:<12} ${:,.2f}     ${:,.2f}     ${:,.2f}".format(ClaimNumber, ClaimDate, Salesperson, ClaimLocation, PerDiemAmount, MileageAmount, ClaimAmount))

            ClaimCounter += 1
            PerDiemAccumulator += PerDiemAmount
            MileageAccumulator += MileageAmount
            ClaimAmountAccumulator += ClaimAmount


        print("="*86)
        print("{} claims listed                                   ${:,.2f}     ${:,.2f}    ${:,.2f}".format(ClaimCounter, PerDiemAccumulator, MileageAccumulator, ClaimAmountAccumulator))
        print()
        print("                                End of Report")
        file.close()
        break

    Anykey = input("Press any key to continue.")


# This function will allow the user to graph monthly claim totals
def GraphClaimTotals():

    import numpy as np
    import matplotlib.pyplot as plt

    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0

    file = open("Claims.dat", "r")

    for claims in file:
        ClaimList = claims.split(",")
        StartDate = ClaimList[4].strip()
        StartDate2 = StartDate.split('-')
        Month = StartDate2[1]
        ClaimAmount = float(ClaimList[11].strip())
        if Month == "01":
            Jan = Jan + ClaimAmount
        elif Month == "02":
            Feb = Feb + ClaimAmount
        elif Month == "03":
            Mar = Mar + ClaimAmount
        elif Month == "04":
            Apr = Apr + ClaimAmount
        elif Month == "05":
            May = May + ClaimAmount
        elif Month == "06":
            Jun = Jun + ClaimAmount
        elif Month == "07":
            Jul = Jul + ClaimAmount
        elif Month == "08":
            Aug = Aug + ClaimAmount
        elif Month == "09":
            Sep = Sep + ClaimAmount
        elif Month == "10":
            Oct = Oct + ClaimAmount
        elif Month == "11":
            Nov = Nov + ClaimAmount
        elif Month == "12":
            Dec = Dec + ClaimAmount

    XAxis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    YAxis = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

    plt.plot(XAxis, YAxis)

    plt.xlabel('Month')
    plt.ylabel('Claim Amount')

    plt.title('Monthly Claim Totals')
    plt.grid(True)

    plt.show()

    Anykey = input("Press any key to continue.")


def main():
    while True:
        print()
        print("NL Chocolate Company - Travel Claims Processing System")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Edit System Default Values.")
        print("3. Print the Travel Claim Report.")
        print("4. Graph Monthly Claim Totals.")
        print("5. Quit Program.")
        print()
        while True:
            Choice = int(input("Enter choice (1-5): "))
            IsValid = BP.ValidIntegerNumber(Choice, 1, 5)
            if IsValid:
                Choice = int(Choice)
                break
        if Choice == 1:
            TravelClaim(ClaimNumber)
        elif Choice == 2:
            EditDefaultValues()
        elif Choice == 3:
            PrintTravelReport()
        elif Choice == 4:
            GraphClaimTotals()
        else:
            print("Thank you for using NL Chocolate Company's Travel Claim Software!")
            exit(0)


if __name__ == "__main__":
    main()


from datetime import datetime

def ValidText(TextValue):

    IsValid = True
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
    if TextValue == "":
        print("Invalid input - value cannot be blank.")
        IsValid = False
    elif set(TextValue).issubset(allowed_char) == False:
        print("Invalid input - entry contains invalid character.")
        IsValid = False

    return IsValid

def ValidInteger(IntegerValue):

    IsValid = True
    if IntegerValue == "":
        print("Invalid input- value cannot be blank.")
        IsValid = False
    elif IntegerValue.isdigit() == False:
        print("Invalid input - value must be numbers only.")
        IsValid = False

    return IsValid


def ValidPhone(PhoneValue):

    IsValid = True
    if PhoneValue.isdigit() == False:
        print("Invalid input - value must be numbers only - no spaces.")
        IsValid = False
    elif len(PhoneValue) != 10:
        print("Invalid input - must be 10 digits.")
        IsValid = False

    return IsValid

def ValidIntegerNumber(NumberValue, MinValue, MaxValue):

    IsValid = True
    try:
        NumberValue = int(NumberValue)
    except:
        print("Invalid input - must be a valid number.")
        IsValid = False
    else:
        if NumberValue < MinValue or NumberValue > MaxValue:
            print("Invalid input - number must be between " + str(MinValue) + " and " + str(MaxValue) + ".")
            IsValid = False

    return IsValid


def ValidFloatNumber(NumberValue, MinValue, MaxValue):

    IsValid = True
    try:
        NumberValue = float(NumberValue)
    except:
        print("Invalid input - must be a valid number.")
        IsValid = False
    else:
        if NumberValue < MinValue or NumberValue > MaxValue:
            print("Invalid input - number must be between " + str(MinValue) + " and " + str(MaxValue) + ".")
            IsValid = False

    return IsValid

def StrAndPad(DollarValue):
    DollarValueStr = "${:,.2f}".format(DollarValue)
    DollarValuePad = "{:>10}".format(DollarValueStr)

    return DollarValuePad

def ValidEmployeeNumber9():
    while True:
        try:
            EmployeeNumber = int(input("Enter employee number (9 digits): "))
        except:
            print("Error - please enter a valid number.")
            continue

        EmployeeNumber = str(EmployeeNumber)

        if EmployeeNumber == "":
            print("Invalid input- value cannot be blank.")
            continue
        elif len(EmployeeNumber) != 9:
            print("Invalid input - employee number must be 9 digits.")
            continue
        break

    return EmployeeNumber


def ProcessDate(Date1, Date2):
    StartDate = datetime.strptime(Date1, "%Y-%m-%d")
    EndDate = datetime.strptime(Date2, "%Y-%m-%d")

    TotalTravelDays = int((EndDate - StartDate).days)

    StartDate = StartDate.date()
    EndDate = EndDate.date()

    return StartDate, EndDate, TotalTravelDays
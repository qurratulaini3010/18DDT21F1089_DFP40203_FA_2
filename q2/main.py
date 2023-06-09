

filename = "DailySales.txt"


def display():
    print("-------Welcome To The D'Warung Cafe---------")
    print("We Have Variety Of Food including attractive Packages offers per head")
    print("Today Iftar packages has discount based on total Price")


def calculatekids(kids):
    kidsp = kids * 50
    return kidsp


def calculateadults(adult):
    adultsp = adult * 100
    return adultsp


def calcdis(totalka):
    total = 0.00
    if totalka > 200:
        total = totalka - (totalka * 0.05)
    elif totalka >= 300:
        total = totalka - (totalka * 0.10)
    else:
        print("Please Enter Correctly")
    return total


def mains():
    while True:
        display()
        kids = int(input("Please Enter the Number Of kids : "))
        adults = int(input("Please enter The number Of Adults : "))
        kidp = calculatekids(kids)
        adultp = calculateadults(adults)
        total = kidp + adultp
        discount = calcdis(total)
        if total:
            with open(filename, "a") as r:
                r.write(
                    f"Total Price For Kids: {kidp}\nTotal Price For Adults: {adultp}\nTotal Price: {total}\nTotal "
                    f"Price with Discount: {discount}\n")
            print(f"Total Price with Discount is: {discount}\n")
        print("Enter the number 3 anywhere if you want to stop")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mains()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

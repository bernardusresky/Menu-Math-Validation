from calculation import Math

class Menu():

    def __init__(self):
        self.math = Math()

#This function is for printing the menu and let user choose from it.
    def menu(self):
        #Use while(True) for menu looping
        while(True):
            print("\n -----Hi, This application is for introducing calculation in python.-----\n")
            print("1. Sum")
            print("2. Divison")
            print("3. Multiplication")
            print("4. Floor Division")
            print("5. Remainder")
            print("6. Square")
            print("7. Substraction")
            print("8. Exit")

            #This will take user input and assign it into userInput variable
            userInput = input("\nPlease enter your choice (1 - 8): ")

            #Using If .. Elif .. Else statement/conditional check to check user input and run the matched funtion.
            if(userInput == "1"):
                #When user input 1 it will ask for user to input 2 number and then call the sum function
                self.math.sum()
            elif(userInput == "2"):
                #When user input 2 it will ask for user to input 2 number and then call the division function
                self.math.division()
            elif(userInput == "3"):
                #When user input 3 it will ask for user to input 2 number and then call the multiplication function
                self.math.multiplication()
            elif(userInput == "4"):
                #When user input 4 it will ask for user to input 2 number and then call the division fraction function
                self.math.division_fractional()
            elif(userInput == "5"):
                #When user input 5 it will ask for user to input 2 number and then call the remainder function
                self.math.remainder()
            elif(userInput == "6"):
                #When user input 6 it will ask for user to input 2 number and then call the squeare function
                self.math.square()
            elif(userInput == "7"):
                #When user input 6 it will ask for user to input 2 number and then call the squeare function
                self.math.substraction()
            elif(userInput == "8"):
                #When user input 8 then it will the line and use break to stop the menu looping/ exit the program.
                print("\n -------------- Thankyou! See you! -------------------")
                break
            else:
                #When user input other than 1 - 8 it will print this line
                print("Invalid input - please try again.")

def main():
    menu = Menu()
    menu.menu()

if __name__ == '__main__':
    main()
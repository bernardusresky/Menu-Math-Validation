class Validation():

    def validate_number(self, user_input):
        try:
            int(user_input)
            Validity = True
        except ValueError:
            Validity = False
        return Validity

    def validate_first_number(self):
        x = input("\nPlease enter the first number :")
        while self.validate_number(x) != True:
                print("\nPlease enter a number!!")
                x = input("\nPlease enter the first number :")
        return int(x)

    def validate_second_number(self):
        y = input("\nPlease enter the second number :")
        while self.validate_number(y) != True:
                print("\nPlease enter a number!!")
                y = input("\nPlease enter the second number :")
        return int(y)
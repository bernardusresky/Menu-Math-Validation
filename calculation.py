#from file validate import Validation class
from validate import Validation

class Math():

    def __init__(self):
        self.validate = Validation()

    #This fuction will sum(+) x and y. Assign it into result variable, then print it.
    def sum(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        result = x + y
        print("\nThe sum of the two number is", result)
    
    #This fuction will multiplicate(*) x and y. Assign it into result variable, then print it.
    def multiplication(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        result = x * y
        print("\nThe multiplication of the two number is", result)

    #This function will divide(/) x and y. Assing it into divison variable, then print it.
    def division(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        division = x / y
        print("\nThe divison of the two number is", division)

    #While divison will return a float, you can use floor divison(//) which will remove the fraction. 
    def division_fractional(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        division = x // y
        print("\nThe fraction divison of the two number is", division)

    """ This function will divide x and y then take the remainder from the result of divison.
            Assign it into remainder variable, then print it. """
    def remainder(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        remainder = x % y
        print("\nThe remainder of the two number is", remainder)

    """This function will power or square x and y based on user input. 
       Assign it into square variable, then print it. """
    def square(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        square = x ** y
        print("\nThe square/powered of the two number is",square)

    """ This function will power or square x and y based on user input. 
           Assign it into square variable, then print it. """
    def substraction(self):
        #call function from validation class and assign the value returned to variable
        x = self.validate.validate_first_number()
        y = self.validate.validate_second_number()
        substraction = x - y
        print("\nThe subsrtraction of the two number is",substraction)
    
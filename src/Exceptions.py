class IllegalArgumentError(ValueError):
    #handling invalid arguments
    def __init__(self, message="Ivalid input"):
        super().__init__(message)



class DivisionByZero(ValueError):
    #handling division by zero
    def __init__(self, message="Can not divide by zero"):
        super().__init__(message)
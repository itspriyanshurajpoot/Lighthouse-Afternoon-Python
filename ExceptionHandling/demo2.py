class InvalidAgeError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


try:
    age = int(input("Enter your age "))

    # if(age <= 0):
    #     raise InvalidAgeError("Age cannot be negative")

    # if(age <= 0):
    #     raise AssertionError("Age cannot be negative")

    assert age >= 0 , "Invalid age"

    print(age)


except InvalidAgeError as e:
    print(f"{type(e).__name__} : {e}")

except AssertionError as e:
    print("I am assertion block")
    print(f"{type(e).__name__} : {e}")

# Number Checking Function
def num_check(question, type):

    if type == int:
        err_type = "an integer"
    else:
        err_type = "a number"

    error = "Please enter {} that is more than zero".format(err_type)

    valid = False
    while not valid:
        try:
            response = type(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)


how_many = num_check("How many items are you going to make / sell ? ", int)
print(how_many)
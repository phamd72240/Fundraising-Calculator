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


# Initialise lists
item_cost = []
expense_list = []

# Get inputs and add to item_cost list
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, break out of loop
    if item.lower() == "xxx":
        break

    # Get the cost (replace with number checking function in due course
    cost = num_check("Item Cost: $", float)

    # Add item name and cost to 'item' list
    item_cost.append(item)
    item_cost.append(cost)

    # Add item name and cost to expense list
    expense_list.append(item_cost)


# Sort by cost...
expense_list.sort(key=lambda x: x[1], reverse=1)

# Output...
print("**** Items by cost <Most expensive to least expensive> *****")
for item in expense_list:
    print("{}: ${:.2f}".format(item[0], item[1]))

print()

# Sort alphabetically
expense_list.sort(key=lambda x: x[0])

print("**** Items <Alphabetical> *****")
for item in expense_list:
    print("{}: ${:.2f}".format(item[0], item[1]))

total = 0

# Add costs...
for item in expense_list:
    total += item[1]

average = total / len(expense_list)
print("average: ", average)

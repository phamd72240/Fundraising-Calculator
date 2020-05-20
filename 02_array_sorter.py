expense_list = [['White Mug', 1.0], ['Printing', 0.75], ['Packaging', .5]]

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

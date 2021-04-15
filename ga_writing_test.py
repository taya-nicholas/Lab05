
data = [10, 15, 2, 4151, 44]
with open('genetic_data.txt', 'w') as file_object:
    for item in data:
        file_object.write("\n" + str(item))

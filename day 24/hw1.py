#1
food_items = ["breid", "waterr", "meat", "apple", "banana"]

print(food_items)


#2


computer_accessories = ["keiboard", "kamera", "mouse", "screen"]
index_of_mouse = computer_accessories.index("keiboard")
print(index_of_mouse)

# გამოიტანა 0 რადგან ათვლა იწყება 0 იდან

#3

data_types = [1, 2.5, "string", True, 1, 2.5, "string", False]

boolean_values = [value for value in data_types if isinstance(value, bool)]
print(boolean_values)



#4

unique_data_types = [1, 2.5, "string", True]
string_value = unique_data_types[-1]  
print(string_value)



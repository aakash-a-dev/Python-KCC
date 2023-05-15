Dict1 = {1: "Aakash", 2: "Anjali", 3: "Hrishik"}
print(Dict1)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Aakash', 2: 'Anjali', 3: 'Hrishik'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Aakash', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Dict = dict([(1, 'Aakash'), (2, 'KCC')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# Accessing through For Loop:
my_dict = {'1': 'Aakash', '2': 'Anjali', '3': 'Hrishik', '4': 'Atithi'}

# Accessing dictionary elements using a for loop
for key in my_dict:
    value = my_dict[key]
    print(f"Key: {key}, Value: {value}")

# import module
from tabulate import tabulate
 
# assign data
mydata = [
    ["Aakash", "Surat"],
    ["Hrishik", "Delhi"],
    ["Anjali", "Bhagalpur"],
    ["Atithi", "Greater Noida"]
]
 
# create header
head = ["Name", "City"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))
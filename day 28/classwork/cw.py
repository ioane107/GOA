#pirveli 1
# upper ყველა ასო გადაყავს დიდზე
# lower  ყველა ასო პატარად იქცევა
# capitalie პირველი ასო დიდი სხვა ასოები პატარად გადადის
# find  პოულობს ასოს მდებარევას


#meore 2

name = input("name: ")
if name[0].upper():
    print("helo!")
else:
    print("bye...")



#mesame 3
surname = input("usernam: ")

if surname[0] == "m" or surname[0] == "M":
    print(surname.upper())  
elif surname[0] == "g" or surname[0] == "G":
    print(name.lower()) 



#meotxe 4
color = input("enter colort: ")

if "p" in color or "P" in color:
    print("gamarjoba")
else:
    print("naxvamdis")

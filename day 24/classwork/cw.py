number = int(input("neter numerber "))
             
if number > 0:
    print("the number is posite")
elif number < 0:
    print("the number is ngative")
else:
    print("the number is zero")




    #@2
    
corect_password = "myseketpassword"


user_password = input("pleaz enter password: ")

while user_password != corect_password:
    print("incorrect password")
    user_password = input("please enter password: ")


print("correct password")

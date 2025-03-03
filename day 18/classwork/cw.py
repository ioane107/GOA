for i in range(0,10):
    print(i)


    #2
    for i in range(50, 151):
        print(i)


        #3
        for i in range(200, 500, 2):
            print(i)


            #4
            for i in range(0, 50, 20):
        
                    print(i)
            
            #5
start = int(input("შეიყვანეთ სტარტ რიცხვი (start): "))
end = int(input("შეიყვანეთ ბოლო რიცხვი (end): "))
step = int(input("შეიყვანეთ სტეპი (step): "))

# range
for number in range(start, end + 1, step):
    print(number)


#6
name = input("შეიყვანეთ თქვენი სახელი: ")
#
for letter in name:
    print(letter)



rent=int(input("Enter your falt/hostel rent = "))
food=int(input("Enter your cost for snacks/food = "))
unit=int(input("Enter your spends unit of electricity = "))
charge=int(input("Enter your charge per unit = "))
persons=int(input("Enter thenumber of persons living in flat = "))

total_bill=unit*charge

output=(rent+food+total_bill)//persons
print("Each person will pay ",output)
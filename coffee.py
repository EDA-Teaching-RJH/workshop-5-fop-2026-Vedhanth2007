

num = int(input("Enter the number of coffee's you want: "))
amount = num * 75
final = 0
print("Cost: ",amount)
while final < amount:
    coin = int(input("Enter coin here: "))
    if coin == 50 or coin == 10 or coin == 5 or coin == 20:
        final = final + coin
        print("amount deposited:",final)
    else:
        print("Coin invalid.")
        print("amount deposited",final)
owned = final - amount
print("Amount owned", owned)
    

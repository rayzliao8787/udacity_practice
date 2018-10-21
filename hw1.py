miles = input("How many miles have you traveled? ")
check = int(miles)
money = 0

if check < 20 or check == 20:
    money += 0
elif check < 200 and check > 20:
    for i in range(check - 20):
        money += 1.2
else:
    money += 1.2*180
    for i in range(check - 200):
        money += 0.8
money = round(money)
print(money)

amount = int(input("Enter your amount to be withdrawn :"))

note_1 = (amount//20)
note_2 = (amount%20)// 10
note_3 = ((amount%20)%10)// 1

print("20 pound notes =", note_1)
print("10 pound notes =", note_2)
print("1 pound coins =", note_3)
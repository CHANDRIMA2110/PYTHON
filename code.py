largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num1 = int(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")
    if smallest is None:
        smallest= num1
    if largest is None:
        largest = num1
    if num1 > largest:
         largest = num1
    if smallest > num1:
         smallest = num1

print("Maximum is", largest)
print("Minimum is", smallest)
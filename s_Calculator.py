print("Choose an operation from below: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("1/2/3/4: ")

num1 = float(input("Enter first digit: "))
num2 = float(input("Enter second digit: "))

if choice == '1':
    results = num1 + num2
    print("the results of adding",num1,"to",num2,"is equal to",results)
elif choice == '2':
    results = num1 - num2
    print("the results of subtracting",num2,"from",num1,"is equal to",results)
elif choice == '3':
    results = num1 * num2
    print("the result for multiplying",num1,"by",num2,"is equal to",results)
elif choice == '4':
    results = num1/num2
    print("the results for dividing",num1,"by",num2,"is equal to",results)

    
else :
    print("Err30344")
    

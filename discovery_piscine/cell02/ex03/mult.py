num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

result = num1 * num2

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

print(result)
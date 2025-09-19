def calculator(num1, num2, operator):
  if operator == '+':
    return(num1 + num2)
  elif operator == '-':
    return(num1 - num2)
  elif operator == '*':
    return(num1 * num2)
  elif operator == '/':
    return(num1 / num2)
  else:
    print('Wrong input')
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator:")
result = calculator(num1, num2, operator)
print("Result :", result)
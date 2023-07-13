print("Welcome to the Calculator!(Type: 'exit' to quit)")

while True:
    operation = input("Enter an number to calculate: ")

    if operation.lower() == "exit":
        print("Calculator off.")
        break

    try:
        result = eval(operation.replace(" ", ""))
        print("Result:", result)
    except Exception as e:
        print("Error: Invalid equation.")

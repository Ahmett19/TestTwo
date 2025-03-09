try:
    
    with open("example.txt", "r") as file:
        content = file.read()
    result = 10 / 0  
except FileNotFoundError:
    print("Error: The file was not found.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Operation successful!")
finally:
    print("This block executes no matter what.")

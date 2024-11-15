class Calculator:
    def __init__(self):
        """Initializes the calculator with no stored value."""
        self.value = 0

    def add(self, a, b):
        """Returns the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference between a and b."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Returns the division of a by b. Handles division by zero."""
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def menu(self):
        """Displays the calculator menu."""
        print("\nSimple Calculator")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exit")

    def run(self):
        """Runs the calculator."""
        while True:
            self.menu()
            choice = input("Select operation (1-5): ")

            if choice == '5':
                print("Exiting calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select a valid operation.")
                continue

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = self.add(num1, num2)
            elif choice == '2':
                result = self.subtract(num1, num2)
            elif choice == '3':
                result = self.multiply(num1, num2)
            elif choice == '4':
                result = self.divide(num1, num2)

            print(f"Result: {result}")

# Instantiate and run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()

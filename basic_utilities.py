# Python Mastery Toolkit - Basic Utilities
def welcome_message():
    print("Welcome to the Python Mastery Toolkit!")
    print("This project helps beginners learn Python step-by-step.")

def simple_calculator(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "Error"
    }

if __name__ == "__main__":
    welcome_message()
    print(f"Calculation Result: {simple_calculator(10, 5)}")
  

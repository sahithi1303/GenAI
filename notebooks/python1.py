'''def calculate_sum(number1, number2):
    """
    Calculate the sum of two numbers
    
    Args:
        number1: First number
        number2: Second number
        
    Returns:
        The sum of number1 and number2
    """
    result = number1 + number2
    return result

# Example usage
x = 10
y = 20
total = calculate_sum(x, y)
print(f"The sum of {x} and {y} is: {total}")


def multiply_numbers(x, y):
    """
    Multiply two numbers together
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Product of x and y
    """
    return x * y

def divide_numbers(numerator, denominator):
    """
    Divide two numbers
    
    Args:
        numerator: Number to be divided
        denominator: Number to divide by
        
    Returns:
        Result of division
    """
    return numerator / denominator

# Example usage
num1 = 20
num2 = 5

product = multiply_numbers(num1, num2)
quotient = divide_numbers(num1, num2)

print(f"Multiplication result: {product}")
print(f"Division result: {quotient}")
'''

import gradio as gr

def multiply_numbers(x, y):
    """
    Multiply two numbers together
    """
    return x * y

def divide_numbers(numerator, denominator):
    """
    Divide two numbers
    """
    if denominator == 0:
        return "Cannot divide by zero"
    return numerator / denominator

# Create Gradio interface for multiplication
def calculator_interface(num1, num2, operation):
    if operation == "Multiply":
        return multiply_numbers(num1, num2)
    else:
        return divide_numbers(num1, num2)

# Create the Gradio interface
demo = gr.Interface(
    fn=calculator_interface,
    inputs=[
        gr.Number(label="First Number"),
        gr.Number(label="Second Number"),
        gr.Radio(["Multiply", "Divide"], label="Operation")
    ],
    outputs=gr.Number(label="Result"),
    title="Basic Calculator",
    description="Enter two numbers and select an operation",
    examples=[
        [10, 5, "Multiply"],
        [20, 4, "Divide"]
    ]
)

# Launch the interface
if __name__ == "__main__":
    demo.launch()

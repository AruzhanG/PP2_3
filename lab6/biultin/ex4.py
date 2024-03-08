import time
import math

def calculate_square_root(number):
    return math.sqrt(number)


input_number = int(input("Enter a number: "))
delay_milliseconds = int(input("Enter the delay time in milliseconds: "))


time.sleep(delay_milliseconds / 1000.0)


result = calculate_square_root(input_number)


print(f"Square root of {input_number} after {delay_milliseconds} milliseconds is {result}")

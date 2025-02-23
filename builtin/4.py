import math
import time
def delyed(number, delay):
    time.sleep(delay/1000)
    return math.sqrt(number)

number=int(input("enetr a number "))
delay=int(input("enetr the delay in ms "))
result = delyed(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

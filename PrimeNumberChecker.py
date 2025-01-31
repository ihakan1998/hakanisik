#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = 17  # Change this number to test other values
is_prime = True  # Assume the number is prime unless proven otherwise

# A prime number is greater than 1 and divisible only by 1 and itself
if number > 1:
    for i in range(2, int(number**0.5) + 1):  # Loop from 2 to the square root of the number
        if number % i == 0:  # Check if the number is divisible by i
            is_prime = False  # If it is divisible, it's not a prime number
            break  # Exit the loop as we found a divisor

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number.")  # Numbers <= 1 are not prime


# In[ ]:





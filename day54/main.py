#!/usr/bin/env python

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 



def speed_calc_decorator(func):
  def wrapper():
    start_time = time.time()
    func()
    end_time = time.time() 
    print(f"{func.__name__} ran for:  {(end_time-start_time)}")
  return wrapper


@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()

# Alternative for fast function
print("-----ALternative-------")

fast = speed_calc_decorator(fast_function)
fast()

from math import log

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_log_return(start_price, end_price):
  return log(end_price / start_price)


log_return = calculate_log_return(200, 250)

print('The log rate of return is', display_as_percentage(log_return))





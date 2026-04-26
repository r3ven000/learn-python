"""
Task: Automated Fuel Dispenser Logic
A customer is refueling a car with a fuel tank capacity of 50 liters. 
The pump delivers 3 liters of fuel per second. 
The task is to simulate the refueling process such that:
1. The tank starts empty (0 liters).
2. The pump adds 3 liters every second until the tank is almost full.
3. If the next 3-liter delivery would exceed the tank capacity (50 liters), 
   the pump must only deliver the exact amount needed to reach 50 liters.
4. The process stops once the tank is exactly full.
"""
current_fuel = 0
full_fuel = 50
sec = 3
while current_fuel < 50:

    if current_fuel + 3 > 50:
        remainder = 50 - current_fuel
        current_fuel += remainder

    else:
        current_fuel += 3

    print(current_fuel)


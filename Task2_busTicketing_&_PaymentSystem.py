class BusPass:
    def __init__(self, name, price, validity_days):
        self.name = name
        self.price = price
        self.validity_days = validity_days

class Passenger:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bus_passes = []

    def buy_pass(self, bus_pass):
        self.bus_passes.append(bus_pass)

# Sample bus passes
daily_pass = BusPass("Daily Pass", 10, 1)
weekly_pass = BusPass("Weekly Pass", 50, 7)
monthly_pass = BusPass("Monthly Pass", 150, 30)

# Sample passengers
passenger1 = Passenger("Johny", "joni@gmail.com")
passenger2 = Passenger("bandi", "bandi@gmail.com")

# Simulate bus pass purchases
passenger1.buy_pass(daily_pass)
passenger2.buy_pass(weekly_pass)
passenger2.buy_pass(monthly_pass)

# Display passenger information and purchased bus passes
print(f"{passenger1.name} ({passenger1.email}):")
for bus_pass in passenger1.bus_passes:
    print(f"- {bus_pass.name}: ${bus_pass.price}, Validity: {bus_pass.validity_days} days")

print(f"\n{passenger2.name} ({passenger2.email}):")
for bus_pass in passenger2.bus_passes:
    print(f"- {bus_pass.name}: ${bus_pass.price}, Validity: {bus_pass.validity_days} days")

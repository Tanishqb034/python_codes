import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 200, 250]

plt.plot(months, sales)

plt.title("Monthly Sales Analysis")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
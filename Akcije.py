import matplotlib.pyplot as plt


stock_prices = [10,12,15,18,20,22,25]
dates = ["Jan 1","Jan 2","Jan 3","Jan 4","Jan 5","Jan 6","Jan 7"]

plt.plot(dates,stock_prices)
plt.xlabel("datum")
plt.ylabel("Ciejna akcija")
plt.title("Kretanje akcija")
plt.savefig("akcije.png")
import matplotlib.pyplot as plt


labels =["A","B","C"]
values = [1,2,6]
bars = plt.bar(labels,values)
bars[0].set_hatch("/")
bars[1].set_hatch("o")
plt.savefig("barchar.png")
plt.show

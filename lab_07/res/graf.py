import matplotlib.pyplot as plt
plt.xlabel("COUNT")
plt.ylabel("MEMORY")
plt.grid(True)
plt.title("MEMORY(COUNT)")
y1 = (48, 88, 128, 168)
x = (5, 10, 15, 20)
plt.plot(x, y1, '-',label ="Memory")
plt.legend()
plt.show()

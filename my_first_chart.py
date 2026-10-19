import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"

prices = [259000, 3065000, 224000, 241500, 258500, 207000, 189600, 188300, 172500,163300]

fig, ax = plt.subplots()
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")
ax.set_title("현대차3우B 월별 주가")
fig.savefig("my_first_chart.png")
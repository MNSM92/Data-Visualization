import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

fifa_data = pd.read_csv("data/fifa.csv", index_col="Date", parse_dates=True)

plt.figure(figsize=(16,6))


sns.lineplot(data=fifa_data)
plt.savefig("plots/fifa.png")

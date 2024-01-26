import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

data = pd.read_csv("data/spotify.csv", index_col="Date", parse_dates=True)
plt.figure(figsize=(16,6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
plt.xlabel("Date")

sns.lineplot(data=data)
plt.savefig("plots/spotify1.png")

plt.figure(figsize=(16,6))
sns.lineplot(data=data['Shape of You'], label="Shape of You")
sns.lineplot(data=data['Despacito'], label="Despacito")


plt.xlabel("Date")
plt.savefig("plots/spotify2.png")

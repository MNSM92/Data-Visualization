import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.plotting.register_matplotlib_converters()

insurance_data = pd.read_csv("data/insurance.csv")

# Scatter plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
plt.savefig("plots/insurance1.png")

# Regression plot
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
plt.savefig("plots/insurance2.png")

# Regression plot with hue
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
plt.savefig("plots/insurance3.png")

# Swarm plot
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
plt.savefig("plots/insurance4.png")

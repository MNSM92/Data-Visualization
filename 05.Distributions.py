import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

iris_data = pd.read_csv('data/iris.csv', index_col="Id")

plt.figure(figsize=(10, 6))
# Histogram
sns.histplot(iris_data['Petal Length (cm)'])
plt.savefig("plots/iris1.png")

plt.figure(figsize=(10, 6))
# KDE plot
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
plt.savefig("plots/iris2.png")

plt.figure(figsize=(10, 6))
# Joint plot 2D
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
plt.savefig("plots/iris3.png")

plt.figure(figsize=(10, 6))
# Distribution plot
plt.title("Histogram of Petal Lengths, by Species")
sns.histplot(data=iris_data, x='Petal Length (cm)', hue='Species')
plt.savefig("plots/iris4.png")

plt.figure(figsize=(10, 6))
# Distribution plot
sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', shade=True)
plt.title("Distribution of Petal Lengths, by Species")
plt.savefig("plots/iris5.png")

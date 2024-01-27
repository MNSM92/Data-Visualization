'''
Trends
    -Line charts with sns.lineplot
Relationship
    -Bar charts with sns.barplot
    -Heatmaps with sns.heatmap
    -Scatter plots with sns.scatterplot
    -Regression plots with sns.regplot
    -Multiple Regression plots with sns.lmplot
    -Swarm plots with sns.swarmplot
Distributions
    -Histograms with sns.histplot
    -Distribution plots with sns.kdeplot
    -Joint plots with sns.jointplot
'''
# Trends-Line, Relationship- Heatmap, Bar, Scatter, Regression, Swarm, Distributions- Distribution, Joint, Histogram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

spotify_data = pd.read_csv('data/spotify.csv', index_col="Date", parse_dates=True)

plt.figure(figsize=(12,6))
# "darkgrid"/ "whitegrid"/ "dark"/ "white"/ "ticks"
sns.set_style("ticks")
sns.lineplot(data=spotify_data)
plt.savefig("plots/spotify3.png")

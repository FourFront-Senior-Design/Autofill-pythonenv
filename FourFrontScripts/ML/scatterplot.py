# library & dataset
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/Python/FourFrontScripts/DataPrep/data.csv", engine='python')

name = ['FirstName', 'MiddleName', 'LastName', 'Suffix']
date = ['BirthDate', 'DeathDate']
rank = ['Rank', 'Rank2', 'Rank3']
branch = ['Branch', 'Branch2', 'Branch3']
rank.extend(branch)
indf = df[df['category'] == 'Inscription']
namedf = df[df['category'].isin(name)]
datedf = df[df['category'].isin(date)]
rankdf = df[df['category'].isin(rank)]

# Use the 'hue' argument to provide a factor variable
sns.scatterplot(x="x1", y="y2", data=df, hue='category')
#sns.scatterplot(x="x1", y="y1", data=indf, hue='category')
#sns.scatterplot(x="x1", y="y1", data=datedf, hue='category')
#sns.scatterplot(x="x1", y="y1", data=rankdf, hue='category')
plt.show()
# Move the legend to an empty part of the plot
#plt.legend(loc='lower right')

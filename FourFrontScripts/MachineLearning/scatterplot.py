import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Plots of the data prepared for training
df = pd.read_csv(r"C:/Python/FourFrontScripts/TestData/data.csv", engine='python')

name = ['FirstName', 'MiddleName', 'LastName', 'Suffix']
date = ['BirthDate', 'DeathDate']
rankBranch = ['Rank', 'Branch', 'War']

indf = df[df['category'] == 'Inscription']
namedf = df[df['category'].isin(name)]
datedf = df[df['category'].isin(date)]
rankBranchdf = df[df['category'].isin(rankBranch)]

fig = plt.figure()

# Creates a scatter plot for the location of the words
# inscription
ax = fig.add_subplot(2, 2, 1)
sns.scatterplot(x="x1", y="y1", data=df, hue='markerType', ax=ax)

# names (Primary)
ax = fig.add_subplot(2, 2, 2)
sns.scatterplot(x="x1", y="y1", data=namedf, hue='category', ax=ax)

# dates(Primary)
ax = fig.add_subplot(2, 2, 3)
sns.scatterplot(x="x1", y="y1", data=datedf, hue='category', ax=ax)

# ranks and branch(Primary)
ax = fig.add_subplot(2, 2, 4)
sns.scatterplot(x="x1", y="y1", data=rankBranchdf, hue='category', ax=ax)

plt.show()

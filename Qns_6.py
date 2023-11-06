import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('adult.csv')

# Filter data into two income categories (above 50k and below 50k)
above_50k = data[data['class'] == '>50K']
below_50k = data[data['class'] == '<=50K']

# Count the number of men and women in each category
men_above_50k = above_50k[above_50k['sex'] == 'Male'].shape[0]
women_above_50k = above_50k[above_50k['sex'] == 'Female'].shape[0]
men_below_50k = below_50k[below_50k['sex'] == 'Male'].shape[0]
women_below_50k = below_50k[below_50k['sex'] == 'Female'].shape[0]

# Create bar plots
categories = ['Above 50k', 'Below 50k']
men_counts = [men_above_50k, men_below_50k]
women_counts = [women_above_50k, women_below_50k]

fig, ax = plt.subplots()
width = 0.35
x = range(len(categories))

bar1 = ax.bar(x, men_counts, width, label='Men')
bar2 = ax.bar([i + width for i in x], women_counts, width, label='Women')

ax.set_xlabel('Income Category')
ax.set_ylabel('Count')
ax.set_title('Income Category by Gender')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(categories)
ax.legend()

plt.show()

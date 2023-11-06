import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('adult.csv')

# Filter data for individuals in "Machine-op-inspect" and "Sales" occupations
machine_op_inspect = data[data['occupation'] == 'Machine-op-inspect']
sales = data[data['occupation'] == 'Sales']

# Create a box plot to compare working hours
plt.figure(figsize=(10, 6))
plt.boxplot([machine_op_inspect['hours-per-week'], sales['hours-per-week']], labels=['Machine-op-inspect', 'Sales'])
plt.title('Comparison of Working Hours in Different Occupations')
plt.ylabel('Hours per Week')
plt.show()

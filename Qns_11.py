import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset using a list
data = []
with open('fire.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read the header row
    for row in csv_reader:
        data.append([float(value) for value in row])

# Split the data into features (X) and target variable (y)
X = [row[:-1] for row in data]  # Features (all columns except the last one)
y = [int(row[-1]) for row in data]  # Target variable (last column)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
logistic_regression_model = LogisticRegression(solver='liblinear')
logistic_regression_model.fit(X_train, y_train)

# Get the regression coefficients
coefficients = logistic_regression_model.coef_[0]

# Find the variable with the most significant association with fire
most_significant_index = coefficients.argmax()
most_significant_variable = header[most_significant_index]

# Display the most significant variable
print(f"The variable most significantly associated with fire is: {most_significant_variable}")

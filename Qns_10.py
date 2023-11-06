import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# Split the data into a training set (70%) and a testing set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a decision tree model with a limited depth of 5
tree_model_depth_5 = DecisionTreeClassifier(max_depth=5)
tree_model_depth_5.fit(X_train, y_train)

# Train a decision tree model without limiting the depth
tree_model_unlimited_depth = DecisionTreeClassifier()
tree_model_unlimited_depth.fit(X_train, y_train)

# Make predictions with both models
y_pred_depth_5 = tree_model_depth_5.predict(X_test)
y_pred_unlimited_depth = tree_model_unlimited_depth.predict(X_test)

# Calculate accuracy for both models
accuracy_depth_5 = accuracy_score(y_test, y_pred_depth_5)
accuracy_unlimited_depth = accuracy_score(y_test, y_pred_unlimited_depth)

# Explain the reason for the difference in accuracy
explanation = "The limited depth decision tree model (depth=5) is likely to be less complex and less prone to overfitting. It may provide better generalization because it doesn't learn the training data as intricately as the model without depth limitation. In contrast, the decision tree model without depth limitation can create a more complex and overfitted model, which may perform well on the training data but poorly on unseen test data due to overfitting."

# Display the accuracy and explanation
print(f"Accuracy of Decision Tree (depth=5): {accuracy_depth_5:.2f}")
print(f"Accuracy of Decision Tree (unlimited depth): {accuracy_unlimited_depth:.2f}")
print("\nExplanation for the difference in accuracy:\n", explanation)

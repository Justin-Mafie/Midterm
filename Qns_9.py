import csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset using a list
data = []
with open('fire.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        data.append([float(value) for value in row])

# Split the data into features (X) and target variable (y)
X = [row[:-1] for row in data]  # Features (all columns except the last one)
y = [int(row[-1]) for row in data]  # Target variable (last column)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier with Euclidean distance metric
k = 5  # You can adjust the value of k
knn_classifier = KNeighborsClassifier(n_neighbors=k, metric='euclidean')

# Train the KNN model on the training data
knn_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = knn_classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of KNN model with k={k}: {accuracy:.2f}")

import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Set experiment name
mlflow.set_experiment("Iris Classification Experiment")

# Load Iris dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
)

y = pd.Series(iris.target).map({
    0: "setosa",
    1: "versicolor",
    2: "virginica"
})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model parameters
n_estimators = 100
max_depth = 3
random_state = 42

# Start MLflow run
with mlflow.start_run():

    # Create model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    # Log parameters
    mlflow.log_param("model_name", "RandomForestClassifier")
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("random_state", random_state)

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(model, "random_forest_model")

    print("MLflow Experiment Completed Successfully")
    print("Model Name: RandomForestClassifier")
    print("Accuracy:", accuracy)
    print("Parameters:")
    print("n_estimators:", n_estimators)
    print("max_depth:", max_depth)
    print("random_state:", random_state)
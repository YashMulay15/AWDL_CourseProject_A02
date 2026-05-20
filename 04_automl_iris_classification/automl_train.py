import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyClassifier


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

print("Dataset loaded successfully")
print("\nFirst five rows of features:")
print(X.head())

print("\nTarget classes:")
print(y.unique())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# AutoML model comparison
clf = LazyClassifier(
    verbose=0,
    ignore_warnings=True,
    custom_metric=None
)

models, predictions = clf.fit(X_train, X_test, y_train, y_test)

print("\nAutoML Model Comparison Results:")
print(models)

print("\nTop 5 Best Models:")
print(models.head())
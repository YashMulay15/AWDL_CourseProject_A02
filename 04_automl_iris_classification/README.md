# AutoML Use Case: Iris Flower Classification using Scikit-learn Model Comparison

## Objective

To demonstrate AutoML-style model selection by automatically training and comparing multiple machine learning classification models on the Iris dataset.

## Tool Used

Scikit-learn based AutoML-style model comparison

## Dataset

Iris Dataset

## Features

- sepal_length
- sepal_width
- petal_length
- petal_width

## Target

- species

## Installation Command

```bash
pip install pandas scikit-learn
```

## Execution Command

```bash
python automl_train.py
```

## Process

1. Load Iris dataset
2. Split dataset into training and testing data
3. Train multiple ML models automatically
4. Compare model accuracy
5. Select the best-performing model

## Models Compared

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors

## Expected Output

```text
AutoML Model Comparison Results
Best Model Selected
Accuracy
```

## Conclusion

This use case demonstrates AutoML-style model comparison by automatically training multiple models and selecting the best-performing model based on accuracy.
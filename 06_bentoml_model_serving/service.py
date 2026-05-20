import bentoml
import pandas as pd


# Load the latest saved Iris model from BentoML model store
iris_model = bentoml.sklearn.load_model("iris_classifier:latest")


@bentoml.service
class IrisPredictionService:

    @bentoml.api
    def predict(self, input_data: dict) -> dict:
        data = pd.DataFrame([{
            "sepal_length": input_data["sepal_length"],
            "sepal_width": input_data["sepal_width"],
            "petal_length": input_data["petal_length"],
            "petal_width": input_data["petal_width"]
        }])

        prediction = iris_model.predict(data)

        class_names = {
            0: "setosa",
            1: "versicolor",
            2: "virginica"
        }

        predicted_class = int(prediction[0])

        return {
            "prediction": class_names[predicted_class]
        }
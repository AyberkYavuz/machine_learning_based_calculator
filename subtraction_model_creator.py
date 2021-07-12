import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from helpers.application_helpers import RegressionHelper
from file_operations.file_handlers import PickleHandler

working_directory = os.getcwd()
substraction_data_path = working_directory + '/machine_learning_data/subtraction.csv'

print("reading substraction data")
substruction_data = pd.read_csv(substraction_data_path, delimiter=",")

print("splitting data")
features = substruction_data[["Number1", "Number2"]]
target = substruction_data["Substruction"]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.30, random_state=42)

print("training substruction machine learning model")
linear_regression = LinearRegression()
substruction_machine_learning_model = linear_regression.fit(X_train, y_train)

print("Making predictions")
y_test_prediction = substruction_machine_learning_model.predict(X_test)

print("Displaying regression model metrics")
RegressionHelper.show_regression_model_metrics(substruction_machine_learning_model, y_test, y_test_prediction)

print("Saving substruction machine learning model")
pickle_handler = PickleHandler()
model_path = working_directory + '/machine_learning_models/subtraction_machine_learning_model.pickle'
pickle_handler.save_object(model_path, substruction_machine_learning_model)

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask.views import MethodView
from helpers.application_helpers import BackendHelper
import pandas as pd
from file_operations.file_handlers import PickleHandler
import os

app = Flask(__name__)
app.secret_key = BackendHelper.create_random_aplhanumeric_string()


class MainPageSenderAPI(MethodView):
    def get(self):
        return render_template("main_page.html")


class SummationMachineLearningModelAPI(MethodView):

    def get(self):
        return "Welcome to summation machine learning model API!", 200

    def post(self):
        print("SummationMachineLearningModelAPI POST Method")
        msg = None

        cond1 = "number1" not in request.form
        cond2 = "number2" not in request.form

        if cond1 or cond2:
            msg = "422", 422
        else:
            try:
                print("creating x_test")
                number1 = request.form['number1']
                number2 = request.form['number2']
                features_data = [[number1, number2]]
                x_test = pd.DataFrame(features_data, columns=['Number1', 'Number2'])
                print("loading summation machine learning model")
                working_directory = os.getcwd()
                summation_model_path = working_directory + '/machine_learning_models/' \
                                                           'summation_machine_learning_model.pickle'
                pickle_handler = PickleHandler()
                summation_machine_learning_model = pickle_handler.load_object(summation_model_path)
                print("making a prediction")
                prediction = summation_machine_learning_model.predict(x_test)[0]
                prediction = round(prediction, 2)
                print(prediction)
                msg = jsonify({"prediction": prediction}), 200
            except Exception as ex:
                print("Exception : " + str(ex))
                msg = "Something went wrong!", 500

        return msg


class SubtractionMachineLearningModelAPI(MethodView):

    def get(self):
        return "Welcome to Subtraction Machine Learning Model API!", 200

    def post(self):
        print("SubtractionMachineLearningModelAPI POST Method")
        msg = None

        cond1 = "number1" not in request.form
        cond2 = "number2" not in request.form

        if cond1 or cond2:
            msg = "422", 422
        else:
            try:
                print("creating x_test")
                number1 = request.form['number1']
                number2 = request.form['number2']
                features_data = [[number1, number2]]
                x_test = pd.DataFrame(features_data, columns=['Number1', 'Number2'])
                print("loading subtraction machine learning model")
                working_directory = os.getcwd()
                subtraction_model_path = working_directory + '/machine_learning_models/' \
                                                              'subtraction_machine_learning_model.pickle'
                pickle_handler = PickleHandler()
                summation_machine_learning_model = pickle_handler.load_object(subtraction_model_path)
                print("making a prediction")
                prediction = summation_machine_learning_model.predict(x_test)[0]
                prediction = round(prediction, 2)
                print(prediction)
                msg = jsonify({"prediction": prediction}), 200
            except Exception as ex:
                print("Exception : " + str(ex))
                msg = "Something went wrong!", 500

        return msg


main_page_sender_view = MainPageSenderAPI.as_view('main_page_sender_api')
app.add_url_rule('/', view_func=main_page_sender_view, methods=['GET'])
summation_machine_learning_model_view = SummationMachineLearningModelAPI.as_view('summation_machine_learning_model_api')
app.add_url_rule('/summation', view_func=summation_machine_learning_model_view, methods=['POST', 'GET'])
subtraction_machine_learning_model_view = SubtractionMachineLearningModelAPI.as_view('subtraction_machine_learning_model_api')
app.add_url_rule('/subtraction', view_func=subtraction_machine_learning_model_view, methods=['POST', 'GET'])
app.run(debug=True)

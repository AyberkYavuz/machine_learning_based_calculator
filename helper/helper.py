import random
import string
from sklearn.metrics import mean_squared_error, r2_score


class BackendHelper:
    @staticmethod
    def create_random_aplhanumeric_string():
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(18))
        return token


class RegressionHelper:
    @staticmethod
    def show_regression_model_metrics(regression_model, y_test, y_test_prediction):
        print('Coefficients: \n', regression_model.coef_)

        print('Mean squared error: %.2f'
              % mean_squared_error(y_test, y_test_prediction))

        print('Coefficient of determination: %.2f'
              % r2_score(y_test, y_test_prediction))


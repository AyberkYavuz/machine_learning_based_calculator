# machine_learning_based_calculator
This repository is a tutorial for beginners who want to learn how to develop end to end machine learning system.

## Project Structure
```bash
machine_learning_based_calculator
├── file_operations
│   ├── __init__.py
│   └── file_handlers.py
├── helpers
│   ├── __init__.py
│   └── application_helpers.py
├── machine_learning_data
│   ├── subtraction.csv
│   └── summation.csv
├── machine_learning_models
│   ├── subtraction_machine_learning_model.pickle
│   └── summation_machine_learning_model.pickle
├── static
│   ├── css
│   │   ├── materialize.min.css
│   │   └── style.css
│   ├── fonts
│   │   └── roboto
│   │       ├── Roboto-Bold.woff
│   │       ├── Roboto-Bold.woff2
│   │       ├── Roboto-Light.woff
│   │       ├── Roboto-Light.woff2
│   │       ├── Roboto-Medium.woff
│   │       ├── Roboto-Medium.woff2
│   │       ├── Roboto-Regular.woff
│   │       ├── Roboto-Regular.woff2
│   │       ├── Roboto-Thin.woff
│   │       └── Roboto-Thin.woff2
│   └── js
│       ├── materialize.min.js
│       └── server_request_handler.js
├── templates
│   └── main_page.html
├── README.md
├── subtraction_model_creator.py
├── summation_model_creator.py
└── web_application_backend.py
```

## Usage
[Machine Learning Based Calculator Usage](https://www.youtube.com/watch?v=xrv5PvmjOro&ab_channel=AyberkYavuz)

## Application Files Descriptions

### main_page.html
[main_page.html](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/templates/main_page.html)
is the web application's user interface.

### server_request_handler.js
[server_request_handler.js](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/static/js/server_request_handler.js)
is the javascript application which enables interactions between user interface and web application's backend. 

### web_application_backend.py
[web_application_backend.py](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/web_application_backend.py)
is the web application's backend that renders main_page.html and serves trained summation machine learning model
and trained subtraction machine learning model as APIs.

### summation_model_creator.py
[summation_model_creator.py](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/summation_model_creator.py)
uses [summation.csv](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/machine_learning_data/summation.csv) 
in order to produce [trained summation machine learning model](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/machine_learning_models/summation_machine_learning_model.pickle).

### subtraction_model_creator.py
[subtraction_model_creator.py](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/subtraction_model_creator.py)
uses [subtraction.csv](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/machine_learning_data/subtraction.csv) 
in order to produce [trained subtraction machine learning model](https://github.com/AyberkYavuz/machine_learning_based_calculator/blob/master/machine_learning_models/subtraction_machine_learning_model.pickle).

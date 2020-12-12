# Covid-19 infection prediction app

This is a flask web application that predict covid-19 infection based on symptoms.

This application uses a simple machine learning model for prediction.

## Installation

1. Download project directory

2. ``` cd covid_ml_flask ```

3. Create virtualenv:
``` bash
virtualenv -p python3 env
```

4. Activate the virtualenv
``` bash
source env/bin/activate
```
5. Install the requirements from requirements.txt file
``` bash
pip install -r requirements.txt
```
6. Create the model
``` bash
python generate_model.py
```
7. Access flask app
``` bash
cd web_app
```
8. Run the app
``` bash
python app.py
```
## Usage

 You can access the app throw:
``` bash 
http://localhost:5000/check
```
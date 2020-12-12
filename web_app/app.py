
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import joblib
import pickle

app = Flask(__name__)
app.debug = True

clf = joblib.load('../covid_predictor.pkl')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/check')
def check_form():
    return app.send_static_file('check.html')


@app.route('/check_predictor', methods=['POST'])
def check_predictor():
    dry_cough = int(request.form['dry_cough'])
    high_fever = int(request.form['high_fever'])
    sore_throat = int(request.form['sore_throat'])
    difficult_breathing = int(request.form['difficult_breathing'])
    prediction = clf.predict([[dry_cough, high_fever, sore_throat, difficult_breathing]])
    probabilities = clf.predict_proba([[dry_cough, high_fever, sore_throat, difficult_breathing]])
    probabiliy = round(float(probabilities[0][1]*100), 2)
    # create the probabiliy message
    probability_message = "({0} % risque d'infection)".format(str(probabiliy))

    # Return message based on the prediction
    if prediction[0] == 1:
        return "Vous êtes probablement atteint! " + probability_message
    else:
        return "Vous n'êtes probablement pas atteint! " + probability_message
    
    
if __name__ == '__main__':
    app.run()
 

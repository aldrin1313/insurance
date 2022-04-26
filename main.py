from flask import Flask, jsonify, render_template, request
import pickle
import numpy
import sklearn
app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def index():
    if request.method=='POST':
        try:
            age=int(request.form['age'])

            sex=request.form['sex']
            if sex=='Female':
                sex=0
            else:
                sex=1

            bmi=float(request.form['bmi'])

            children=request.form['children']

            smoker=request.form['smoker']
            if smoker=='Yes':
                smoker=1
            else:
                smoker=0

            region=request.form['region']
            if region=='North East':
                region=0
            elif region=='North West':
                region=1
            elif region=='South West':
                region=2
            else:
                region=3

            filename='final_model.pkl'
            model=pickle.load(open(filename,'rb'))
            prediction=model.predict([[age,sex,bmi,children,smoker,region]])
            print('prediction is', prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,port=8000)
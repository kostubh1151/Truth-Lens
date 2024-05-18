from flask import Flask, escape, request, render_template
import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Prediction.html', methods=['GET', 'POST'])
def Prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        Predict = model.predict(vector.transform([news]))[0]
        print(Predict)
        if Predict==0:
            Predict='FAKE'
        else:
            Predict='REAL'

        return render_template("Prediction.html", Prediction_text="News headline is--> {}".format(Predict))


    else:
        return render_template("Prediction.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
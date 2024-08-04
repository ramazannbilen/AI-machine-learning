from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("salary.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    experience = float(request.form.get("experience"))
    grade = float(request.form.get("grade"))
    interview = float(request.form.get("interview"))
    prediction = model.predict([[experience,grade,interview]])
    return render_template("index.html", prediction = "Salary predicted by AI is: ${}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)

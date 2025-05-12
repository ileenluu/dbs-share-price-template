from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return(render_template("index.html"))

@app.route("/prediction", methods=['GET', 'POST'])
def predicton():
    q = float(request.form.get('q'))
    return(render_template("prediction.html", r=(13.25*q)+2.3))

if __name__ == "__main__":
    app.run(debug=True)
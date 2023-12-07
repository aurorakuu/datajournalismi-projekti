from flask import Flask, render_template, request
from projekti import get_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        day = int(request.form["day"])
        month = int(request.form["month"])
        year = int(request.form["year"])

        result_text = get_data(day, month, year)

        return render_template("index.html", result=result_text)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


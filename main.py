from flask import Flask, render_template, request
from projekti import get_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        day = int(request.form["day"])
        month = int(request.form["month"])
        year = int(request.form["year"])

        result_list = get_data(day, month, year)
        result_date = result_list[0]
        result_text = result_list[1]

        return render_template("index.html", result_t=result_text,
                               result_d=result_date)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


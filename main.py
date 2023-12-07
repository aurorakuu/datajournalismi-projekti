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
        result_text1 = result_list[1]
        result_text2 = result_list[2]

        return render_template("index.html", result_d=result_date,
                               result_t1=result_text1, result_t2=result_text2)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


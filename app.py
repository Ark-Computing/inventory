from flask import Flask
from flask import render_template

app = Flask(__name__)

cpus = [
        {
            'name': 'i5-4690K',
            'generation': '4',
            'manufacturer': 'Intel',
            'purchased_by': 'blake',
            'qty': '1',
        }
]


@app.route("/")
@app.route("/home")
@app.route("/dashboard")
def dash():
    return render_template('dash.html', cpus=cpus, title='dashboard')


@app.route("/report")
def report():
    return render_template('report.html', title='report')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html', value='hello dsf ads fasd f')


@app.route('/about-me/<name>/<age>')
def about(name, age):
    return name + " " + age + " y. o."


app.run(debug=True)

from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'name' : "Ramya",
        'title' : "Cryptography in the era of quantum computing"
    },
    {
        'name' : "Grace",
        'title' : "Something"
    }
]

@app.route("/")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

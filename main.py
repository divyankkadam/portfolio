from flask import Flask , render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# project Page
@app.route("/project")
def project():
    return render_template("project.html")


# skill Page
@app.route("/skill")
def skill():
    return render_template("skill.html")


# certificate Page
@app.route("/certificate")
def certificate():
    return render_template("certificate.html")


if __name__ == "__main__":
    app.run(debug=True)
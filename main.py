import datetime
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def home():

    godina = datetime.datetime.now().year

    poruka = "Pozdrav iz python programa!"

    return render_template("index.html", godina=godina, poruka=poruka)

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        name = request.form.get("contact-name")
        email = request.form.get("contact-email")
        msg = request.form.get("contact-msg")

        print(name)
        print(email)
        print(msg)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", name)

        return response

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run()
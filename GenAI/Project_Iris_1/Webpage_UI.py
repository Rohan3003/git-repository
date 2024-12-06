from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages

# Dummy credentials
valid_credentials = {"admin": "password"}

@app.route("/", methods=["GET", "POST"])
def login():
    """Login Page"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Validate credentials
        if username in valid_credentials and valid_credentials[username] == password:
            return redirect(url_for("select_bu"))
        else:
            flash("Invalid username or password!")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/select_sbu/<bu>")
def select_sbu(bu):
    """Select Sub-Business Unit Page"""
    return render_template("sbu.html", bu=bu)


@app.route("/final_page/<bu>/<sbu>/<page>")
def client_page(bu, sbu, page):
    """Final Page (e.g., BMO, RBCCM)"""
    return render_template("Client.html", bu=bu, sbu=sbu, page=page)


if __name__ == "__main__":
    app.run(debug=True)

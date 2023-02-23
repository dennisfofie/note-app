from flask import Blueprint, render_template, redirect, url_for, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for('views.home'))

@auth.route("/sign-up", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(firstName) < 2:
            flash("FirstName must be greater than 1 character", category="error")
        elif len(lastName) < 2:
            flash("Last name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Password does not match", category="error")
        else:
            flash("Account created", category="success")

    return render_template("signup.html")
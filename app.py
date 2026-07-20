
from dotenv import load_dotenv
import os

from flask import Flask, render_template, request, redirect, session , flash
import mysql.connector
import bcrypt

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = db.cursor()

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        print("Login button clicked!")

        email = request.form["email"]
        password = request.form["password"]

        print(email)
        print(password)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()
        

        if user:

            stored_password = user[3]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password.encode("utf-8")
            ):

                session["user"] = email

                return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")


# Signup Page
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check passwords match
        if password != confirm_password:
            return "Passwords do not match!"

        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return "Email already registered!"

        # Hash password
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        cursor.execute(
            "INSERT INTO users(fullname,email,password) VALUES(%s,%s,%s)",
            (fullname, email, hashed_password)
        )

        db.commit()

        flash("Registration Successful! Please login.")
        return redirect("/login")

    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")
        

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
        )

        user = cursor.fetchone()
        if user:
            session["reset_email"] = email
            return redirect("/reset-password")

        else:

            flash("Email not found!")

    return render_template("forgot_password.html")

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():

    if "reset_email" not in session:
        return redirect("/forgot-password")

    if request.method == "POST":

        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            flash("Passwords do not match!")

            return redirect("/reset-password")
        
        hashed_password = bcrypt.hashpw(
             password.encode("utf-8"),
             bcrypt.gensalt()
        ).decode("utf-8")

        cursor.execute(
            "UPDATE users SET password=%s WHERE email=%s",
            (
                hashed_password,
                session["reset_email"]
            )
        )

        db.commit()

        session.pop("reset_email")

        flash("Password Reset Successfully!")
        return redirect("/login")

    return render_template("reset_password.html")


if __name__ == "__main__":
    app.run(debug=True)
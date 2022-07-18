import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import re

from helpers import apology, login_required, lookup, usd

# https://iexcloud.io/console/tokens

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    stock = db.execute(
        "SELECT symbol, SUM(number_of_shares) AS 'number_of_shares' FROM portfolio WHERE user_id = ? GROUP BY symbol HAVING SUM(number_of_shares) > 0;", user_id)
    cashOnAccount = db.execute("SELECT cash FROM users WHERE id = ? ;", user_id)
    myBalance = cashOnAccount[0]['cash']
    prices = {}
    # for each
    for share in stock:
        foo = lookup(share['symbol'])
        bar = foo['price']
        prices[share['symbol']] = bar

    return render_template("index.html", stock=stock, prices=prices, myBalance=myBalance)

@app.route("/topup", methods=["GET", "POST"])
@login_required
def topup():
    """Add money to your account"""
    if request.method =="GET":
        return render_template("topup.html")
    else:
        user_id = session["user_id"]
        funds = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']
        newFunds = int(funds) + 1000
        topup = db.execute("UPDATE users SET cash = ? WHERE id = ?", newFunds, user_id )
        return redirect("/")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # handle invalid share entries
        try:
            if int(shares) < 0:
                return apology("Must purchase a positive number of shares")
        except:
            return apology("Must purchase a number of shares")

        # check if user can afford the shares
        try:
            user_id = session["user_id"]
            funds = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            balance = funds[0]['cash']
            stock = lookup(symbol)
            totalPrice = int(int(shares) * float(stock['price']))
        except:
            return apology("something went wrong")

        if balance < totalPrice:
            return apology("Insufficient funds")
        else:
            # take user's cash
            try:
                newBalance = balance - totalPrice
                exchange = db.execute("UPDATE users SET cash = {} WHERE id = {}".format(newBalance, user_id))
            except:
                return apology("Could not debit account")

            try:
                timecheck = datetime.datetime.now()
                db.execute("INSERT INTO transactions (user_id, transaction_type, symbol, price_at_sale, number_of_shares, transaction_time) VALUES (?, ?, ?, ?, ?, ?)",
                    user_id, "purchase", symbol, stock['price'], int(shares), timecheck)
            except:
                return apology("transaction failed")

             # add stock to portfolio
            try:
                db.execute("INSERT INTO portfolio (user_id, symbol, number_of_shares) VALUES (?, ?, ?)", user_id, symbol, int(shares))
            except:
                return apology("portfolio update failed")
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    userHistory = db.execute(
        "SELECT transaction_type, symbol, price_at_sale, number_of_shares, transaction_time FROM transactions WHERE user_id = ? ;", user_id)
    return render_template("history.html", userHistory=userHistory)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        if stock:
            return render_template("quoted.html", stock=stock)
        else:
            return apology("Please provide a valid stock symbol", 400)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # added register.html
    if request.method == "GET":
        return render_template("register.html")
    else:
        newUserName = request.form.get("username")
        newPassword = request.form.get("password")
        newPasswordConfirm = request.form.get("confirmation")
        passHash = generate_password_hash(newPassword)

        # validate those inputs
        if newUserName == "":
            return apology("Please provide a user name", 400)
        elif newPassword == "":
            return apology("Please provide a password", 400)
        elif newPassword != newPasswordConfirm:
            return apology("Passwords need to match", 400)  # confirm the password

        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", newUserName, passHash)
        except:
            return apology("Please provide a unique user name")

        session["user_id"] = new_user
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    stock = db.execute(
        "SELECT symbol, SUM(number_of_shares) AS 'number_of_shares' FROM portfolio WHERE user_id = ? GROUP BY symbol;", user_id)
    if request.method == "GET":
        return render_template("sell.html", stock=stock)
    else:
        symbol = request.form.get("symbol")
        quantitySold = request.form.get("shares")

        # confirm a valid symbol was added
        list_of_bool = [True for d in stock if symbol in d.values()]
        if not any(list_of_bool):
            return apology("You must select a stock you own")

        # check if they have enough shares
        for i in range(len(stock)):
            if symbol == stock[i]['symbol']:
                if int(quantitySold) > stock[i]['number_of_shares']:
                    return apology("Insufficient shares in portfolio")

        # proceed with sale
        # take user's cash
        try:
            funds = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            balance = funds[0]['cash']
            stock = lookup(symbol)
            salePrice = int(int(quantitySold) * float(stock['price']))
            newBalance = balance + salePrice
            exchange = db.execute("UPDATE users SET cash = ? WHERE id = ? ;", newBalance, user_id)
        except:
            return apology("Could not credit account")

        try:
            timecheck = datetime.datetime.now()
            db.execute("INSERT INTO transactions (user_id, transaction_type, symbol, price_at_sale, number_of_shares, transaction_time) VALUES (?, ?, ?, ?, ?, ?)",
                user_id, "sale", symbol, stock['price'], int(quantitySold), timecheck)
        except:
            return apology("transaction failed")

        # add stock to portfolio
        try:
            db.execute("INSERT INTO portfolio (user_id, symbol, number_of_shares) VALUES (?, ?, ?)",
                        user_id, symbol, int(quantitySold) * -1)
        except:
            return apology("portfolio update failed")
        return redirect("/")

        return apology("TODO")


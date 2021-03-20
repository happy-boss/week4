from flask import Flask,request,render_template,redirect,session,url_for

app=Flask(
    __name__,static_folder="public",static_url_path="/")   

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin",methods=["POST"])
def signin():
    user=({
        "account":request.form["account"],
        "password":request.form["password"]
    })
    login=({
        "account":"test",
        "password":"test"
    })
    if user==login:
    # if request.form["account"]=="test" and request.form["password"]=="test":
        session['account'] = request.form['account']
        return redirect("/member")
                    
    else:
        return redirect("/error")
@app.route("/signout")
def signout():
    session.pop('account', None)
    return redirect("/")

@app.route("/member")
def member():
    print(session)
    if "account" in session: 
        return render_template("member.html")
    else:
        return redirect("/")    
@app.route("/error")
def error():
    return render_template("error.html")
app.run(port=3000)    
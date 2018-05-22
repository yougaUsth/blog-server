from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/user/index')
def render_index():
    return render_template("index.html",res={"status":True})


@app.route("/user/login", methods=["POST"])
def user_login():
    res = {
        "status":False,
        "msg":""
    }
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not username :
        res["msg"] = "username or password is None"
        return render_template("index.html",res=res)
    elif username != password:
        res["msg"] = "username or password is error"
        return render_template("index.html",res=res)
    else:
        res["status"] = True
        res["msg"] = "login success"

        return render_template("main.html",res=res)


if __name__ == '__main__':
    app.run()

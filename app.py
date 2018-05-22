from flask import Flask, render_template

from www.handler.user import user

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')


@app.route('/index')
def render_index():
    return render_template("index.html", res={"status": True})


if __name__ == '__main__':
    app.run()

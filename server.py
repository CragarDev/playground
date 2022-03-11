from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_cragardev():
    return "Hello Cragar, How are we doing?"


@app.route('/play')
def blue_boxes():
    return render_template("index.html")


@app.route('/play/<int:num>')
def number_of_blue_boxes(num):
    return render_template("index.html", num=num)


@app.route('/play/<int:num>/<string:color>')
def number_of_colored_boxes(num, color):
    return render_template("index.html", num=num, color=color)


@app.route('/<other>')
def other(other):
    return "Sorry! No response.\nTry again"


#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)

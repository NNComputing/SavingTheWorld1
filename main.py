from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    print(request.form["class"])
    print(request.form["Duedate"])
    print(request.form["homework"])
    return render_template("result.html")


# main driver function
if __name__ == '__main__':

  # run() method of Flask class runs the application
  # on the local development server.
  app.run(debug='true', host='0.0.0.0')

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define the correct passwords
passwords = {
    "level1": "JIGGER",
    "level2": "3:33",
  #  "level3": "apple",
    "level4": "WTC",
    "level5": "Walter White",
    "level6": "I love Breaking Bad and I aspire to be like Walter White",
    "level9": "Grape"
}

@app.route("/")
def index():
    return redirect(url_for('level1'))

@app.route("/level1", methods=["GET", "POST"])
def level1():
    if request.method == "POST":
        # We can just check if the "win" signal was sent
        return redirect(url_for('level2'))
    return render_template("level1.html")

@app.route("/level2_69", methods=["GET", "POST"])
def level2():
    if request.method == "POST":
        return redirect(url_for('level3'))
    return render_template("level2.html")

@app.route("/level3_nig", methods=["GET", "POST"])
def level3():
    if request.method == "POST":
        return redirect(url_for('level4'))
    return render_template("level3.html")

@app.route("/level4")
def level4():
    return "<h1>Congrats. Explosive Games season 2 complete</h1>"


if __name__ == "__main__":
    app.run(debug=True)
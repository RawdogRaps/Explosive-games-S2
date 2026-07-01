import logging
import os

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

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
        app.logger.info("Level 1 completed")
        return redirect(url_for('level2'))
    return render_template("level1.html")

@app.route("/level2_69", methods=["GET", "POST"])
def level2():
    if request.method == "POST":
        app.logger.info("Level 2 completed")
        return redirect(url_for('level3'))
    return render_template("level2.html")

@app.route("/level3_nig", methods=["GET", "POST"])
def level3():
    if request.method == "POST":
        app.logger.info("Level 3 completed")
        return redirect(url_for('level4'))
    return render_template("level3.html")

@app.route("/level4")
def level4():
    return "<h1>Congrats. Explosive Games season 2 complete</h1>"


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning("Page not found: %s", request.url)
    return "<h1>404 — Page Not Found</h1><p>This level doesn't exist.</p>", 404


@app.errorhandler(500)
def internal_error(e):
    app.logger.error("Internal server error: %s", e)
    return "<h1>500 — Internal Server Error</h1><p>Something went wrong.</p>", 500


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true")
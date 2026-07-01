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

# Level progression: maps each level to its template and the next level's endpoint.
LEVELS = [
    {"endpoint": "level1", "template": "level1.html", "route": "/"},
    {"endpoint": "level1", "template": "level1.html", "route": "/level1"},
    {"endpoint": "level2", "template": "level2.html", "route": "/level2_69"},
    {"endpoint": "level3", "template": "level3.html", "route": "/level3_nig"},
    {"endpoint": "level4", "template": None,           "route": "/level4"},
]


def _make_level_handler(template, next_endpoint):
    """Factory that returns a view function for a standard level page.

    Each level follows the same pattern:
      GET  -> render its template
      POST -> redirect to the next level
    """
    def handler():
        if request.method == "POST":
            return redirect(url_for(next_endpoint))
        return render_template(template)
    return handler


@app.route("/")
def index():
    return redirect(url_for('level1'))


# Register levels 1-3 using the shared handler factory
for i in range(1, 4):
    cur = LEVELS[i]
    nxt = LEVELS[i + 1]
    view = _make_level_handler(cur["template"], nxt["endpoint"])
    app.add_url_rule(
        cur["route"],
        endpoint=cur["endpoint"],
        view_func=view,
        methods=["GET", "POST"],
    )


@app.route("/level4")
def level4():
    return "<h1>Congrats. Explosive Games season 2 complete</h1>"


if __name__ == "__main__":
    app.run(debug=True)

"""`main` is the top level module for your Flask application."""

import json
from valid_sorting_network import SortingNetworkValidator

# Import the Flask Framework
from flask import Flask, request, render_template
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/validate", methods=["GET"])
def validate():
	wire_count = int(request.args.get("wc"))
	comparators = json.loads(request.args.get("c"))
	snv = SortingNetworkValidator(wire_count, comparators)
	if snv.isValid():
		return "1"
	else:
		return "0"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML = """
<h2>Vote for your favorite item</h2>
<form method="POST">
  <button name="item" value="item1">Item 1</button>
  <button name="item" value="item2">Item 2</button>
  <button name="item" value="item3">Item 3</button>
</form>
"""

RESULT_HTML = """
<h2>Results</h2>
<p>Item 1: {{ r.item1 }}</p>
<p>Item 2: {{ r.item2 }}</p>
<p>Item 3: {{ r.item3 }}</p>
<a href="/">Vote Again</a>
"""

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form.get('item')
        requests.post("http://backend:5000/vote", json={"item": item})
        r = requests.get("http://backend:5000/results").json()
        return render_template_string(RESULT_HTML, r=r)

    return HTML

app.run(host='0.0.0.0', port=3000)

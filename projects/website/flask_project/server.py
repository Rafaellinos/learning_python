from flask import Flask, render_template

app = Flask(__name__) # name of main file __name__ == __main__
"""
python3 -m venv <venv_name>
pip install flask
export FLASK_APP=server.py
export FLASK_ENV=development #debug mode
flask run
"""
@app.route('/')
def hello_world():
    return render_template('./index.html')

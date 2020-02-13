from flask import Flask, render_template, send_from_directory

app = Flask(__name__) # name of main file __name__ == __main__
"""
python3 -m venv <venv_name>
pip install flask
export FLASK_APP=server.py
export FLASK_ENV=development #debug mode
flask run
"""
@app.route('/home')
@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(f"{page_name}.html")
    except Exception as err:
        return f"page not found {err}"

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    return 'form submitted hooray'

if __name__ == '__main__':
    app.run(debug=True)

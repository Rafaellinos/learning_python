from flask import Flask, render_template, send_from_directory, request, redirect
import csv


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
def submit_form(**kw):
    # request.args.get is used to get the query param
    if request.method == 'POST':
        # can use request.form.to_dict()
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        print(f'{email}, {subject}, {message}')

        # with open('database.csv', 'a') as f:
        #     f.write(f"\nEmail: {email} | Subject: {subject} | Message: {message}")
        with open('database.csv', 'a', newline='') as f:
            csv_writter = csv.writer(f, delimiter=',')
            csv_writter.writerow([email,subject, message])

        return redirect("thankyou")
    else:
        return "Something went wrong, try again!"

if __name__ == '__main__':
    app.run(debug=True)

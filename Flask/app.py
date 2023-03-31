from flask import Flask, request, render_template
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import morph
from flaskwebgui import FlaskUI

app = Flask(__name__)

ui = FlaskUI(app, width=500, height=500)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/termination', methods=['GET', 'POST'])
def termination():
    if request.method == 'POST':
        data = request.form['data']
        S1 = morph.morph(data)
        terminate_data = S1.termination()
        

        return render_template('result.html', data=terminate_data, data2 = data)
    else:
        return render_template('form.html')
    
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    FlaskUI(app=app, server="flask").run()
    #app.run()
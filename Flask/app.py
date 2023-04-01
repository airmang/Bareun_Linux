from flask import Flask, request, render_template
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import stemmer
from flaskwebgui import FlaskUI

app = Flask(__name__)

ui = FlaskUI(app, width=500, height=500)

#홈페이지
@app.route('/')
def index():
    return render_template("index.html")


#문장 분석 페이지
@app.route('/tokenize', methods=['GET', 'POST'])
def tokenize():
    if request.method == 'POST':
        data = request.form['data']
        T1 = stemmer.tokenize(data)
        tokenize_data = T1.list()
        

        return render_template('tokenize_result.html', data=tokenize_data, sentence = data)
    else:
        return render_template('tokenize_form.html')


#어미 분석 페이지
@app.route('/termination', methods=['GET', 'POST'])
def termination():
    if request.method == 'POST':
        data = request.form['data']
        S1 = stemmer.morph(data)
        terminate_data = S1.termination()
        

        return render_template('termination_result.html', data=terminate_data, data2 = data)
    else:
        return render_template('termination_form.html')
    
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    FlaskUI(app=app, server="flask").run()
    #app.run()
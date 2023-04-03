from flask import Flask, request, render_template
import google.protobuf.text_format as tf
import os
import sys
import json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import stemmer
from flaskwebgui import FlaskUI

app = Flask(__name__)

ui = FlaskUI(app, width=500, height=500)

#홈페이지
@app.route('/')
def index():
    return render_template("index.html")


#문장 분석 페이지 (체언, 용언은 tokenize / 수식언, 관계언, 독립언은 morph)
@app.route('/tokenize', methods=['GET', 'POST'])
def tokenize():
    if request.method == 'POST':
        data = request.form['data']
        T1 = stemmer.tokenize(data)
        M1 = stemmer.morph(data)
        seg_data = M1.list()
        morph_data = T1.list()
        predicates_data = M1.predicates() # 용언
        substantives_data = M1.substantives() # 체언
        modifier_data = M1.modifier() #수식언
        relative_data = M1.relative() #관계언
        termination_data = M1.termination() #어미
        msgdata = M1.message()
        
        

        return render_template('tokenize_result.html',data = msgdata, termination_data = termination_data, relative_data = relative_data, modifier_data = modifier_data, predicates_data = predicates_data, substantives_data = substantives_data, morph_data = morph_data, seg_data = seg_data, sentence = data)
    else:
        return render_template('tokenize_form.html')


#어미 분석 페이지
@app.route('/embrace', methods=['GET', 'POST'])
def embrace():
    if request.method == 'POST':
        data = request.form['data']
        S1 = stemmer.morph(data)
        terminate_data = S1.termination()
        

        return render_template('embrace_result.html', data=terminate_data, data2 = data)
    else:
        return render_template('embrace_form.html')
    
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    FlaskUI(app=app, server="flask").run()
    #app.run()
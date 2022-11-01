import os
from flask import (
     Flask, 
     request, 
     render_template)
from model import sorayomi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        atmo = request.form['atmo']
        atmo = int(atmo)
        input_length = request.form['input_length']
        a = request.form['a']
        author,title,other = sorayomi(atmo,input_length,a)
        return render_template('result.html',author = author ,title = title ,other = other)
        
if __name__ == '__main__':
  app.run(debug=True)
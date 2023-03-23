#step 1 -import flask
from flask import Flask,render_template,request
import re

#step 2-create object with a parameter __name__
app=Flask(__name__)

#step-3 create an endpoint using route and bind them with functionality

@app.route('/',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        string=request.form['string']
        pattern=request.form['pattern']

        #finding matches
        matches_found=re.findall(pattern,string)

        #return result
        return render_template('result.html',matches_found=matches_found)
    return render_template('search.html')


#step_4 run the app

if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("model1.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict_placement():
    se_l=float(request.form.get("se_l"))
    se_w=float(request.form.get("se_w"))
    pe_l=float(request.form.get("pe_l"))
    pe_w=float(request.form.get("pe_w"))
    
    
    result=model.predict(np.array([[se_l,se_w,pe_l,pe_w]]))
    
    if result[0]==0:
        return "<h1 style='color:green'>SETOSA</h1>"
    elif result[0]==1:
        return "<h1 style='color:red'>VERSICOLOR</h1>"
    else:
        return "<h1 style='color:orange'>VIRGINICA</h1>"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
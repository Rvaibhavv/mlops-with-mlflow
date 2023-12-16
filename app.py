from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import predictionPipeline


app =Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "Training successful"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
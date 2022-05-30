from testing import *
from flask import Flask, render_template,request 

model1, model2, model3 = load_models()

app = Flask(__name__)
@app.route('/',methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    img_path = 'images/' + imagefile.filename
    imagefile.save(img_path)
    result, peluang, count = main(img_path, model1, model2, model3)
    hasil = report(result, peluang, count)
    return render_template("index.html", value = hasil )

if __name__ == '__main__':
    app.run(port=3000,debug=True)

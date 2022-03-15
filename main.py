from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def get_data():
    return render_template('data.html')

@app.route('/')
def data():
    return str(data)


if __name__=="__main__":
    app.run(port=89,debug=True)
from flask import Flask, app, render_template

app = Flask(_name_)
@app.route('/myflaskapp')
def index():
    return render_template('index.html')

if _name_ == '_main_':
    app.run(port=5000, debug=True)
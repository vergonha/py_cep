from flask import Flask, render_template, url_for, request
import cepUtils

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    getCep = request.form.get('cep')
    try:
        cep = cepUtils.findCep(getCep)
        return render_template('search.html', cep=cep)
    except:
        return render_template('error.html')

@app.route("/error")
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
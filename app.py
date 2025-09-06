from flask import Flask, render_template, request
from weather import main as get_weather 
import os


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    data = None

    if request.method == 'POST':
        city = request.form['cityN']
        state = request.form['stateN']
        country = request.form['countryN']
        data = get_weather(city,state,country)

    return render_template('index.html',data=data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


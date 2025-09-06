from flask import Flask, render_template, request
from weather import main as get_weather
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    error_message = None  # ADDED: Variable to store error messages
    
    if request.method == 'POST':
        city = request.form['cityN']
        state = request.form['stateN']
        country = request.form['countryN']
        
        # ADDED: Try-except block to catch errors
        try:
            data = get_weather(city, state, country)
        except Exception as e:
            # ADDED: Convert technical errors to user-friendly messages
            if "Location not found" in str(e):
                error_message = f"Location '{city}' not found. Please check spelling and try again."
            else:
                error_message = "Error getting weather data. Please try again."
    
    # MODIFIED: Pass error_message to template
    return render_template('index.html', data=data, error_message=error_message)

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to all interfaces (0.0.0.0) so Render can access it
    app.run(host='0.0.0.0', port=port, debug=False)
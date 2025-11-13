# Weather Application 🌤️

A Flask-based web application that provides real-time weather information for any city worldwide using the OpenWeatherMap API.

## 🌐 Live Demo

**[View Live Application](https://weather-app-beta-five-53.vercel.app/)**

Try it out now without any installation!

## Features

- 🌍 Search weather by city, Province/State, and country
- 🌡️ Displays current temperature in Celsius
- 🔍 Shows weather conditions and descriptions
- 🎨 Clean and responsive user interface
- ⚠️ User-friendly error handling for invalid locations
- 🖼️ Weather condition icons

## Project Structure

```
WEATHER_APPLICATION/
│
├── __pycache__/          # Python cache files
├── env/                  # Virtual environment
├── static/               # Static files (CSS)
│   └── index.css
├── templates/            # HTML templates
│   └── index.html
├── .env                  # Environment variables (API key)
├── app.py               # Flask application (main entry point)
├── weather.py           # Weather API logic
├── requirements.txt     # Python dependencies
├── vercel.json          # Deployment configuration


```

## Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (free tier available)

## Installation

1. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment**
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your OpenWeatherMap API key:
     ```
     API_KEY="*****"
     ```

## Getting an API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Copy your API key
5. Paste it in your `.env` file

## Usage

1. **Run the application**
   ```bash
   python app.py / python -m flask run
   ```

2. **Open your browser**
   - Navigate to `http://localhost:5000`

3. **Search for weather**
   - Enter a city name (required)
   - Enter state/province (optional)
   - Enter country name or code (required)
   - Click submit to view weather data

## Dependencies

- **Flask**: Web framework for Python
- **requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management
- **dataclasses**: Data structure for weather information

## API Endpoints

The application uses two OpenWeatherMap API endpoints:

1. **Geocoding API**: Converts location names to coordinates
   - `http://api.openweathermap.org/geo/1.0/direct`

2. **Current Weather API**: Fetches weather data for coordinates
   - `https://api.openweathermap.org/data/2.5/weather`

## Error Handling

The application includes robust error handling:
- Invalid location entries show user-friendly messages
- Network errors are caught and displayed gracefully
- Location not found errors provide helpful feedback

## Deployment

### Live Deployment on Vercel

The application is currently deployed and accessible at the live demo link above.

**Deployment Configuration:**
- Platform: Vercel
- Framework: Flask (Python)
- Configuration file: `vercel.json`
- Environment variables configured in Vercel dashboard

### Deploy Your Own

#### Deploy to Vercel

1. Fork or clone this repository
2. Sign up for a [Vercel account](https://vercel.com)
3. Import your repository in Vercel
4. Add environment variable:
   - Key: `API_KEY`
   - Value: Your OpenWeatherMap API key
5. Deploy!

#### Deploy to Render

1. Create a [Render account](https://render.com)
2. Create a new Web Service
3. Connect your repository
4. Set environment variables in the Render dashboard
5. Deploy automatically

**Environment Variables for Deployment:**
- `API_KEY`: Your OpenWeatherMap API key
- `PORT`: Automatically set by hosting platform

## Development

To contribute or modify:

1. Make changes to the code
2. Test locally using `python app.py/pyhton -m flask run`
3. Ensure all dependencies are in `requirements.txt`
4. Submit pull requests with clear descriptions

## Troubleshooting

**Location not found error:**
- Check spelling of city/country names
- Try using country codes (e.g., "US" instead of "United States")
- For cities with common names, include the state/province

**API key errors:**
- Verify your `.env` file exists and contains the API key
- Ensure there are no spaces around the `=` sign
- Check that your API key is active on OpenWeatherMap

**Module import errors:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## License

**This project is open source and available for educational purposes.**

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with Flask framework
- Icons courtesy of OpenWeatherMap

## Contact

**For questions or suggestions, please open an issue in the repository.**
## Author

**Andile Ntshangase**
## EMAIL
**vuyiswaandile176@gmail.com**

---

**Note**: Keep your `.env` file private and never commit it to version control. Add `.env` to your `.gitignore` file.
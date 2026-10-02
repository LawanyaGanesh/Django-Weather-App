# Django Weather App

A simple weather application built using **Python and Django** that fetches real-time weather information from the **OpenWeather API**.

## Features

* Search weather by city name
* Display current temperature in Celsius
* Display humidity
* Display weather description
* Handle invalid/unknown cities
* Handle API/request errors
* Uses environment variables for API configuration
* Request timeout handling

## Technologies Used

* Python
* Django
* HTML/CSS
* Requests
* OpenWeather API
* Git & GitHub

## Project Structure

```text
weather_project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── weather/
│   ├── templates/
│   │   └── weather/
│   │       └── home.html
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── .env
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd weather_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django requests python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
WEATHER_URL=https://api.openweathermap.org/data/2.5/weather
```

**Do not commit the `.env` file to GitHub.**

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/weather/
```

## What I Learned

This project helped me practice:

* Django URL routing
* Django views
* Django templates
* Handling GET and POST requests
* Calling external APIs using `requests`
* Working with JSON responses
* Nested dictionaries and lists
* HTTP status codes
* Exception handling
* Environment variables
* Git and GitHub

## Future Improvements

* Add weather icons
* Add 5-day weather forecast
* Improve UI design
* Add loading/error messages
* Add weather history

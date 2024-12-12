### INF601 - Advanced Programming in Python
### Baylee Peterson
### Final Project


# Project Title

A program helping users view weather in different NFL cities.

## Description

This program will help users decide which game would have the best weather in the next five days by asking them for the preferred date and three city options. They will enter these options then get a weather report for every 3 hours in each city. 

## Getting Started

* Download files from GitHub repository and open in PyCharm.

### Dependencies

* Flask
* Requests
* OpenWeatherMap API Key

```
pip install -r requirements.txt
```

### Installing

* Download ZIP files from GitHub repository.
* Open PyCharm and navigate to the extracted folder or cloned repository:
* Go to File → Open → Select the folder containing the project files.
* In PyCharm, create a virtual environment for the project:
* Go to File → Settings → Project: <Your Project Name> → Python Interpreter → Add Interpreter → New Environment → Choose Virtualenv.
* Open the terminal in PyCharm and install dependencies:
```
pip install -r requirements.txt
```
* Open app.py and replace your_api_key_here with your OpenWeatherMap API key:
```
API_KEY = "your_api_key_here"
```
* Confirm the directory structure is as follows:
```
project/
├── templates/       # Contains HTML templates
│   ├── index.html
│   ├── results.html
├── static/          # Contains CSS, JavaScript, or other assets
├── app.py           # Main application file
├── requirements.txt # Dependencies list
```

### Executing program

* Open the terminal in PyCharm or your project folder and run:
```
python app.py
```
* Open your browser and navigate to:
```
http://127.0.0.1:5000/
```
* Enter: Up to three NFL game locations (city names only, e.g., Denver), A specific date within the next 5 days.
* Submit the form to view weather forecast.
* The weather details (temperature, condition, and time) for the specified locations and date will be displayed on the results page.
* Use the "Search Again" button to return to the home page.

## Help

The application fetches data only for cities within the OpenWeatherMap database.
Forecasts are limited to the next 5 days and available at 3-hour intervals.


## Authors

Baylee Peterson
b_peterson4@mail.fhsu.edu

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the Baylee Peterson License - see the LICENSE.md file for details

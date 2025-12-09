# OIBSIP Python Task 1 – BMI Calculator

## Objective
To build a simple Python program that calculates the Body Mass Index (BMI) of a person based on weight and height (feet + inches format).

## Steps Performed
- Took weight input in kilograms
- Took height input in feet and inches
- Converted height to meters
- Applied BMI formula: BMI = weight / height²
- Classified the result as Underweight, Normal, Overweight, or Obese

## Tools Used
- Python 3
- VS Code

## Output in Brief
The program displays:
- Height in meters
- Calculated BMI value
- BMI category

## How to Run
```bash
python bmi_calculator.py








# OIBSIP Python Task 2 – Password Generator

## Objective
To create a secure password generator that allows users to choose password length and character types.

## Steps Performed
- Used Python's `string` and `random` modules
- Allowed users to choose:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Symbols
- Generated a random password based on user choices
- Ensured at least one character from each selected set

## Tools Used
- Python 3
- VS Code

## How to Run
```bash
python password_generator.py





---


# OIBSIP Python Task 3 – Weather App

## Objective
To create a Python program that fetches real-time weather data using the OpenWeatherMap API.

## Steps Performed
- Installed and used the `requests` module
- Took city name as input from the user
- Fetched weather data from OpenWeatherMap API
- Displayed:
  - Temperature
  - Feels like
  - Humidity
  - Weather condition

## Tools Used
- Python 3
- OpenWeatherMap API
- VS Code

## How to Run
```bash
pip install requests
python weather_app.py





---


# OIBSIP Python Task 4 – Voice Assistant

## Objective
To develop a simple voice-based assistant using Python.

## Steps Performed
- Used speech recognition and text-to-speech
- Made the assistant respond to:
  - Hello greeting
  - Time
  - Date
  - Google search
- Used Python libraries like `speech_recognition`, `pyttsx3`, `webbrowser`

## Tools Used
- Python 3
- SpeechRecognition
- pyttsx3
- VS Code

## How to Run
Install dependencies:
```bash
pip install speechrecognition pyttsx3 pyaudio





---


# OIBSIP Python Task 5 – Chat Application

## Objective
To build a simple chat application using Python socket programming where two users can exchange messages.

## Steps Performed
- Created server program to handle messages
- Created client program to connect to server
- Used socket programming for real-time communication

## Tools Used
- Python 3
- VS Code
- Socket Programming

## How to Run

### Start the Server:
```bash
python chat_server.py





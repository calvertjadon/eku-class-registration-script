# EKU Class Registration Script

This is just a simple script I threw together last year to register for classes.  The code is really bad looking back, but it works I guess.

## Requirements

- Chrome
- chromedriver
- Python 3.7
- pipenv

I have only tested this on macOS so Windows users be warned

## Installation

1. Clone this repo
2. Run `pipenv install` inside the cloned folder to setup the python environment and install dependencies
3. Create a config.json file with the following information:

```json
{
  "full_name": "First Last",
  "user_id": "901000000",
  "pin": "012345",
  "registration_term": "Fall 2019",
  "rac_number": "098765",
  "crns": ["12345", "23456", "34567", "45678", "56789", "67890"],
  "testing": false // will not click 'register' if true
}
```

4. Run `pipenv run python app.py` and cross your fingers

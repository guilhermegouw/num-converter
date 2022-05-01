# Num Converter

[![Coverage Status](./reports/coverage/coverage-badge.svg?dummy=8484744)](./reports/coverage/index.html)

Is a web application that converts a number given to it into the English words that describes that number.<br>
It exposes a GET endpoint:<br>http://127.0.0.1:8000/num_to_english?number=23<br>
 Where number is the number you want to convert to English. <br>
The output should look like this:<br>
```console
{
  "status": "ok",
  "number": "twenty three"
}
```
And a POST endpoint:<br>http://127.0.0.1:8000/num_to_english/<br>Request 
Body:
```console
{
    "number": "123"
}
```
The output should look like this:
```console
{
  "status": "ok",
  "number": "one hundred twenty three"
}
```

## How to install it?
1. Clone the repository
2. Download the dependencies
3. Configure the .env file
4. Run the tests

```console
git clone git@github.com:guilhermegouw/num-converter.git
cd num-converter
pipenv install --dev
pipenv shell
cp .env-sample .env
python manage.py test
```
If you get a warning like this one
```console
Warning: Python 3.10 was not found on your system...
```
You can run this command (or install Python 3.10 on your machine)
```console
pipenv --python path/to/python
```
And then continue with the list of commands above starting from
```console
pipenv install --dev
```
The application is integrated with Swagger OpenAPI to access it and play with the endpoints.<br>
With your virtualenv activated run:
```console
python manage.py runserver
```
And go to:
http://127.0.0.1:8000/swagger/
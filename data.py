import requests


request = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
request.raise_for_status()
data = request.json()
question_data = [question for question in data["results"]]


import requests

api_key = "354d2a166c8d479bac7be4dafb38c860"
url = ("https://newsapi.org/v2/everything?q=Google&"
       "sortBy=popularity&"
       "apiKey=354d2a166c8d479bac7be4dafb38c860")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
       print(article["title"])
       print(article["description"])
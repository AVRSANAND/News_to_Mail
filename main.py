import requests
from send_mail import send_email
api_key = "354d2a166c8d479bac7be4dafb38c860"

topic = input("Enter a topic for the articles")

url = (f"https://newsapi.org/v2/everything?q={topic}&"
       "sortBy=popularity&"
       "apiKey=354d2a166c8d479bac7be4dafb38c860&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
count = 0
articles_num = int(input("How many articles do you want ?"))
# Access the article titles and description
for article in content["articles"]:
    if count < articles_num:
        if (article["title"] != "[Removed]") and (article["title"] is not None):
            body = (body + article["title"] + "\n"
                    + article["description"] + "\n" + article["url"] + 2*"\n")
            body = "Subject: Today's News" \
            + "\n" + body
        else:
            continue
        count += 1
    else:
        break
body = body.encode("utf-8")
print(body)
send_email(body)

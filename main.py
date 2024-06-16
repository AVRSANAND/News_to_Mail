import requests
from send_mail import send_email
api_key = "354d2a166c8d479bac7be4dafb38c860"

topic = input("Enter a topic for the articles - ")

url = (f"https://newsapi.org/v2/everything?q={topic}&"
       "sortBy=publishedBy&"
       "apiKey=354d2a166c8d479bac7be4dafb38c860&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
count = 0
articles_num = int(input("How many articles do you want ? "))
while articles_num > 50:
    articles_num = int(input("Enter a number below 50! "))

# Access the article titles and description
for article in content["articles"]:
    if count < articles_num:
        if (article["title"] != "[Removed]") and (article["title"] is not None):
            body = (body + f"Title: {article['title']}" + "\n"
                    + f"Desc: {article['description']}" + "\n" + f"Link: {article['url']}" + 2*"\n")
            body = f"Subject: Today's News about {topic}" \
            + "\n" + body
        else:
            continue
        count += 1
    else:
        break

body = body.encode("utf-8")
send_email(body)

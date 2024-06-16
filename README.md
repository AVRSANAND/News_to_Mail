# News Articles to Email 

## Description

This application fetches news articles based on a specified topic using the NewsAPI and sends the articles to a specified email address. The application consists of two main components:
1. Fetching news articles from the NewsAPI.
2. Sending the fetched articles to an email address using the smtplib library.

## Files

- `main.py`: This script fetches news articles based on user input and sends the articles via email.
- `send_mail.py`: This script handles the email sending functionality.

## Prerequisites

- NewsAPI key
- Gmail account for sending emails

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/AVRSANAND/News_to_Mail.git
    cd News_to_Mail
    ```

2. **Install required libraries:**
    Ensure you have `requests` installed. You can install it using pip if it's not already installed:
    ```sh
    pip install requests
    ```

3. **Generate API keys and passwords:**
    - **NewsAPI Key:** Sign up at [NewsAPI](https://newsapi.org/) and generate your API key.
    - **Email Application Password:** If using Gmail, generate an App Password for your Google account. Refer to [Google's guide on app passwords](https://support.google.com/accounts/answer/185833?hl=en).

## Configuration

1. **Replace API Key:**
    In `main.py`, replace the placeholder API key with your own:
    ```python
    api_key = "your_newsapi_key_here"
    ```

2. **Replace Email Credentials:**
    In `send_mail.py`, replace the email credentials with your own:
    ```python
    username = "your_email@gmail.com"
    password = "your_email_app_password"
    receiver = "receiver_email@gmail.com"
    ```

## Usage

1. **Run the application:**
    ```sh
    python main.py
    ```

2. **Enter the topic:**
    When prompted, enter the topic you are interested in:
    ```
    Enter a topic for the articles - technology
    ```

3. **Enter the number of articles:**
    Enter the number of articles you want to receive (must be less than 50):
    ```
    How many articles do you want? 5
    ```

The application will fetch the specified number of articles related to the topic and send them to the specified email address.

## Improvements and Success

This application automates the process of fetching and sharing news articles, making it easier to stay informed about specific topics. By using this tool, users can quickly gather relevant news and disseminate it to interested parties without manual searching and sharing. This automation saves time and ensures that recipients receive up-to-date information efficiently.


## Notes

- Ensure that you handle your API keys and passwords securely. Avoid hardcoding them in your scripts.
- You may want to enhance the application by adding error handling and logging for better usability and maintenance.

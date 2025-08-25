import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_API_KEY = os.environ.get("ALPHA_API")
NEWS_API_KEY = os.environ.get("NEWS_API")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH")


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
yesterday = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in yesterday.items()]
yesterdays_closing_price = data_list[0]["4. close"]
the_day_before_closing_price = data_list[1]["4. close"]

difference = float(yesterdays_closing_price) - float(the_day_before_closing_price)
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "down"
difference_percent = round((difference / float(yesterdays_closing_price)) * 100)

if abs(difference_percent) > 90:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_news = articles[:3]

formatted_news = [f"{STOCK}: {up_down} {difference_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_news]

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

for article in formatted_news:
    client.messages.create(
        body=article,
        from_="your twilio number",
        to="+Your real number"
    )


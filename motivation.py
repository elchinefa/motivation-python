import requests
from pushbullet import Pushbullet

# API configuration
category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
api_key = 'pUG704+N6zXeMX8KlI1Wvg==Fqt31NR5MBNzEenj'

# Get quotes from API
response = requests.get(api_url, headers={'X-Api-Key': api_key})
if response.status_code == requests.codes.ok:
    quotes_data = response.json()

    if quotes_data:
        # Select the first quote in the list
        first_quote = quotes_data[0]
        quote = first_quote['quote']
        author = first_quote['author']

        message = f"Quote of the day: {quote} - {author}"
        print(message)

        # Send push notification using Pushbullet
        pb = Pushbullet('PUSHBULLET_API_CODE_HERE') # https://www.pushbullet.com/  
        push = pb.push_note('Motivational Quote', message)
    else:
        print("No quotes found in the response.")
else:
    print("Error:", response.status_code, response.text)



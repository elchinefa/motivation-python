import requests
import re
import json
from pushbullet import Pushbullet

def fetch_quote_from_forismatic_api():
    api_url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Extract the JSON data from the JSONP response
        json_data = re.search(r'\(({.*})\)', response.text)
        if json_data:
            quote_data = json.loads(json_data.group(1))
            quote_text = quote_data.get("quoteText", "Quote text not available")
            quote_Author = quote_data.get("quoteAuthor", "quoteAuthor not available")
            return quote_text,quote_Author

           
        else:
            return "Failed to extract JSON data from response"
    else:
        return f"Failed to retrieve a quote. Status code: {response.status_code}"

if __name__ == "__main__":
    quote, author = fetch_quote_from_forismatic_api()
    #print("Quote:")
    print(quote)
    # print("Author:")
    print(author)
    # Send push notification using Pushbullet 
    pb = Pushbullet('PUSHBULLET_API_CODE_HERE') # https://www.pushbullet.com/ 
    push = pb.push_note('Motivational Quote', quote + author)

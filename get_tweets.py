import time
import requests
import os
from dotenv import load_dotenv
from produce import tweets_producer

load_dotenv()
bearer_token = os.environ.get("BEARER_TOKEN")

def get_user_id(usernames :str):
    print('getting user id')
    usernames = usernames.replace(" ", "")
    userlookup_url = "https://api.twitter.com/2/users/by"
    query_params = {'usernames': usernames}
    json_resonse = connect_to_endpoint(userlookup_url, query_params)
    print(json_resonse)
    id = json_resonse['data'][0]['id']
    return id

def get_timeline(id):
    query_params = {'tweet.fields':'created_at', 'max_results':100}
    timeline_url = f"https://api.twitter.com/2/users/{id}/tweets"
    json_response = connect_to_endpoint(timeline_url, query_params)
    
    return json_response

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params=None):
    """
    given the url and query parameters, returns the json reponse of GET request
    """
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main(id=None):

    if not id:
        id = get_user_id('ndtv')
    
    print(id)
    json_response = get_timeline(id)
    for item in json_response['data']:
        tweets_producer.send('tweets', value = item) 
        time.sleep(2)
    


if __name__ == "__main__":
    main()

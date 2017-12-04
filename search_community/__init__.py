from googleapiclient.discovery import build
import pprint,os


my_api_key = os.getenv('API_KEY')
my_cse_id = "Custom Search Engine ID"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

print(my_api_key)
#results = google_search(
#    'stackoverflow site:en.wikipedia.org', my_api_key, my_cse_id, num=10)
#for result in results:
#    pprint.pprint(result)
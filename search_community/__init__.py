from googleapiclient.discovery import build
import pprint
import os

# Put them on Environment Variable
my_api_key = os.getenv('API_KEY')
my_cse_id = os.getenv('CSE_ID')


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


results = google_search(
   'books site:4shared.com', my_api_key, my_cse_id, num=10)
for result in results:
    "This and"
    pprint.pprint(result)

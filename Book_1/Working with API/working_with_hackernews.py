from operator import itemgetter
import requests

url='https://hacker-news.firebasio.com/v0/topstories.json'
r=requests.get(url)
print (f"Status code: {r.status_code}")

submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:30]:
  url=f'https://hacker-news.firebasio.com/v0/item/{submission_id}.json'
  r=requests.get(url)
  print (f"id: {submission_id}\tstatus: {r.status_code} ")
  response_dict=r.json()

  submission_dict={
    d
  }

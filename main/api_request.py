import requests

url = "https://ajith-holy-bible.p.rapidapi.com/GetVerses"

querystring = {"VerseTo": "8", "VerseFrom": "5", "chapter": "1", "Book": "Luke"}

headers = {
    "X-RapidAPI-Host": "ajith-holy-bible.p.rapidapi.com",
    "X-RapidAPI-Key": "be532bde6cmsh60515fab6019230p1ab77djsn2e6ba45ca46d"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())

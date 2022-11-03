import requests
import pytest

url = "https://api.duckduckgo.com"
president_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson",
                  "Van Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce",
                  "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
                  "Cleveland", "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft",
                  "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower",
                  "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush",
                  "Clinton", "Bush", "Obama", "Trump", "Biden"]


def test_url():
    resp = requests.get(url + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    presidents = []

    for president in president_list:
        for topic in rsp_data['RelatedTopics']:
            if president in topic['Text']:
                presidents.append(president)
                break
    assert presidents == president_list



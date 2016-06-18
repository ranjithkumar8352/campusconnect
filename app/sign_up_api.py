import requests
import json


def sign_up():
    url = 'https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/createProfile'
    headers = {'Content-Type': 'application/json'}
    dummy_data = dict()
    dummy_data["profileName"] = "Sarthak Shetty"
    dummy_data[
        "collegeId"] = "ahJzfnVwbG9hZG5vdGVzLTIwMTZyFAsSB0NvbGxlZ2UYgICAgICAgAoM"
    dummy_data["batchName"] = "2015"
    dummy_data["branchName"] = "Computer Science and Engineering"
    dummy_data["sectionName"] = "A"
    dummy_data["photoUrl"] = "http://www.1.jpg"
    dummy_data["email"] = "sarthakshetty1@gmail.com"
    dummy_data["gcmId"] = "invalid"
    r = requests.post(url, data=json.dumps(dummy_data), headers=headers)
    print(r)
    print(r.json())
    return(r.json())

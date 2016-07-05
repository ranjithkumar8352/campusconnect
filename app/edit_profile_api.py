import requests
import json
url = 'https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/editProfile/'
headers = {'Content-Type': 'application/json'}

def edit_profile(profileId,gcmId):
    user_profile = dict()
    user_profile["gcmId"] = gcmId
    api_call = requests.post(url+profileId, data=json.dumps(), headers=headers)
    print(api_call.json())
    return(api_call.json())

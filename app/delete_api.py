import requests
import json
from app.models import User
delete_url = 'https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/delete'
clear_all_url = 'https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/clearAll'

headers = {'Content-Type': 'application/json'}


def delete_profile(user,request):
    request.session["active"] = False
    user_profile = dict()
    user_profile["profileId"] = user.profileId
    User.objects.get(gprofileId=user.gprofileId).delete()
    api_call = requests.post(delete_url, data=json.dumps(user_profile), headers=headers)

def clear_all():
    api_call = requests.get(clear_all_url)




    
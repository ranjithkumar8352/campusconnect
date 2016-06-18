import models


def validate(profileId, gprofileId):
    try:
        user = models.User.get(profileId=profileId, gprofileId=gprofileId)
        return True
    except:
        return False

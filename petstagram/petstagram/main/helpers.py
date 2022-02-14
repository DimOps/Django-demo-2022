from petstagram.main.models import Profile


def get_profile():
    '''
    :return: Users from database
    '''
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None
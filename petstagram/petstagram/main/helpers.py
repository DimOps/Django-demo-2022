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


class BootstrapFormMixin:
    def _init_bootstrap_form_control(self):
        fields = {}
        for _, field in fields.items():

            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''

            field.widget.attrs += 'form-control'

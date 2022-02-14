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
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'

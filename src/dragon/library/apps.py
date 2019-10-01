from django.apps import AppConfig

# In order to use an app within the project
# it needs to be packaged into a name, this must
# then be added to the list of apps in `settings.py`
class LibraryConfig(AppConfig):
    name = 'library'

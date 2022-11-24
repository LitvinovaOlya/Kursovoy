from django.contrib.auth.views import LogoutView
from django.urls import path
from content.forms import ZayavkiForm

app_name = 'users'

urlpatterns = [
    path(
        'logout/', LogoutView.as_view(template_name='index.html', extra_context={'form': ZayavkiForm}),
        name='logout'
    ),
]

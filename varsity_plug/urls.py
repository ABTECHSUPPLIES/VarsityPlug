# varsity_plug/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helper.urls')),  # Your app's main routes
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login, password reset, etc.
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Direct logout path
]

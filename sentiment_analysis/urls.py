from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentiment/', include('sentiment.urls')),
    # Redirect the root URL to the sentiment page
    path('', RedirectView.as_view(url='/sentiment/', permanent=False)),
]

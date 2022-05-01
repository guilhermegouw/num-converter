from django.urls import path
from .views import NumToEnglish

urlpatterns = [
    path("", NumToEnglish.as_view()),
]

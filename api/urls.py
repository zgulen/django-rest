from django.urls import path
from api.views import ImageAPIView

urlpatterns = [
    path('id/<id>', ImageAPIView.as_view()),
]

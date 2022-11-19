from django.views.generic import ListView
from .models import Images

# Create your views here.

class ImagesListView(ListView):
    model = Images
    template_name = 'images/all_images.html'

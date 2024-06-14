from typing import Any
from django.views .generic import ListView

from product.models import Product

class IndexViews(ListView):
    model = Product
    template_name = 'index.html'
    
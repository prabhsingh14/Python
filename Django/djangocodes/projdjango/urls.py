from django.urls import path, include
from . import views

#localhost:8000/chai/
urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('stores/', views.chai_store_view, name='chai_stores'),
]
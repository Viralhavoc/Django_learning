from django.urls import path
from . import views

urlpatterns = [
	path('', views.page_1_view, name='page_1'),
]

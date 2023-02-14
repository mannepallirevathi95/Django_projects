from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>',views.WebsiteView.as_view(), name = 'website_view'),
    path('about/', views.AboutView.as_view(), name = 'about_view'),
    path('', views.PostList.as_view(), name = 'home')
]
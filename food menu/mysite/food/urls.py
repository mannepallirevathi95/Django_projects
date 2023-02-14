from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(), name = 'index'),
    #/food/1
    #path('display/',views.display, name = 'display'),
    path('<int:pk>/', views.FoodDetail.as_view(), name = 'detail'),
    # add items
    path('add',views.CreateItem.as_view(), name ='create_item'),
    #edit functionaity
    path('update/<int:id>/',views.update_item, name='update_item'),
    #/delete/
    path('delete/<int:id>/',views.delete_item, name='delete_item'),
    #/about/
    path('about/',views.about, name = 'about'),
    #/action/
    # path('action/',views.action, name = 'action'),
]


from django.urls import path
from . import views


urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('get/<str:pk>/',views.getAPI, name='get-api'),
    path('post/',views.insertAPI,name='post'),
    path('update/<str:pk>/',views.updateAPI, name='update'),
    path('delete/<str:pk>/',views.deleteAPI, name='delete'),
    path('',views.ApiOverview.as_view(), name='api-overview')

]
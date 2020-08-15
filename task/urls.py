from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('update/<int:pk>', views.updateTask, name="update"),
    path('delete/<int:pk>', views.deleteTask, name="delete")

]

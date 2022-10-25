from django.contrib import admin
from django.urls import path

from crview import views
from crview.views import home

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]

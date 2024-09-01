# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload/', views.upload_csv, name='upload_csv'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload', views.fileupload, name = "File_Uploads")
]

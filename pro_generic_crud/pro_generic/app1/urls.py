from django.urls import path
from .import views

urlpatterns=[
    path('sv/',views.ShowEmp.as_view(),name='show_url'),
    path('av/',views.AddEmp.as_view(),name='add_url'),
    path('uv/<int:pk>/',views.UpdateEmp.as_view(),name='update_url'),
    path('dv/<int:pk>/',views.DeleteEmp.as_view(),name='delete_url')
    
]
from django.urls import path
from cliente import views 

urlpatterns = [    
   path('create_client/',views.CreateClient.as_view()),

   path('list_client/',views.ListClient.as_view()),
 
    
]
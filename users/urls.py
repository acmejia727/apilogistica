from django.urls import path
from users import views 

urlpatterns = [    
    path('userlist/',views.UserList.as_view()),
    path('userlist2/',views.UserList2.as_view()),
    path('user_update/<int:pk>/',views.UserUpdate.as_view()),
    
]
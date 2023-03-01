from django.urls import path
from.import views
urlpatterns=[
    # path('index',views.index,name='index')
    path('add_student',views.add_student,name='add_student'),
   
    path('view_student',views.view_student,name='view_student'),
    path('update_student/<int:stud_id>',views.update_student,name='update_student'),
    path('delete_student/<int:stud_id>',views.delete_student,name='delete_student')
    
]
    


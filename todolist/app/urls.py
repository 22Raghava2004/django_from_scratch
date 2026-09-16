from django.urls import path
from . import views


urlpatterns = [
   path( "",views.task_home,name='task_home'),
   path('addtask/',views.add_task,name='add_task'),
   path('deletetask/<int:task_id>/',views.delete_task,name='delut_task'),

   path('completetask/<int:task_id>/',views.complete_task,name='complete_task'),
   path('signup/',views.signup,name='sign_pop'),
   path('login/',views.login_user,name='login'),
      path('logout/',views.logout_user,name='logout'),


   

]

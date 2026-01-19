from django.urls import path , include
from . import views


urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.comment_list,name="comment_list"),
    path('create_comment/',views.create_comment,name="create_comment"),
    path('update_comment/<int:comment_id>',views.update_comment,name="update_comment"),
    path('delete_comment/<int:comment_id>',views.delete_comment,name="delete_comment"),
    path('register/',views.register,name="register"),
    
]  
 
from django.conf.urls import url
from django.urls import include,path
from blog import views

urlpatterns = [
    path('about/', views.AboutView.as_view(),name = 'about'),
    path('',views.PostListView.as_view(), name = 'post_list'),
    path('post/', views.PostDetailView.as_view(),name = 'post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name ='post_new'),
    path('post/edit/',views.PostUpdateView.as_view(),name ='post_edit'),
    path('post/remove/',views.PostDeleteView.as_view(),name ='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name ='post_draft_list'),
    path('post/comment/',views.add_comment_to_post,name ='add_comment_to_post'),
    path('comment/approve/',views.comment_approve,name ='comment_approve'),
    path('comment/remove',views.comment_remove,name ='comment_remove'),
    path('post/publish',views.comment_remove,name ='post_publish'),

]
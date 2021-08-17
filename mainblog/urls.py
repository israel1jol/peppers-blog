from django.urls import path
from mainblog.views import Index, PostDetail, addComment, PostCategory, About

app_name = 'mainblog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('recents/<slug:slug>/', PostDetail.as_view() ,name='detailpost'),
    path('recents/<slug:post_slug>/submitComment/', addComment,name='addcomment'),
    path('category/<str:string>/', PostCategory.as_view(),name='category'),
    path('category/<str:string>/<slug:slug>/', PostDetail.as_view() ,name='categorypost'),
    path('about/', About.as_view(), name='about')
]
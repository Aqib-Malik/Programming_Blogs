import imp
from django.urls import path,include
from .views import CategoryViewSet, PostCatView, PostView, PostViewset,ProfileViewset, ProfiletwoViewset
from .views import PostView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token####login etc
from django.conf.urls.static import static
from django.conf import settings
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI,FindPost


routers=DefaultRouter()
routers.register('profile',ProfileViewset,basename='profile')
# routers.register('profile_two',ProfiletwoViewset,basename='profile_two')
routers.register('category',CategoryViewSet,basename='category')
# routers.register('image',ImageViewSet,basename='image')
routers.register('post',PostViewset,basename='post')

urlpatterns = [
    path('fp/',FindPost.as_view()),
    path('cat/',include(routers.urls),),
    path('',PostView.as_view()),
    
    path('<int:cid>/',PostCatView.as_view()),
    path('prof/<int:cid>/',ProfiletwoViewset.as_view()),
    #path('login/',obtain_auth_token),
    path('api/register/', RegisterAPI.as_view(), name='register'),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
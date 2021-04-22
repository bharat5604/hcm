from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', dashboard, name='web_dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('change_action/<str:objectType>/<int:objectId>/', change_action, name='change_action'),
    path("site_settings/view/<str:objectSlug>/", show_object_list, name="show_object_list"),
    path("site_settings/create/<str:objectSlug>/", model_object, name="model_object"),
    path('saveObject/<str:objectSlug>/', saveObject,name='saveObject'),
    path('updateObject/<str:objectSlug>/<int:objectId>/', updateObject,name='updateObject'),
    path('deleteObject/<str:objectSlug>/<int:objectId>/', deleteObject,name='deleteObject'),
]

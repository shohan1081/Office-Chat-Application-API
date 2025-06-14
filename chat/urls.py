from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_websocket, name='test_websocket'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('history/<str:room_name>/', views.ChatHistoryView.as_view(), name='chat_history'),
    path('upload/', views.FileUploadView.as_view(), name='file_upload'),
]
from django.urls import path
from .views import AllSnapPrograms

urlpatterns = [
   
    path('all-snap-data/', AllSnapPrograms.as_view(), name='all-snap-data?'),
    # path("login/", Log_In.as_view(), name="login"),
    # path("logout/", Log_Out.as_view(), name="logout"),    
    # path('info/', Info.as_view(), name='info')
]
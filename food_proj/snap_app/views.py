from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import SnapData, StateSnapProgram, ApplicationInfo
from .serializers import SnapDataSerializer, StateSnapProgramSerializer, ApplicationInfoSerializer

# Create your views here.

class AllSnapPrograms(APIView):

    def get(self):
        all_snap = SnapDataSerializer(SnapData.objects, many = True)
        return Response(all_snap.data, status=HTTP_200_OK)
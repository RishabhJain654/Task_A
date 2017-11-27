from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StringData
from .serializers import StringDataSerializer


class StringDataList(generics.ListCreateAPIView):
    queryset = StringData.objects.all()
    serializer_class = StringDataSerializer

    def get(self, request, format=None):
        string_data = StringData.objects.all()
        serializer = StringDataSerializer(string_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StringDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)

class StringDataDetail(APIView):
    def get_object(self, pk):
        try:
            return StringData.objects.get(pk=pk)
        except StringData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        string_data = self.get_object(pk)
        serializer = StringDataSerializer(string_data)
        return Response(serializer.data)

def home(request):
    return redirect('ping')

def ping(request):
    return HttpResponse("pong")

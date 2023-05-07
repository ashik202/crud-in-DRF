from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializer import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Producr

# Create your views here.
# class ProductView(APIView):
#     def post(self,request):
#         serilizer=ProductSerializer(data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data,status=status.HTTP_201_CREATED)
#         return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def get(self,request,id=None):
#         if id==None:
#             data = Producr.objects.all()
#             print(data)
#             serializer = ProductSerializer(data, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             data = Producr.objects.get(pk=id)
#             print(data)
#             serializer = ProductSerializer(data)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self,request,formate=None):
#             print(request.data)
#             data=Producr.objects.get(pk=request.data["id"])
#             serializer=ProductSerializer(instance=data,data=request.data)
#             if serializer.is_valid():
#                  serializer.save()
#                  return Response(serializer.data,status=status.HTTP_200_OK)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductView(ViewSet):
    """for get all data"""
    def list(self,request):
        data=Producr.objects.all()
        serializer=ProductSerializer(data,many=True)
        return Response (serializer.data)
    """for get single data"""
    def retrieve(self,request,pk=None):
        data = Producr.objects.get(pk=pk)
        serializer = ProductSerializer(data)
        return Response(serializer.data)
    """for create data"""
    def create(self, request):
        serilizer=ProductSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    """for update data partialy """
    def partial_update(self,request,pk):
        obj=Producr.objects.get(pk=pk)
        serializer=ProductSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg':'update susseccfully'},status.HTTP_200_OK)
        return Response(serializer.errors)





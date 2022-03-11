from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PerusahaanSerializer, PerusahaanCreateUpdateSerializer, PekerjaSerializer
from .models import Perusahaan, Pekerja

class PerusahaanView(APIView):
     def post(self, request):
          serializer = PerusahaanCreateUpdateSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(
                    {
                         "data": serializer.data
                    },
                    status=status.HTTP_201_CREATED
               )
          else:
               return Response(
                    {
                         "error": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
     
     def get(self, request, pk=None):
          if pk:
               perusahaan = get_object_or_404(Perusahaan, pk=pk)
               serializer = PerusahaanSerializer(perusahaan)
               return Response(
                    {
                         "data": serializer.data
                    },
                    status=status.HTTP_200_OK
               )
          perusahaans = Perusahaan.objects.all()
          serializer = PerusahaanSerializer(perusahaans, many=True)
          return Response(
               {
                    "data": serializer.data
               },
               status=status.HTTP_200_OK
          )

     def put(self, request, pk=None):
          perusahaan = get_object_or_404(Perusahaan, pk=pk)
          serializer = PerusahaanCreateUpdateSerializer(perusahaan, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(
                    {
                         "data": serializer.data
                    },
                    status=status.HTTP_200_OK
               )
          else:
               return Response(
                    {
                         "error": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
     def delete(self, request, pk=None):
          perusahaan = get_object_or_404(Perusahaan, pk=pk)
          perusahaan.delete()
          return Response(
               {
                    "message": "Item Deleted"
               },
               status=status.HTTP_200_OK
          )

class PekerjaView(APIView):
     def post(self, request):
          serializer = PekerjaSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(
                    {
                         "data": serializer.data
                    },
                    status=status.HTTP_201_CREATED
               )
          else:
               return Response(
                    {
                         "error": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
     
     def get(self, request, pk=None):
          if pk:
               pekerja = get_object_or_404(Pekerja, pk=pk)
               serializer = PekerjaSerializer(pekerja)
               return Response(
                    {
                         "data": serializer.data
                    },
                    status=status.HTTP_200_OK
               )
          pekerjas = Pekerja.objects.all()
          serializer = PekerjaSerializer(pekerjas, many=True)
          return Response(
               {
                    "data": serializer.data
               },
               status=status.HTTP_200_OK
          )

     def put(self, request, pk=None):
          pekerja = get_object_or_404(Pekerja, pk=pk)
          serializer = PekerjaSerializer(pekerja, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(
                    {
                         "data": serializer.data
                    },
                    status=status.HTTP_200_OK
               )
          else:
               return Response(
                    {
                         "error": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
     def delete(self, request, pk=None):
          pekerja = get_object_or_404(Pekerja, pk=pk)
          pekerja.delete()
          return Response(
               {
                    "message": "Item Deleted"
               },
               status=status.HTTP_200_OK
          )
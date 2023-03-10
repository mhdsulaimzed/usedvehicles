from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from vehicles.serializers import VehicleSerializer
from vehicles.models import Vehicles

class VehiclesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        sz=VehicleSerializer(qs,many=True)
        return Response(data=sz.data)
    def post(self,request,*args,**kwargs):
        # qs=Vehicles.objects.create(**request.data)
        sz=VehicleSerializer(data=request.data)
        if sz.is_valid():
            Vehicles.objects.create(**sz.validated_data)
            return Response(data=sz.data)
        else:
            return Response(sz.errors)
class VehiclesDet(APIView):
    def get(self,req,*args,**kw):
        id=kw.get("id")
        qs=Vehicles.objects.get(id=id)
        sz=VehicleSerializer(qs)
        return Response(sz.data)










#         if sz.is_valid():
#             print(sz.validated_data)
#             Vehicles.objects.create(**sz.validated_data)
#             return Response(data=sz.data)
#         else:
#             return Response(data=sz.errors)

# class VehiclesDetailsView(APIView):
#     def get(self,request,*args,**kwargs):
#         id= kwargs.get("id")
#         qs=Vehicles.objects.get(id=id)
#         sz=VehicleSerializer(qs)
#         return Response(data=sz.data)
#     def delete (self, request, *args, **kwargs):
#         id=kwargs.get("id")
#         Vehicles.objects.filter(id=id).delete()
#         return Response(data="deleted")
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         sz=VehicleSerializer(data=request.data)
#         if sz.is_valid():
#             Vehicles.objects.filter(id=id).update(**sz.validated_data)
#             return Response(data=sz.data)
#         else:
#             return Response(data=sz.errors)


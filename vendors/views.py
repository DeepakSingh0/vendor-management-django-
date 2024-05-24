# views.py
from rest_framework import generics, status
from .models import Vendor
from rest_framework.response import Response
from .serializers import VendorSerializer
from django.http import Http404

class VendorListCreate(generics.ListCreateAPIView):
    # queryset = Vendor.objects.all()
    # serializer_class = VendorSerializer
    
    def get(self, request, format=None):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response({
            "message": "All Vendors List.",
            "count": Vendor.objects.count(),
            "data": serializer.data
        })
    
    def post(self, request, format=None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Vendor created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Failed to create vendor. Please check your input data.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "message": "Vendor retrieved successfully.",
            "data": serializer.data
        })
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Vendor updated successfully.",
                "data": serializer.data
            })
        else:
            return Response({
                "message": "Failed to update vendor.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Vendor deleted successfully."})

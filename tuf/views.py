from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Hospital
from .serializers import HospitalSerializer


class HospitalView(APIView):


    # GET METHOD
    def get(self, request):

        hospital = Hospital.objects.all()

        serializer = HospitalSerializer(hospital, many=True)

        return Response(serializer.data)



    # POST METHOD
    def post(self, request):

        serializer = HospitalSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)



class HospitalDetailView(APIView):


    def get_object(self, id):

        return Hospital.objects.get(id=id)



    # PUT METHOD
    def put(self, request, id):

        hospital = self.get_object(id)

        serializer = HospitalSerializer(
            hospital,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)



    # PATCH METHOD
    def patch(self, request, id):

        hospital = self.get_object(id)

        serializer = HospitalSerializer(
            hospital,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)



    # DELETE METHOD
    def delete(self, request, id):

        hospital = self.get_object(id)

        hospital.delete()

        return Response("Hospital Deleted")
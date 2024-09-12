from django.shortcuts import render
from .serializers import MovieSerializer,GuestSerializer,ReservationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,APIView
from rest_framework.permissions import IsAuthenticated
from .models import Guest,Movie,Reservation
import json
from django.http.response import JsonResponse
from rest_framework import mixins,generics
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Q

# Create your views here.

# 1 without rest_framweork and no model query
def no_rest_model(request):
    guests = [{
        'id':'1',
        'name':'mina',
        'mobile':'0125465'
    },
    {
        'id':'2',
        'name':'kero',
        'mobile':'13265'
    },
    
    ]
    
    return JsonResponse(guests,safe=False)
# 2 no rest_framwork but   from model query 
def no_rest_but_from_model(request):
    guest = Guest.objects.all().values()
 
    return JsonResponse(list(guest),safe=False)

# 3 function based views
# 3.1 GET POST Guests
@api_view(['GET','POST'])
def fbv_list(request):
    try:
        if request.method == 'GET' :
            guest = Guest.objects.all()
            serializer = GuestSerializer(guest,many =True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        if request.method == 'POST' :
            data = request.data
            serializer =GuestSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend{ex}'},status=status.HTTP_400_BAD_REQUEST)

# 3.2 GET PUT DELETE Guests
@api_view(['GET','PUT','DELETE'])
def fbv_pk_guest(request,pk):
    try:
        if request.method == 'GET' :
            guest = Guest.objects.get(id =pk)
            serializer = GuestSerializer(guest)
            return Response(serializer.data,status=status.HTTP_200_OK)
        if request.method == 'PUT' :
            data = request.data
            guest = Guest.objects.get(id =pk)
            serializer =GuestSerializer(data=data,instance =guest,partial =True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE' :
            guest = Guest.objects.get(id =pk)
            guest.delete()
        return Response({'successful':'gust id deleted '},status=status.HTTP_204_NO_CONTENT)
    except Guest.DoesNotExist :
        return Response({'error':f'gust not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex :
        return Response({'error':f'error happend{ex}'},status=status.HTTP_400_BAD_REQUEST)

# 3.3 GET POST reservtion
@api_view(['GET','POST'])
def fbv_list_reservtion(request):
    try:
        if request.method == 'GET' :
            reservation = Reservation.objects.all()
            serializer = ReservationSerializer(reservation,many =True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        if request.method == 'POST' :
            data = request.data
            serializer =ReservationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend{ex}'},status=status.HTTP_400_BAD_REQUEST)

# 4.1 GET POST class based views

class CBV_List(APIView):
    def get(self,request):
        guest = Guest.objects.all()
        serializer =GuestSerializer(guest,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializer =GuestSerializer(data =data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# 4.2 GET PUT DELETE class based views
class CBV_PK(APIView):
    def get(self,request,pk):
        try :
            guest = Guest.objects.get(id =pk)
            serializer =GuestSerializer(guest)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Guest.DoesNotExist :
            return Response({'error':'guest not found'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex :
            return Response({'error':f'error happend{ex}'},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            guest = Guest.objects.get(id =pk)
            data = request.data
            serializer =GuestSerializer(data =data,instance =guest,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Guest.DoesNotExist :
            return Response({'error':'guest not found'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex :
            return Response({'error':f'error happend{ex}'},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            guest = Guest.objects.get(id =pk)
            guest.delete()
            return Response({'mesage':'gust is deleted'},status=status.HTTP_204_NO_CONTENT)
        except Guest.DoesNotExist :
            return Response({'error':'guest not found'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex :
            return Response({'error':f'error happend{ex}'},status=status.HTTP_400_BAD_REQUEST)
        
# 5.1 GET POST mixins
class Mixins_List(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Guest.objects.all()
    serializer_class  = GuestSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
# 5.2 GET PUT DESTROY mixins
class Mixins_pk(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Guest.objects.all()
    serializer_class  = GuestSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request) 
    
    def delete(self,request,pk):
        return self.destroy(request)
    
# 6.1 GET POST Generics
class Generics_List(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# 6.2 GET PUT DELETE Generics
class Generics_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# 7.1  viewsets
class Viewsets_Guests(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class Viewsets_Movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']
class Viewsets_Reverstion(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# 8.1 find movie
@api_view(['GET'])
def find_movie(request):
    try : 
        print('data==',request.data)
        movie = Movie.objects.filter(Q(movie = request.data['movie']) | Q(hall=request.data['hall']))
       # movie = Movie.objects.filter(movie = request.data['movie']) | Movie.objects.filter(hall=request.data['hall'])


        if movie :
            serializer = MovieSerializer(movie,many = True)
            return Response(serializer.data)
        else :
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex :
        return Response({'error':f'error hapend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 9.1 create new reverstion
@api_view(['POST'])
def new_reservation(request):
   # مشكلة الانشاء مع العرض 
  
    try : 
        data = request.data
        print('data====',data)
        serializer = ReservationSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex :
        return Response({'error':f'error happened {ex}'},status=status.HTTP_400_BAD_REQUEST)
   
   
     
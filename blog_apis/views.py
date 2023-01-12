from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.contrib import auth


# class RegisterView(APIView):
#
#     def post(self, request):
#         try:
#             data=request.data
#             serializer = RegisterSerializer(data=data)
#             if not serializer.is_valid():
#                 return Response(
#                     {
#                         'data':serializer.errors,
#                         'message':'Something went wrong'
#                     }
#                 , status=status.HTTP_400_BAD_REQUEST)
#
#             serializer.save()
#             return Response(
#                 {
#                     'data': {},
#                     'message': 'Account created'
#                 }
#                 , status=status.HTTP_201_CREATED)
#
#         except Exception as e:
#             return Response({
#                 'data':{},
#                 'message': 'Something went wrong'
#
#             } , status=status.HTTP_400_BAD_REQUEST)
#

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)

        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'data':serializer.errors,
                'message':'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

        response = serializer.get_jwt_token(serializer.data)

        return Response(response,   status=status.HTTP_200_OK)





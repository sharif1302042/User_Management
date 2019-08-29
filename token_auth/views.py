from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            return Response({"message":"Hello Dear"},status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({"message":"You are Failed"},status=status.HTTP_400_BAD_REQUEST)



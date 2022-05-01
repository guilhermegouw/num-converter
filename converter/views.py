from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NumberToEnglishRequestSerializer
from .utils import Converter


class NumToEnglish(APIView):
    converter = Converter()
    number_param = openapi.Parameter('number', in_=openapi.IN_QUERY, description='number to be converted to english', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[number_param])
    def get(self, request):
        number = request.GET.get("number")
        try:
            english = self.converter.integer_to_english(int(number))
            json_english = {"status": "ok", "number": english}
        except (ValueError, TypeError):
            json_error = {
                "status": "Error",
                "message": "Please insert an integer number",
            }
            return Response(json_error, status=status.HTTP_400_BAD_REQUEST)
        return Response(json_english, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=NumberToEnglishRequestSerializer)
    def post(self, request):
        """Convert a string of numbers to its respective value in english."""
        data = request.data
        try:
            number = data["number"]
            english = self.converter.integer_to_english(int(number))
            json_english = {"status": "ok", "number": english}
        except (ValueError, KeyError):
            json_error = {"status": "Error", "message": "This is not a valid payload"}
            return Response(json_error, status=status.HTTP_400_BAD_REQUEST)
        return Response(json_english)

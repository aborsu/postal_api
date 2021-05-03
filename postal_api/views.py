from drf_spectacular.utils import extend_schema
from drf_yasg import openapi
from postal.expand import expand_address
from postal.parser import parse_address
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AddressSerializer, ParsedAddressSerializer

test_param = openapi.Parameter(
    "test", openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN
)

parsed_address_response = openapi.Response("parsed address", ParsedAddressSerializer)


@extend_schema(
    methods=["POST"],
    request=AddressSerializer,
    responses={200: ParsedAddressSerializer, 500: None, 400: None,},
)
@api_view(["POST"])
def parse_address_api(request):
    input_serializer = AddressSerializer(data=request.data)
    if input_serializer.is_valid():
        address = input_serializer.validated_data["address"]
        parsed_address = {k: v for v, k in parse_address(address)}
        output_serializer = ParsedAddressSerializer(data=parsed_address)
        if output_serializer.is_valid():
            return Response(output_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                output_serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    methods=["POST"],
    request=AddressSerializer,
    responses={200: AddressSerializer(many=True), 500: None, 400: None,},
)
@api_view(["POST"])
def expand_address_api(request):
    input_serializer = AddressSerializer(data=request.data)
    if input_serializer.is_valid():
        address = input_serializer.validated_data["address"]
        expanded_addresses = [{"address": a} for a in expand_address(address)]
        output_serializer = AddressSerializer(data=expanded_addresses, many=True)
        if output_serializer.is_valid():
            return Response(output_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                output_serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

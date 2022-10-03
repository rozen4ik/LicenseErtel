from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TokenErtelSerializer
from license_server.models import TokenErtel


@api_view(['GET', 'PUT', 'DELETE'])
def api_post_token(request, token_mobile):
    try:
        tokens = TokenErtel.objects.get(token=token_mobile)
        if tokens.number_of_activated_devices < tokens.number_of_activations:
            tokens.number_of_activated_devices += 1
            tokens.save()
        else:
            return Response(data="Превышено количество активаций")
    except TokenErtel.DoesNotExist:
        return Response(data="Отказано в активации, ключ не действительный")

    if request.method == 'GET':
        serializer = TokenErtelSerializer(tokens)
        return Response(serializer.data)

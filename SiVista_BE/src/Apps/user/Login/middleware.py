from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
import datetime
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_simplejwt.settings import api_settings
from rest_framework import status



class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in['/api/login/','/api/token/refresh/'] :
            response = self.get_response(request)   
            return response
        else:
            authorization_header = request.headers.get('Authorization') 
            refresh_token = request.headers.get('Refresh')
            call_url=request.path

            try:

                if authorization_header:
                    if authorization_header.startswith('Bearer '):
                        token = authorization_header.split(' ')[1]
                        decoded_access_payload = jwt_decode_handler(token)
                        print(decoded_access_payload)
                        if float(decoded_access_payload['exp'])< datetime.datetime.now().timestamp():
                            # Token has expired, attempt to refresh
                            return JsonResponse({'message': 'Token has expired.',  'status':status.HTTP_401_UNAUTHORIZED})
                        else: 
                            response = self.get_response(request)   
                            return response
                    else:
                        return JsonResponse({'message': 'Invalid token type.', 'status':status.HTTP_401_UNAUTHORIZED})
                elif refresh_token:
                    decoded_refresh_payload = jwt_decode_handler(refresh_token)
                    if float(decoded_refresh_payload['exp']) > datetime.datetime.now().timestamp():
                        
                        return JsonResponse({'message': 'Generate new access token', 'status':status.HTTP_401_UNAUTHORIZED,'Current_request':call_url})
                    else: 
                        return JsonResponse({'message': 'Refresh token has expired ', 'status':status.HTTP_401_UNAUTHORIZED})

            except (IndexError, TokenError, InvalidToken) as e:
                print(e)

            
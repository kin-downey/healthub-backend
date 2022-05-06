from pdb import post_mortem
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
import requests
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from dotenv import load_dotenv
load_dotenv(override=True)
import os

User = get_user_model()


class UserList(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


def test(request, uid, token):
    url = "http://localhost:8000/api/auth/users/activation/"
    payload = {'uid': uid,
            'token': token}
    files = []
    headers = {
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    if response.status_code == 204:
        return HttpResponseRedirect(('http://localhost:8080/registed'))
    elif response.status_code == 403:
        return HttpResponseRedirect(('http://localhost:8080/registererror'))
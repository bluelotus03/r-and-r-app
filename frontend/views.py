from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Create your views here.

def homepage(request):
    users_query_set = Users.objects.all()
    print('#'*25)
    print('# All DB row items')
    for user in users_query_set:
        print('{} {}: {}'.format(user.fname, user.lname, user.email))
    print('#'*25)
    return render(request, 'hello.html', { 'name': 'ash', 'users': users_query_set})

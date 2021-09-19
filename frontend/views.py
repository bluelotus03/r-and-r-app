from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Created my views below.

def homepage(request):
    users_query_set = Users.objects.all()
    print('#'*25)
    print('# All DB row items')
    for user in users_query_set:
        print('{} {}: {}'.format(user.fname, user.lname, user.email))
    print('#'*25)
    return render(request, 'list_users.html', {'users': users_query_set})

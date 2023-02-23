from django.shortcuts import render
from django.http import HttpResponse 
'An HTTP response class with a string as content.'
import random
# Create your views here.
""" return render(request,'generator/home.html',{'password':'dndjon'})"""
def home(request):
    return render(request,'generator/home.html')


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    """get('length') denotes the name of the tag in the home.html file and 12 denotes the default value for it when user doesn't enter anything"""
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special characters'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    

    length = int(request.GET.get('length',12))
    thepswd = ''

    for x in range(length):
        thepswd += random.choice(characters)

    """{'password':thepswd} - dictionary/map"""

    return render(request,'generator/password.html',{'password':thepswd})
